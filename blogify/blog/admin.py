from django.contrib import admin
from blog.models import contactus
# Register your models here.

admin.site.register(contactus)


# python manage.py makemigrations
    # ---> help to create migrations from our model 
    
    
# python manage.py migrate
        # --> to apply migrations on database