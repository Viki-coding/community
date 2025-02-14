<h1> Community Centre</h1> 


Live link: https://community-noticeboard-app-00b83bd93757.herokuapp.com/


<h1> INTRODUCTION </h1>
This website aims to keep everyone in the community informed of events, matches, social gatherings, meetings and sporting opportunities available in their area.  The community of Ballinameela based in West Waterford are a strongly knitted community who have worked very hard over the years fundraising and running events to create a community centre as the central point for families, individuals and sporting groups to have a meeting area to keep healthy, meet and gather in state of the art facilitiies.  To utilise the centre to its higest purpose it is important to highlight to the community themselves of what is going on on a weekly basis.  

<h2>Description - Project Purpose</h2>
The website will show the latest events that are taking part in the centre, by event name, time, date, location and description.  The purpose is to allow anyone in the community the ability to look up the site to see what's on and feel welcome to join in taking part in that event.  The users of the site will be all age demographics living in the community who may want to check the time and location of a match, to a new parent to the area wondering if there is a parent and toddler group. 

We will have an number of facilitators who will be authorised to post events to the community notice board.  They may be coaches, community centre members, parent and toddler facilitator etc. 

Please see attached some user personas. 

	
-	The project aims to accomplish keeping all members informed of what's going on, by having a central platform to higlight and encourage people to events.  That could be the time of the U10's hurling match v's Ballygunner that their grandparents would love to attend and watch, or a new mother in the area wondering if there is a local yoga group she could take part in.  The community centre was built using the dedication and money over many years from people within the community, this website will highlight everything that is taking place so the communtiy members themselves can enjoy it.

Decreases of women in sport, childhood obesity and lonliness are all major problems in our society today.  The community centre has faciliites such as basket ball, indoor soccer, after school children support, retirement film night, astroturf and flood lights, long jump, meeting rooms and a full size pitch.  If we can make it easy for people to view whats on in their local community they may make a postitive health or life decision that can help them get healthier, meet others, get support etc that is a very positive experience and result. This will benefit all members of the community. 



<h2>User Demographics - Target audience</h2>

<h2>UX</h2>

<h2>USER STORIES</h2>
As a facilitator, I want to log in to the app so that I can manage my events.
As a Facilitator, I want to create a new event so that I can inform the community about upcoming activities.
As a Facilitator, I want to edit an existing event so that I can update the event details.
As a Facilitator, I want to delete an event so that I can remove outdated or canceled events from the notice board.
As a Community Member, I want to view the notice board so that I can see the upcoming events.
As a Community Member, I want to search for events by category so that I can find events happening in specific category.
As a community user, I can view a paginated list of posts so that I can select which post I want to view.
As a community User, I can click on a post so that I can read the full event details.
As a facilitator I can create a login in with approval from the super user.

<h2>Design Choices</h2>
Colour Scheme
Using a colour contrast checked we checked which font colours stood out best against our base colours.  All receiving good ratings. Graphic illustrated below:

<h2>Typography</h2>

<h2>Wireframes</h2>
<h2>Flow Chart</h2>

<h3>FEATURES</h3>
	(example: nav bars, footer, contact forms, social media icons. )
	Functional Overview 
-	Core functionalities
-	Elements of the project
-	Sets expectations
Navigation and Interaction Points 
-	Offers preview of key elements which are crucial for user interaction.
Assessor wants to see:
Feature Title / Screenshot / Value to the User
<h2>Interaction Points</h2>

<h2>Future Implementation Section</h2>

<h2>Accessibility</h2>

<h2>Technologies Used</h2>
HTML -  CSS -  JS


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
* Responsive tool - https://responsivetesttool.com/
* JSHint to check JS code
* Spell Check
* Heroku
* Django 

  
<h2>Manual Testing</h2>
(Does the site work as intended?)
FEATURES TESING
LIGHTHOUSE PERFORMANCE
VALIDATOR TESTING
BROWSER COMPATIBILITY
SCREEN SIZE RESPONSIVENESS
BUGS RESOLVED AND NOTE SOLUTIONS AND UNRESOLVED
	
We performed manual testing on the deployed site and also ran our html, css and js codes through validators.
<h3>W3C Validator</h3>
<h3> CSS (Jigsaw) validator</h3>
<h2>JavaScript Code Validator</h2>
<h2> JSON formatter and Validator</h2>

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



<h2>User Experience Assurance</h2>
<h2>Deployment Steps</h2>

* The site is Deployed using GitHub Pages
* Login to GitHub
* Go to the projects repository (https://viki-coding.github.io/Guess-the-Flag-Quiz/)
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
https://cloudinary.com/guides/front-end-development

Creating view to handle djangos login form: ([Django Documentatin](https://docs.djangoproject.com/en/5.1/topics/auth/default/#:~:text=groups.%20set%28%5Bgroup_list%5D%29))

![Slugify](https://www.w3schools.com/django/ref_filters_slugify.php) to help fix IntegrityError with a duplicate key value for the slug field. 
![blogizem - How to Fix UNIQUE Constraint Error in Django Model for Slug Field?] (https://www.youtube.com/watch?v=D0K51GneU3g)

<b>General good videos and links to teaching of Python:<b>
I signed up to a phone app called MIMO which I found great for teaching me python and to help me do something productive rather than doom scrolling when I'm in the car waiting on my kids or having breakfast in the morning. Would highly recommend. 

Lucimeri Andretta - PP4 - MVP & Community Walkthrough.pdf was great or refer to for the entire projects including common errors, testing, readme. 

<b>Videos & Websites that we gained visual clues of how to create the community centre website:</b>


We gained inspiration with the READ.me by watching the video 'Creating your first README with Kera Cudmore' on CI Chanel Lead Library on YouTube and also the video with Lane-Sawyer Thompson on CI Channel on YouTube. Thanks to the on-line tutor, Oisin and Rebecca for their expertise and ability to explain some of the 'challenges' I encountered. Thanks to our very supportive and positive facilitator Kay and my Kiwi mentor Dick Vlaanderen. Also found the webinar 'Community Q&A: How to Troubleshoot with Lane-Sawyer Thompson' very helpful approach to how to view looking at the site for bugs and methodically identifying issues.

<h2>Media/Images</h2>
Image by of Green Globes in background by Clicker-Free-Vector-Images from Pixabay
Flag images from Britannica website. 
Image of logo created in Canva using canva template. 

<h2>CONTENT</h2>
The content text for website  is written by Viki Mulhall. 

<h2>Legal & Ethical Compliance</h2>
This project is for educational purposes only.



