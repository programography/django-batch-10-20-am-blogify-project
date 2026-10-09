from django.urls import path
from blog import views

urlpatterns = [
   path("", views.home, name = "home"),
   path("about", views.aboutus, name = "about"),
   path("contact", views.contactuss, name = "contact"),
   path("services", views.services, name = "services"),
   path("privacy-policy", views.privacy_policy, name = "privacy_policy"),
   path("contact-data", views.contactdatasace, name = "contactus"),
   path("sucess-message", views.success_message, name = "sucess_page"),
   path("delete-my-card/<int:x>", views.deletecard, name = "deetecard"),
   path("contact-update/<int:xyz>", views.contact_for_update, name = "contact_for_update"),
   path("update-contact-data/<int:myid>", views.updatecntect, name = "updateconatct"),
   
   
   path("sign-up", views.signuphere, name = "signup"),
   path("login", views.loginhere, name = "login"),
   path("logout", views.logouthere, name = "logout"),
]