<h1> TESTING DOCUMENTATION - COMMUNITY CENTRE APP</h1> 

<h2> Responsiveness Testing</h2>
<h2> Browser Compatability Testing</h2>
<h2> Bugs Resolved & Unresolved</h2>
<h2> Lighthouse Testing Outcome</h2>
<h2> Code Validation</h2>
<h2> User Story Testing</h2>
<h2> Features Testing</h2>
<h2> Responsiveness Testing</h2>


<h2> Browser Compatability Testing</h2>
<h2> Bugs Resolved & Unresolved</h2>
<h2> Lighthouse Testing Outcome</h2>
<h2> Code Validation</h2>
<h2> User Story Testing</h2>
<h2> Features Testing</h2>

  
<h2>Manual Testing</h2>
(Does the site work as intended?)
FEATURES TESTING
LIGHTHOUSE PERFORMANCE
VALIDATOR TESTING
BROWSER COMPATIBILITY
SCREEN SIZE RESPONSIVENESS
BUGS RESOLVED AND NOTE SOLUTIONS AND UNRESOLVED

https://wave.webaim.org/
	
We performed manual testing on the deployed site and also ran our html, css and js codes through validators.
<h3>W3C Validator</h3>
<h3> CSS (Jigsaw) validator</h3>
<h2>JavaScript Code Validator</h2>
<h2> JSON formatter and Validator</h2>
<h2>(https://pep8ci.herokuapp.com/)</h2>

<h2>Quality Assurance</h2>
 (Steps taken to manually test the project
-	Ensures it functions correctly
-	Identifies potential bugs
User Experience Assurance
-	Ensures that the end-users have a smooth experience by addressing potential issues. 
We took a systematic and structural approach to manually test each page to ensure it functions correctly and to help identify potential bugs. We created a specific testing template to ensure and re-check all aspects of the quiz were working correctly as specified with expected and actual outcomes using a methodical approach. We did final testing on the deployed site. 

<h3>Test Evaluation Sheet:</h3>
As shown in the evaluation sheet below we navigated around our site and tested all available features to ensure they were working as intended.

<h2>Lighthouse Testing</h2>
<h2>BUGS</h2>
<u>Solved Bugs</u>
I came across many bugs while testing the quiz, from missing semi-colons to the reset button not being contained within the centre of the quiz box due to styling errors that were fixed and rectified. I put the HTML and CSS code through W3CValidator and fixed all warnings that were shown.  Having chrome development tool open while creating code and inspect console log was very helping with some aspects of the bug finding.  It was also helpful breaking down the problem and  thinking logically - what’s working, what’s not to be able to focus in on the issue. 

One challenging bug was
After following the step by step guide to migrating from gitpod to visual studio code, I found it difficult, lost my project kanban board, so I decided to start again rather than make the migration. Deploying to heroku also took 1 full day to sort of, with many errors and google, stack overflow and slack to assist.  It was very frustrating at the time, loosing valuable coding hours trying to fix errors but each is a learning curve where you learn something new and get braver at writing commands to see if things get fixed.  In the end I had to resort to Oisin in student support who finally got me sorted! 

I followed the steps to install summernote. After running my server and apending /admin at the end I found it had not updated. I checked again to see if summernote was installed. I checked to see if it was in my installed apps. I checked to see it was in my projects urls.py file. I then checked the EventAdmin class was registered in my admin.py file. All was ok. I made migrations again and still did not make any changes. Then I right clicked to inspect and checked the console for javascript errors and found errors for the static files. Then I googled how to resolve this error and followed the steps which got it resolved. 

I applied styling to the page, but when I ran the server it was not applying the changes. I corrected by static files in settings.py as I had inserted staticfile_dirs twice. I checked my file paths, my style.css sheet was not in its own css folder under static so I ameneded it. I ran the python manage.py collect static command again and ran the server. Still didn't work. Then I saw it, in my file directory - I had style.css rather than styles.css

Made a lot of styling changes to the page, deployed to Heroku and the following was displayed.  Realised I had forgotten to collectstatic, went back into the terminal ran the command again and deployed successfully. 

Faciliator log in bug, faciliator user not being redirected when username and password entered. When running server, got error module error not found in forms. Realised I had created the forms.py in the incorrect file path under community centre rather than under noticeboard app. Deleted forms.py under community centre. Bug still existed, so decided to create a separate login.html page for facilitators to log in to, corrected the views.py links. Checked that the users set up in Django were authorised as faciliators, created a new user called facilitator, ensured they had full permissions and facilitator status. Still unable to log on.  With tutor support, checked login_view function to realise  that after authentication is successful I should of re-directed them to create_event. After half a day of pulling my hair out - finally worked, good lesson learnt check django documentation for tips! 

javascript error - while dev tools was open noticed I had a js error, checked the filepath in base.html to realise that I should of had script.js in its own js folder. Corrected it and it ran fine. 

Facilitator Dashboard not displaying when facilitator logs in. 
Focused in on the logical step that my view.py for dashboard was incorrect, yellow error page higlighted the error, changed user to facilitator and error was resolved. 

Integrity Error 
After I log in as a facilitator, it takes me to my dashboard, I choose to create an event, I enter the field details and when I click on submit I get Integrity Error. ![geeksforgeeks](https://www.geeksforgeeks.org/integrityerror-in-django/) suggestted 3 common reasons, 1. FK Violation, 2. Unique Constraint Violation and 3. Non-Null Field Violation. My yellow error message highlighted [null value in column "facilitator_id" of relation "noticeboard_event" violates not-null,constraint]. I realised that this was consistent with the above error and changed user to facilitator as that was a valid value in my model. I changed the edit and delete views to faciliator to ensure the error didn't happen again. 

IntegrityError - duplicate key value violates unique constaint (https://www.youtube.com/watch?v=D0K51GneU3g)

Log Out as Facilitator Error
I added the feature that once the facilitator was logged in, the button would change to log out. But when I clicked on log out it would bring me to the django admin log out panel rather than my own customised one. 
Stack Overflow, credid/link below in credits. helped me anmend the customised django view and urls.py to my home page. 

Facilitator Bookings Table 
I created a tabel on the facilitator dashboard so that the names, emails and phone numbers of the people who were booked were clearly displayed.  On smaller screens the table half disappeared horizonally. I made many changes but stackoverflow advice helped to display it most clearly. (https://stackoverflow.com/questions/4237110/how-can-i-make-a-css-table-fit-the-screen-width)
