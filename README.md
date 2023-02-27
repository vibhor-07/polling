Project:
Making a simple polling web-application, where we can add question with choices from admin side.
Other users can open the given url to read the the question and vote for there desired choice.

Setup the project on local system:
1) Install python-3
    i) sudo apt-get update
   ii) sudo apt-get install python3
  iii) sudo apt install python3-pip
2) Create a virtual environment and activate it.
    i) pip install virtualenv
   ii) virtualenv venv
  iii) venv\Scripts\activate (this is used to activate the virtual environment)
3) Install django.
    i) pip install django
4) Start the django project.
    i) django-admin startproject
5) Create the required apps.
    i) django-admin startapp (appname)
6) Register the apps in setting.py file.
7) Apply migrations and run the project.
    i) python manage.py makemigrations
   ii) python manage.py migrate
  iii) python manage.py runserver

Create a Docker image:
1) Write a dockerfile for the above setup.
2) Create and push the image on dockerhub

Deployment:
1) Create the required infrastructure using IAC(Terraform) code.
    i) Create VPC.
   ii) Create AutoScaling Group
  iii) Create an instance to install Jenkins for CI/CD pipeline.
   iv) Create an EKS cluster.
2) Deploy the application on the EKS cluster.
    i) Create a Deployment using the declarative method (yml file).
   ii) Create a Service using the declarative method (yml file).
3) Routing
    i) Generate Elastic IP and attach it to the cluster.
   ii) Make the cluster available on the required URL using Route53.