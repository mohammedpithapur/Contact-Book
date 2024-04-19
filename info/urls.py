from django.contrib import admin
from django.urls import path
from .views import list,add_contact,contact_detail,delete

urlpatterns = [
    path('', list, name="list"),
    path('add_contact', add_contact, name="add_contact"),
    path('contact_detail/<int:contact_id>/', contact_detail , name="contact_detail"),
    path('edit_contact/<int:contact_id>/', add_contact, name='edit_contact'),
    path('delete_contact/<int:contact_id>/', delete, name='delete_contact')
]