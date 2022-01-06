# XtremeTech-Assignment


## Django Server for Email Automation

Basic django project which accepts email, receiver's name and city and sends an email to the respective person.
send_mail() method present in django.core.mail module is used to send the email.


## Steps to run the project:
	
**Requirements:** Python and pip must be installed in your system.

### 1) Clone the project onto your local machine.

	git clone https://github.com/shivendushukre/XtremeTech-Assignment.git

### 2) Create a virtual environment and install the required packages.


create a virtual envirnoment:

	virtualvenv venv

activate this virtual envirnoment:

	venv\Scripts\activate

installing all required packages which are present in requirement.txt:

	pip install -r requirements.txt

### 3) Start the development server:

	python manage.py runserver

### To set the sender's email address and password, open email_automation/settings.py.
	At line no. 132 add email address
	At line no. 133 add the password



