from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    statuses = [("D","Draft"),("P","Published")]

    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.CharField(max_length=1,choices=statuses,default="D")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Create your models here.


# Blog: 
#     - Image 
#     - Title 
#     - Content 
#     - Author
#     - Published Date 


# 1. Activate the virtual env  djangoenv\Scripts\activate
# 2. django-admin startproject cms 
# 3. >>cms python manage.py startapp blog 
# 4. settings.py => installed_apps add ['blog',] 
# 5. models.py define the models
# 6. python manage.py makemigrations => Migration file 
# 7. python manage.py migrate 
# 8. runserver => python manage.py runserver 127.0.0.1:8000/admin
# 9. python manage.py createsuperuser
# 10.admin.py admin.site.register(Post) 
# 
#Category
#   id   
    # name 
    # description

# Blog 
#   title
#   content
#   status 
#     category => 2 => programming 

# 1 blog 1 category 
# 1 category many blog   1 to many 