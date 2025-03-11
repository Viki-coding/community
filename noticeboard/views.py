from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Event, Booking, CommunityUser
from .forms import EventForm, UserForm, CommunityUserForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.text import slugify
from django.utils import timezone
from django.core.paginator import Paginator


def is_facilitator(user):
    """
    Check if the user is in the facilitator group.
    """
    return user.groups.filter(name="Facilitators").exists()


@login_required
@user_passes_test(is_facilitator)
def facilitator_dashboard(request):
    """
    Display the facilitator dashboard with events they manage.
    Use prefetch_related to reduce the number of queries.
    """
    events = Event.objects.filter(facilitator=request.user).prefetch_related(
        "booking_set__user"
    )
    return render(
        request, "noticeboard/facilitator_dashboard.html", {"events": events}
    )


@login_required
def book_event(request, event_id):
    """
    Allow a community user to book an event if conditions are met.
    """
    event = get_object_or_404(Event, id=event_id)
    # Check if the user is a facilitator
    if is_facilitator(request.user):
        messages.error(
            request,
            "Facilitators cannot book events. "
            "Create a separate user account to book events."
        )
        return redirect("event_detail", event_id=event_id)

    # Check if the user is a community user
    community_user = getattr(request.user, "communityuser", None)
    if not community_user:
        messages.error(request, "Create a User profile to book events.")
        request.session["event_id"] = event_id
        return redirect("create_community_user")

    # Check if the booking deadline has passed
    if event.booking_deadline and event.booking_deadline < timezone.now():
        messages.error(request, "SORRY! BOOKING DEADLINE HAS PASSED.")
        return redirect("event_detail", event_id=event_id)

    # Check if the event capacity has been reached
    if Booking.objects.filter(event=event).count() >= event.capacity:
        messages.error(request, "SORRY! EVENT CAPACITY HAS BEEN REACHED.")
        return redirect("event_detail", event_id=event_id)

    # Check if the user has already booked the event
    if Booking.objects.filter(event=event, user=community_user).exists():
        messages.error(request, "YOU HAVE ALREADY BOOKED THIS EVENT.")
        return redirect("event_detail", event_id=event_id)

    # Create a booking for the user
    Booking.objects.create(event=event, user=community_user)
    messages.success(
        request,
        "THANK YOU - EVENT BOOKED SUCCESSFULLY. "
        "CLICK ON DASHBOARD TO VIEW / DELETE YOUR BOOKING.",
    )
    return redirect("event_detail", event_id=event_id)


def login_view(request):
    """
    Manage user login and redirection based on user type (facilitator/user).

    Returns:
        Facilitator dashboard: If logged in and is in facilitator group.
        User dashboard: If logged in as a community user.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect to facilitator dashboard if the user is a facilitator
            if is_facilitator(user):
                return redirect("facilitator_dashboard")

            # Check if the user is a community user
            try:
                user.communityuser
                return redirect("user_dashboard")
            except CommunityUser.DoesNotExist:
                messages.error(request, "Create User profile to book events.")
                return redirect("create_community_user")

            # Redirect to event booking page if an event_id is stored in the
            # session
            event_id = request.session.pop("event_id", None)
            if event_id:
                return redirect("book_event", event_id=event_id)
            return redirect("index")

        else:
            messages.error(request, "Invalid username or password")
            return render(request, "noticeboard/login.html")

    return render(request, "noticeboard/login.html")


def create_community_user(request):
    """
    Handle the creation of a community user.
    """
    if request.method == "POST":
        user_form = UserForm(request.POST)
        community_user_form = CommunityUserForm(request.POST)
        if user_form.is_valid() and community_user_form.is_valid():
            user = user_form.save()
            community_user = community_user_form.save(commit=False)
            community_user.user = user
            community_user.save()
            login(request, user)
            messages.success(
                request,
                "Thank you for registering as a user. You are now logged in.",
            )
            # Redirect to the event booking page if an event_id is stored in
            # session
            event_id = request.session.pop("event_id", None)
            if event_id:
                return redirect("book_event", event_id=event_id)
            return redirect("user_dashboard")
        else:
            messages.error(request, "Please correct the errors below.")
            print(user_form.errors, community_user_form.errors)
    else:
        user_form = UserForm()
        community_user_form = CommunityUserForm()

    return render(
        request,
        "noticeboard/create_community_user.html",
        {"user_form": user_form, "community_user_form": community_user_form},
    )


@login_required
def user_dashboard(request):
    """
    Display the dashboard for community users, showing their booked events.
    """
    community_user = getattr(request.user, "communityuser", None)
    if not community_user:
        messages.error(request, "Create a User profile to book events.")
        return redirect("create_community_user")

    bookings = Booking.objects.filter(user=community_user).select_related(
        "event"
    )
    return render(
        request, "noticeboard/user_dashboard.html", {"bookings": bookings}
    )


@login_required
def cancel_booking(request, booking_id):
    """
    Allow a community user to cancel a booking.
    """
    community_user = getattr(request.user, "communityuser", None)
    if not community_user:
        messages.error(request, "Create a User profile to manage bookings.")
        return redirect("create_community_user")

    booking = get_object_or_404(
        Booking, id=booking_id, user=community_user
    )
    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking has been cancelled.")
        return redirect("user_dashboard")
    return render(request, "noticeboard/user_dashboard.html")


def index(request):
    """
    Display the events on the noticeboard.
    Display events based on category filter.
    """
    category = request.GET.get("category")
    if category:
        events = Event.objects.filter(category=category)
    else:
        events = Event.objects.all()

    # Pagination
    paginator = Paginator(events, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Event.CATEGORY_CHOICES
    return render(
        request,
        "noticeboard/index.html",
        {"page_obj": page_obj, "categories": categories},
    )


class EventList(generic.ListView):
    """
    List all events, ordered by creation date (most recent first).
    """

    model = Event
    queryset = Event.objects.order_by(
        "-created"
    )  # Order in descending order from the most recent to the oldest
    template_name = "noticeboard/index.html"
    paginate_by = 3


def event_detail(request, event_id):
    """
    Display the full details of a specific event.
    """
    event = get_object_or_404(Event, id=event_id)
    user_is_facilitator = is_facilitator(request.user)
    user_has_booked = False

    if not user_is_facilitator:
        community_user = getattr(request.user, "communityuser", None)
        if community_user:
            user_has_booked = Booking.objects.filter(
                event=event, user=community_user
            ).exists()

    return render(
        request,
        "noticeboard/event_detail.html",
        {
            "event": event,
            "user_is_facilitator": user_is_facilitator,
            "user_has_booked": user_has_booked,
        },
    )


@login_required
@user_passes_test(is_facilitator)
def create_event(request):
    """
    Handle event creation by facilitators.
    """
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.facilitator = request.user
            event.slug = slugify(event.title)
            event.save()
            return redirect("facilitator_dashboard")
    else:
        form = EventForm()
    return render(request, "noticeboard/create_event.html", {"form": form})


@login_required
@user_passes_test(is_facilitator)
def edit_event(request, event_id):
    """
    Handle event editing by facilitators.
    """
    event = get_object_or_404(
        Event, id=event_id, facilitator=request.user
    )
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event.slug = slugify(event.title)
            form.save()
            return redirect("facilitator_dashboard")
    else:
        form = EventForm(instance=event)
    return render(
        request, "noticeboard/edit_event.html", {"form": form, "event": event}
    )


@login_required
@user_passes_test(is_facilitator)
def delete_event(request, event_id):
    """
    Handle event deletion by facilitators.
    """
    event = get_object_or_404(
        Event, id=event_id, facilitator=request.user
    )
    if request.method == "POST":
        event.delete()
        messages.success(request, "Event has been deleted.")
        return redirect("facilitator_dashboard")
    return render(request, "noticeboard/delete_event.html", {"event": event})


@login_required
def logout_view(request):
    """
    Handle user logout and confirmation.
    """
    if request.method == "POST":
        logout(request)
        return redirect("index")
    return render(request, "noticeboard/logout_confirm.html")


def handler404(request, exception):
    """
    Custom 404 error view.
    """
    return render(request, "errors/404.html", status=404)
