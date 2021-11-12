
# Student Management System
  Rest Apis Using DRF framework to manage students and their marks in each term examinations.
  # Code
    views.py and serializers.py contain api handling functions
    # Models
    models.py contains Teacher, Student, Marks Models
  # Requirements
    requirement.txt file conatins all requirements to run this project
    use:
      pip install -r requirement.txt
   # To generate new migrations:
       ./manage.py makemigrations portal_user
       ./manage.py migrate
   # To start project:
       ./manage.py createsuperuser
       ./manage.py runserver

   # To use Db Dump:
        ./manage.py loaddata data_dump.json
            admin user: ananthu
            admin password : 17fingent

   # Sample Response and Urls:
        response.txt file in root holder contains sample response and information about urls.

   # CSV Upload
        students.csv in root holder contains students records.

   # To upload CSV to database:
     ./manage.py csv_upload < path to the csv file >
