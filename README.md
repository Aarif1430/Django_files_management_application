# Description
Implement a web application that allows users to store, at later retrieve, files at a specified URL. The application should be composed of two distinct components - frontend JavaScript application, and a backend API.

# Requirements
- Stores files of any type and name — Implemented
- Stores files at any URL — Partially Implemented
- Does not allow interaction by non-authenticated users — Implemented
- Does not allow a user to access files submitted by another user — Implemented
- Allows users to store multiple revisions of the same file at  the same URL — Implemented
- Allows users to fetch any revision of any file — Implemented

# Building Solution
The build contains requirements.txt file consisting of all the necessary python packages used for this application.

- **Installing dependencies**: *python install -r requirements.txt*
 - **Migration steps**: *python manage.py makemigrations, python manage.py migrate, python manage.py migrate —run-syncdb*
- **Running Server**: *python manage.py runserver*
Note: Please note incase you’re facing any permission issue for writing to directory in Macos operating system, Run above command with sudo prefix

# Home Page
The below screen is the home page of the application. It has got two controls:
- Login - Where existed user can login with his own credentials.
- Sign Up - Where user can register by providing necessary inputs.
![Login Page](https://github.com/Aarif1430/Django-file-storage-application/blob/master/media/login.png)

# SignUp Page
The signup page is shown below
![SignUp Page](https://github.com/Aarif1430/Django-file-storage-application/blob/master/media/sign_up.png)

# Successfull Login
After logged in successfully, The following page is show to user
![Home Page](https://github.com/Aarif1430/Django-file-storage-application/blob/master/media/home.png)

As you can see in above screen, The Upload Document text appears after user is authenticated.

# Upload Document
After clicking Upload Document, The following screen appears. The screen shows all the documents uploaded by TestUser1. This page gives a freedom to download or delete any specific document, path were documents are stored is also shown to user.
![File Upload Page](https://github.com/Aarif1430/Django-file-storage-application/blob/master/media/file_upload1.png)
![File Upload Page](https://github.com/Aarif1430/Django-file-storage-application/blob/master/media/file_upload2.png)

# Django REST Framework
Below screenshot shows the get query sent using Django REST Framework
![Django REST Framework](https://github.com/Aarif1430/Django-file-storage-application/blob/master/media/postman.png)

# Password Reset
Below screenshot shows the password reset functionality added to the application. The application is configured for gmail two way factor authentication and needs to be configured in settings.py, The functionality is not working as expected and sending email fails sometimes.
![Django REST Framework](https://github.com/Aarif1430/Django-file-storage-application/blob/master/media/forgot_password.png)
![Django REST Framework](https://github.com/Aarif1430/Django-file-storage-application/blob/master/media/email_reset.png)

# Testing and Code Coverage
Run below commands to generate code coverage in html format. The test cases are written using pthon pytest module.
-  **pytest --cov=. --cov-report=html 	chromium htmlcov/index.html**

The below screenshot shows the reports generated using above command, The code looks into tests folder inside core application and evaluates matrix for code coverage. As you can see in below screenshot for every file a corresponding html file is generated  

![Code Coverage](https://github.com/Aarif1430/Django-file-storage-application/blob/master/media/code_coverage.png)


