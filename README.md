<h1> Community Centre</h1> 


![multiscreen_view_BCC](https://github.com/user-attachments/assets/8f58f17a-b47c-44b1-b4e9-d3faa10eb97e)

Live link: (https://community-noticeboard-app-00b83bd93757.herokuapp.com/)

Link to Kanban Board:
[Viki-coding/Projects/Community Notice Board Project] 
(https://github.com/users/Viki-coding/projects/8/views/1)

## Table of Contents
- [Introduction](#introduction)
- [Description - Project Purpose](#description---project-purpose)
- [User Demographics - Target Audience](#user-demographics---target-audience)
- [UX](#ux)
- [User Stories](#user-stories)
- [Design Choices](#design-choices)
- [Typography](#typography)
- [Wireframes](#wireframes)
- [Flow Chart](#flow-chart)
- [Features](#features)
- [Interaction Points](#interaction-points)
- [Future Implementation Section](#future-implementation-section)
- [Accessibility](#accessibility)
- [Technologies Used](#technologies-used)
- [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
- [Testing](#testing)
- [Manual Testing](#manual-testing)
- [Quality Assurance](#quality-assurance)
- [Lighthouse Testing](#lighthouse-testing)
- [Bugs](#bugs)
- [User Experience Assurance](#user-experience-assurance)
- [Deployment Steps](#deployment-steps)
- [How to Fork](#how-to-fork)
- [How to Clone](#how-to-clone)
- [Heroku Deployment](#heroku-deployment)
- [Acknowledging Contributions & Credits](#acknowledging-contributions--credits)
- [Media/Images](#mediaimages)
- [Content](#content)
- [Legal & Ethical Compliance](#legal--ethical-compliance)


<h1> Introduction </h1>
This website aims to keep everyone in the community informed of events, matches, social gatherings, meetings and sporting opportunities available in their area.  Ballinameela Community Centre is a large sports hall, with a meeting room, kitchen, mezzineine and outdoor facilities of a large GAA/Soccer pitch and an all weather flood lit astro-turf pitch.  The community of Ballinameela based in West Waterford are a strongly knitted community who have worked very hard over the years fundraising and running events to create a community centre as the central point for families, individuals and sporting groups to have a meeting area to keep healthy, meet and gather in state of the art facilitiies.  To utilise the centre to its higest purpose it is important to highlight to the community themselves of what is going on on a weekly basis.  

<h2>Description - Project Purpose</h2>

The website will show the latest events that are taking part in the centre, by event name, time, date, location and description.  The purpose is to allow anyone in the community the ability to see what's on and feel welcome to join in taking part in that event.  

My husband and I moved to this community over 20 years ago, and at the time we had no idea what took place in the hall, sometimes it was highlighted in the local paper, sometimes on the local facbook page.  But unless you bought the local paper on a weekly basis, or if you are happy to scroll though facebook page on a regular basis it is difficut to pin point exactly what it happening and when. 

The users of the site will who want to check the time and location of an event can easily check it here. 
We increased the functionality of site by allowing community users to book events.  

This site caters for 2 types of users, community users and faciliators.  The community users are regular people in the community who would like to view events, book events and delete booked events. The facilitators are the people who actually create the event itself. They can create, read and view, edit or delete the event. 

We will have an number of facilitators who will be authorised to post events to the community notice board.  They may be coaches, community centre members, parent and toddler facilitator etc. 

Facilitators - can create a username and password. The django admin can then grant access to be part of the Facilitator Group within the django Group functionality.  The Facilitor Group set up in Django allows facilitators to be able to create, edit and delete events. Facilitators, when logged in can view their Dashboard, view the events they have created, edit events they have created and delete events they have created. The events are bookable.  The facilitator has to put the capacity of people allowed at the event and the date and time they should be booked by when creating an event. A facilitator can only view, create, edit and delete events. If they want to book events created by another facilitator they should have their own community user name and password. 

Community Users - can navigate to the site to view all events that are posted without being logged in.   A community user can create their own username and password, when they are logged in they can book a place on an event if it is within a time and date that has been stipulated and if there is still capacity, both of which are stipulated by the faciltiator.  When logged in, they can navigate to the dashboard to view the events they have booked and can delete the booking if rquired. 

<h2>User Demographics - Target audience</h2>
The project aims to accomplish keeping all members informed of what's going on, by having a central platform to higlight and encourage people to events.  That could be the time of the U10's hurling match v's Ballygunner that their grandparents would love to attend and watch, or a new mother in the area wondering if there is a local yoga group she could take part in.  The community centre was built using the dedication and money over many years from people within the community, this website will highlight everything that is taking place so the communtiy members themselves can enjoy it.

Decreases of women in sport, childhood obesity and lonliness are all major problems in our society today.  The community centre has faciliites such as basket ball, indoor soccer, after school children support, retirement film night, astroturf and flood lights, long jump, meeting rooms and a full size pitch.  If we can make it easy for people to view whats on in their local community they may make a postitive health or life decision that can help them get healthier, meet others, get support etc that is a very positive experience and result. This will benefit all members of the community. 

<h2>User Personas</h2>

The following is some user personas of indivduals in the community who are our target audience and who will utilise our site with great benefit:


1. Active Annie (Community User)
Demographics: 68 years old, retired teacher, lives alone, active in the community.

Tech Saviness: Comfortable using a computer and smartphone, uses Facebook, checks email daily.

Needs & Goals: Wants to stay active and social, looking for events to attend, easy access to information about local activities. She wants a simple, reliable way to find out what's happening at the Community Centre.

Frustrations: Dislikes scrolling through Facebook, finds it hard to find specific event information, misses events because she doesn't hear about them in time.

Website Use Case: Regularly checks the website to see what events are coming up, uses the search/filter functions to find activities that interest her (e.g., book clubs, exercise classes). Books events directly through the website.

Quote: "I just want a simple way to see what's going on. I don't want to miss another interesting talk or activity!"

2. Busy Brendan (Community User)

Demographics: 42 years old, works full-time, married with two school-aged children.

Tech Saviness: Very comfortable with technology, uses multiple devices daily, relies on online information.

Needs & Goals: Finds activities for his children, wants to participate in community events as a family, needs information that's quick and easy to access. He's looking for events that fit into his family's schedule.

Frustrations: Doesn't have a lot of free time, finds it difficult to find events that are suitable for his children, needs a quick overview of event details.

Website Use Case: Checks the website on his phone to see weekend events, looks for family-friendly activities, books events for his kids online, quickly checks times and locations.

Quote: "I need to know what's happening, when it's happening, and if my kids will enjoy it. I don't have time to waste."

3. Newcomer Nicole 
Demographics: 28 years old, recently moved to the community for work, single.

Tech Saviness: Highly tech-savvy, relies on online resources for everything.

Needs & Goals: Wants to meet new people and integrate into the community, looking for social events and activities, needs a welcoming and informative platform.

Frustrations: Doesn't know anyone in the area, feels isolated, unsure of where to find information about local events.

Website Use Case: Uses the website to discover social events and activities, signs up for email updates, explores different interest groups, relies on the website to feel more connected to the community.

Quote: "I'm new here and want to get involved. I hope this website can help me find my place in the community."


4. Facilitator Fiona (Event Faccilitator)

Demographics: 35 years old, runs a local parent-and-toddler group, volunteer.

Tech Saviness: Reasonably comfortable with technology, uses a computer for basic tasks.

Needs & Goals: Promote her parent-and-toddler group, easily create and manage event listings, reach a wide audience in the community, needs a user-friendly platform for event management.

Frustrations: Finds it time-consuming to promote her group through multiple channels, needs a central place to update event information, struggles with complicated website interfaces.

Website Use Case: Creates new event listings with detailed information (date, time, location, age group), updates existing listings, checks the number of bookings, interacts with community members through the website (if possible).

Quote: "I need a simple way to let people know about our group and manage our events without spending hours on it."

5. Community Committee Member (Event Facilitator)

Demographics: 55 years old, Community Centre Committee Member, manages various hall events.

Tech Saviness: Moderate tech skills, delegate if possible.

Needs & Goals: Effectively promote all events, delegate event creation, manage event schedules and bookings, needs a reliable platform for event organization.

Frustrations: Coordinating multiple facilitators, ensuring all events are properly promoted, keeping track of bookings and schedules, managing user accounts and permissions.

Website Use Case: Oversees all event listings, manages facilitator accounts, checks overall website traffic and engagement, ensures the website is up-to-date and informative.

Quote: "I need a system that allows me to keep an overview of all the activities in the community center and to easily delegate tasks."


<h2>UX</h2>
When you land on our site it is immeadiatley obvious what the site is and conveys the message of a notice board straight away.  There are 6 events posted per page, the most recents event posts are posted first, with navigation links to older events. 

Each event post shows enough detail to entice the user, if they are interested they can read more and book the event.  If they are not a user and would like to book an event they are easily navigated to the signup form.  Once they have a logded in, it is clear in the navigation bar, the log in button has changed to Log out and they can navigate to their personal dashboard to view and delete any events that they have booked. Prior to cancelling an event an alert modal confirms if they are sure they want to cancel the booking. They can naviage easily back to events to book or view another event as required. 

As a Facilitator once logged in you can navigate to the dashboard to create, view, edit or delete any events you have created. The event create form is clear and well labelled. Each field is required and the format of the field input is displayed in the label.

When the event is created, a nice clear edit and delete button is situtated under the event itself. 

Under each event is listed the names, emails and phone numbers of any community user who has booked their event.  The phone numbers and emails are active links which can be clicked on to create a call or email to the community user who has booked the event, allowing the faciltiator the ease to contact them about the event, for example if a child booked into an event got sick and the facilitator wanted to contact the parent. 

It is easy to edit and update any event. If the facilitator chooses to delele an event an alert modul is displayed to ensure they wish to continue to delete. 

When the facilitator is logged in the Log in changes to Log Out. 


<h2>USER STORIES</h2>
As a facilitator, I want to log in to the app so that I can manage my events.
As a Facilitator, I want to create a new event so that I can inform the community about upcoming activities.
As a Facilitator, I want to edit an existing event so that I can update the event details.
As a Facilitator, I want to delete an event so that I can remove outdated or canceled events from the notice board.
As a Facilitator, I want to view the community users who have booked 

As a Community Member, I want to view the notice board so that I can see the upcoming events.
As a Community Member, I want to search for events by category so that I can find events happening in specific category.
As a community user, I can view a paginated list of posts so that I can select which post I want to view.
As a community User, I can click on a post so that I can read the full event details.


<h2>Design Choices</h2>
Colour Scheme
Ballinameela Community Centre is based in the beautiful country side of West Waterford.  We wanted to use a nice green color to represent healthy country living.  As this was a comunity noticeboard to highlight the events of the area we used a bright yellow 'post-it color' to make it look like events were posted up aginst board.  We used a black text font to help stand out to all users especially those with accessible issues.  We used a contrasting cream color against the green which makes the scheme look solf, friendly while also accessible.  
Using a colour contrast checked we checked which font colours stood out best against our base colours.  All receiving good ratings. Graphic illustrated below:

![Color-contrast-good](https://github.com/user-attachments/assets/cbd1c72f-4e2e-42f8-b20c-94e6a307f087)

<h2>Typography</h2>
Font used is Roboto from Google Fonts. It is in the sans serif family, is clean and modern appearance.  It is dyslexic friendly helping with readability. 

<h2>Wireframes</h2>

![Wireframes1-BCC](https://github.com/user-attachments/assets/39b1ce9b-1024-4e79-97f0-4a219019833f)

![Wireframes2-BCC](https://github.com/user-attachments/assets/db6cf6aa-c986-410c-8981-f68ca2331ef5)

![Wireframes3-BCC](https://github.com/user-attachments/assets/a7c92c87-70cb-48bc-8c97-a32f14961c48)


<h2>ER Diagram</h2>

<img width="1037" alt="ERD Community Centre V3" src="https://github.com/user-attachments/assets/5660257a-5d2e-4f5d-bf3f-38c0cdc3cf44" />


<h3>FEATURES</h3>
Feature Title / Screenshot / Value to the User

Naviagtion Bar:
Login Feature
If you already have a username and password you can log in easily to view your events. Once logged in the button changes to Log Out. When you go to log out an alert modul asks if you are sure you want to log out. 

![Nav-bar with logout modul](https://github.com/user-attachments/assets/2ec3479e-569e-4dcc-ae35-ad9f83995dd9)

Sign Up Feature:
If you are a new user, it is easy to navigate to the Sign Up form, enter your details and password and are set up within minutes, the login button changes to Log Out and you have access to book events. 

![Nav Bar](https://github.com/user-attachments/assets/da4620e3-8fc8-48cc-9605-acbdc1a6cf25)

Dashboard Feature:
As a Community User the dashboard is personalised to the user and their booked events only.  If no events are booked it will display no events booked. If events are booked they are clearly diplayed in the dasboard, a user can view, or delete their events in the dashboard. Before a user deletes an event there is an alert modul asking them if they are sure. 

As a Facilitator the dashboard is personalised to your created events only.  Here the faciltiator can view, create, edit and delete their events.  They can also see the users signed up to each of their events. 


![My Events Facilitatator Dashboard](https://github.com/user-attachments/assets/d59824d4-bc0b-4b01-8bad-1e730608e1fb)


Notice Board Feature:
Community users can log on and immeaditlatey view the latest events in their area, keeping them up to date with events.  When an event such as an exercise class is advertised a community user may be motivated to attend due to its ease of access. This has the value to making our community a healhier community. 

![Noticeboard Feature](https://github.com/user-attachments/assets/35d45c40-419e-4f9c-acb2-67c63477b80d)

The user is fully informed, the date, time, location. The facilitator can expand more in the description, such as duration/cost of a class, what to bring. The value of fully informing the community to events with the flexibility of expanding the details in the Read more section. 

Search by Category Feature: 
Users who want to narrow down the search to certain events, such as a new parent in the area may want to only see events in the 'Parent & Toddler' section.  When a facilitator creates a new event, they have the opportunity of associating it with a certain category.  By clicking on the drop down arrow, a list of categories is displayed and when 1 is selected only events listed under those categories are displayed. 

![Sort-by-category](https://github.com/user-attachments/assets/4f4765a0-9bfe-4a71-b54e-718c3b12c5aa)

Booking Feature as a Community User
A community user can view all events and book their place to ensure they have a place at the class or event.  When an event is publised it is often only bookable with a phone number and within a certain timeframe which is not always convient for those making the booking, this feature allows users to book when ever a new event is posted in an easy to use booking method. They can share the site with friends and encouage them to book also. 

![Book Event](https://github.com/user-attachments/assets/b26de344-ce75-4c91-9e13-03eb34bd8e2f)


Booking Feature as a Facilitator 
The value of the booking feature as a faciltiator allows facilators to be able to put a capcity limit on an event to ensure the event is managable, such as a boot camp having a capacity of 40 to ensure their is enough exercise stations, a cookery course having a capacity limit of 10 to ensure their is enough equipment.  

The faciltitator also applies a booking by date/time, so an event cannot be booked after a certain time.  This allows the facilitator to be able to manage their event knowing the numbers of people intereted. For example a facilitator of a cookery course, the faciltiator would be able to see that 15 have booked by the booked by date/time and allow them to purchase 15 portions to prevent food waste. A bootcamp facilitator could see there are 40 signed up and understant the amount of exercise stations required. 

The booking feature also has the value added of showing the community users have booked their event. This allows faciliators to see the number of people who have booked their event, with their names, active email and an active phone number. Users can be easilty contacted if required. 

![Dashboard with list of users booked](https://github.com/user-attachments/assets/b29feb77-32bd-44bf-9e71-93d7683e5c57)

FOOTER FEATURES:

![Footer Features](https://github.com/user-attachments/assets/a03fb0fa-dd92-463e-83e8-deb04b3407d2)

Footer Features:
The Eircode of centre is already linked to google maps the user can easilty navigate to the centre by clicking on the eircode, which opens in a new page. 

Facebook and Instagram Features:
This allows the user to access the Ballinameela Community Centre socials in a new page. 

Pagination Feature:
The latest events are posted first, to view older posted events the user can user the pagination links at the bottom of the page to easilty naviage though the pages. 


<h2>Interaction Points</h2>

<h2>Future Implementation Section</h2>
I spoke with some of my non techie frieds about the site, who are involved in our community and are coaches of various teams and they got very excited about the potential of the site. They were suggesting a Games and Fixtures and Results page, so show all our local GAA matches, Home and Away of the juvenile club, ladies and seniors so that locals could review what matches are on and where to check the results. 

Expiry Date, after a certain period to remove 'old' event posts from the site, so for example if there was a bootcamp on for 6 weeks it would stay up for the 6 weeks but would be removed after to keep the site clean and up to date. 


<h2>Accessibility</h2>
This is a community website for everyone in the community to use.  Accessibility of the site is very important. 
(a) Semantic HTML elements were used to provide meaningful structure to the content.
(b) Keyboard Navigation ensures alll interactive elements like the form fields and buttons are accessible via the keyboard. 
(c) Using Text Alternatives using Aria labels to describe content were used to improve accessibility for screen readers.  
(d) Color Contrast: The color pallet chosen has sufficent constrast against the background to be readable by users with visual impairments.  
(e) All forms were accessible with associated lables to provide clear instruction and are navigable using keyboard. 
(d) Alt attributes were used to describe any image content such as the logo and notice board image. 
(e) Testing, we used WAVE a Web Accessible Evaluation Tool to ananlyse the page and made adjustments to the site to try to improve it. It passed the Wave Evaluation without errors. 


![WAVE evaluation results](https://github.com/user-attachments/assets/1b635a48-a1fb-451e-8757-64eda867a761)

Lighthouse Testing 

![Lighthouse test results](https://github.com/user-attachments/assets/53a061ea-edb5-4d32-b60e-a9ab34756838)


<h2>Technologies Used</h2>
HTML -  CSS -  JS - Python - Django - Bootstrap 


<h2>Frameworks, Libraries and Programs Used: </h2>

* Balsamiq Wireframes - used to create wireframes
* Git - version control
* Visual Studio Code 
* Git Hub - To save and store the files for the website
* Google Fonts - to import fonts onto the website
* Font Awesome for iconography on website
* Favicon.io - to create favicon
* Coolors - checking colour pallets and their contrast abilities with fonts.
* Berme.net - to reduce image sizes and convert to .webp
* Canva - to create logo image
* Am I Responsive - quick tool to check how responsiveness on various devices and creates display
* Responsive tool - (https://responsivetesttool.com/)
* Screen Shot of site on various screens (https://techsini.com/multi-mockup/)
* JSHint to check JS code
* Spell Check
* Heroku
* Django 
* Pylint 


<h2>User Experience Assurance</h2>
<h2>Deployment Steps</h2>

* The site is Deployed using GitHub Pages
* Login to GitHub
* Go to the projects repository (https://github.com/Viki-coding/community)
* Click on Settings
* Select pages in the left navigation bar
* From SOURCE dropdown select Deploy from a Branch
* Under BRANCH from dropdown select Main Branch and SAVE
* The site is now deployed but may take a few minutes to go live.
* Return to CODE tab of Github repo and wait a few minutes for build to finish, refresh page. This will show on GitHub-pages to see active deployments.

<h2>How to Fork</h2>

* Login to Github
* Go to Project repository
* Click the FORK button top right corner

<h2>How to Clone</h2>

* Log into Github
* Go to project repository
* Click on the code button, select what want to clone HTTPS, SSH or GitHub CLI and copy the link.
* Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory
* Copy 'git clone' into the terminal and paste the link you copied in step 3. Press enter.

Heruko Deployment

Log on to Heruko
https://dashboard.heroku.com/apps
 
Select “Create new app”
Name the app something unique
Choose Europe from the dropdown
Click ‘Create App’
Go to the SETTINGS  tab first
In the ‘Config Vars’ section aka environment variables 
In the KEY section type in PORT and the value section type in 8000 – add

IF you build a landmark project that doesn’t use a cred.json file you don’t need to set up config vars otherwise: 
In the KEY section type CREDS (all capital letters) – 
Go to workspace and copy the entire creds.json file and paste it into the value field and add.

 To add other dependencies:
ADD BUILDPACK
Select Python – choose add
Select Node.js – choose add 
(Should be in this order, python first then node.js)
 
DEPLOY SECTION
Click on the DEPLOY Tab
Choose the Githb deployment method
Confirm that you want to connect to GitHub, gitbub will request your password to connect. 
Click in repo name  and Search for your repository name and select connect. 
Select Enable Automatic Deploys 
Check Choose a branch to deploy is defaulted is MAIN
Click on Display Branch 
 
App will build
Wait until the message ‘App was successfully deployed’ is displayed, click on the view button


<h2>Acknowledging Contributions & Credits</h2>
TITLE OR DESCRIPTION
SOURCE OF LINK
CONTEXT
[Django Tutorial #24 - Requiring Login - Net Ninja @6.15](https://www.youtube.com/watch?v=fqDTZA5P1EE)
Improving the look of my hero image and using css and flex
(https://cloudinary.com/guides/front-end-development)

Creating view to handle djangos login form: ([Django Documentatin](https://docs.djangoproject.com/en/5.1/topics/auth/default/#:~:text=groups.%20set%28%5Bgroup_list%5D%29))

![Slugify](https://www.w3schools.com/django/ref_filters_slugify.php) to help fix IntegrityError with a duplicate key value for the slug field. 
![blogizem - How to Fix UNIQUE Constraint Error in Django Model for Slug Field?] (https://www.youtube.com/watch?v=D0K51GneU3g)

[Facilitator Logout View](https://stackoverflow.com/questions/15467831/django-logout-redirects-me-to-administration-page#:~:text=If%20you%20are%20seeing%20the,admin%20comes%20after%20your_application%20.)
Helped to fix when a facilitator logs out, rather than seeing the django admin panel log out I wanted the facilitator to see the customised page. 

[Expand button on hover for Delete](https://www.shecodes.io/athena/3020-how-to-use-hover-to-expand-a-button-in-css)

My notice board excerpts were various lenths and then that was having an affect on my styling and pushing the text out of my notice board display cards.  I had to come up with a way of reducing down the amount of text in my excerpt. This website showed me some good filter techniques available. I used the slice method. (https://earthly.dev/blog/django-template-filters/)

To help prevent overflow of the text I also made some changes to my css to prevent it.  Found this video really helpful to explain the concepts of overflow/text wrapping. (https://www.youtube.com/watch?v=6m3ZmlgfZlA)

When facilitator was logged it, they could view, edit and delete their own event, but when they left their dashboard and clicked on an event they did create, it was just showing the event without allowing them to edit. to fix this I amended by event_detail.html page to include {% if is_facilitator%} and included the hrefs to edit and delete. I also had to change the event_detail view to include is_facilitator. 

I wanted to creat a select events by category function, so for example if you just wanted to see what gaa matches were on you would select GAA. I found this video helpful to explain the query ge GET parameters using djangos filter. [Django QueryDict | GET parameters | django-filter] (https://www.youtube.com/watch?v=nBrkUxa5X0E)

[W3 Schools] (https://www.w3schools.com/django/django_queryset_get.php)
[W3 Schools onchange Event] (https://www.w3schools.com/jsref/event_onchange.asp)  Submitting the form automatically submits the forms with the new attribute. 

[Fetch Data from a Database and output to a webpage] - Django ()

(https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html)


Bootstrap is fanatasic and frustrating at the same time, I found this aritcle on stackoverflow good. How can I override Bootstrap CSS styles. (https://stackoverflow.com/questions/20721248/how-can-i-override-bootstrap-css-styles)

Bug: Time no longer displaying on event. I had made some changes to the time imput fields as I wanted the facilitator to be understand to put in the 24hr clock.  When I amended my model to facilitate the bookings functionality I unfortunetly made the error of changing the names of my start_time to starttime and end_time to endtime, I changed it in some files and not in others, so I had to make sure the forms.py file was the same as my model.  

Dates & Times in Python
Understanding date and time to work with my bookings I found this video helpful. 
[Learn Python DATES & TIMES in 6 minutes! - Bro Code](https://www.youtube.com/watch?v=DwBDHsdX6XQ)

Django does not allow exists method in the template, I was trying to have the facilitator and user dashboard to appear in the navigation bar depending on who was logged in. When I did this it created a templateSyntaxError. To solve it I used a custom template filter and restarted my server. 
(https://stackoverflow.com/questions/40686201/django-1-10-1-my-templatetag-is-not-a-registered-tag-library-must-be-one-of)

Bug: Logged in as a community user. Booked an event. Went to Dashboard, but no booked events displayed. 
Resolved by looking at code and realising I had for booking in booking rather than booking in bookings to match what I had in my views. 

[Pagination For Django - Django Wednesdays #18 - Codeemy.com] (https://www.youtube.com/watch?v=N-PB-HMFmdo) Good video about creating pagination. 

[PEP 8 - Style Guide for Python Code] (https://peps.python.org/pep-0008/)

<b>General good videos and links to teaching of Python:<b>


I signed up to a phone app called MIMO which I found great for teaching me python and to help me do something productive rather than doom scrolling when I'm in the car waiting on my kids or having breakfast in the morning. Would highly recommend. 

Lucimeri Andretta - PP4 - MVP & Community Walkthrough.pdf was great or refer to for the entire projects including common errors, testing, readme. 

[Code Validation with Joanna Gorska](https://www.youtube.com/watch?v=6j9dZTW4owI&list=PL_7334VduOHvzZYlgy_0kZLcic2NINCUt&index=37)

<b>Videos & Websites that we gained visual clues of how to create the community centre website:</b>

Modifying forms and using widgets. This guy had some great videos about Django, he was really good at explaing concepts.
[Try DJANGO Tutorial - 26 - Form Widgets] (https://www.youtube.com/watch?v=-oWIyFYyNQw) I wanted to change myt date format to dd/mm/yy rather than the american format of yyyy/mm/dd. 
Also Dajngo documentation helped out again: (https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-DATE_INPUT_FORMATS)

To prevent users from booking events that were past the date we got inspiration for the code from (https://stackoverflow.com/questions/70671189/avoid-booking-past-dates-with-django)

We gained inspiration with the READ.me by watching the video 'Creating your first README with Kera Cudmore' on CI Chanel Lead Library on YouTube and also the video with Lane-Sawyer Thompson on CI Channel on YouTube. Thanks to the on-line tutor, Oisin and Rebecca for their expertise and ability to explain some of the 'challenges' I encountered. Thanks to our very supportive and positive facilitator Kay and my Kiwi mentor Dick Vlaanderen. Also found the webinar 'Community Q&A: How to Troubleshoot with Lane-Sawyer Thompson' very helpful approach to how to view looking at the site for bugs and methodically identifying issues.

[CSS TRICKS - A Grid of Squares] (https://www.youtube.com/watch?v=8bhKjoowr4c&t=12s) Which helped me to fix my events grid to make it look better. 

In my events detail page, once a user had booked an event, I didn't want the Book Event to display again when they went to view their booking. So I used the if no user_is_facilitator to check if the event had already been booked. These websites were helpful to explain the concept. (https://www.w3schools.com/python/gloss_python_check_if_dictionary_item_exists.asp)
(https://www.geeksforgeeks.org/python-if-with-not-operator/)

Bug: Bootstrap color over-riding the cream color I wanted in my nav bar. To fix it I first put !important beside it which failed to work, advice from stack overlflow was 'specificity', adding another class to the rule.  This worked. (https://stackoverflow.com/questions/46736264/overriding-bootstrap-default-important-color-codes)

<h2>Media/Images</h2>
Images of logo and notice board both created in Canva by myself using canva template. No other imagery used. 

<h2>CONTENT</h2>
The content text for website  is ficticous and is written by Viki Mulhall. 

<h2>Legal & Ethical Compliance</h2>
This project is for educational purposes only.



