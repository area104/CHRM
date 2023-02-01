from django.urls import path
from ClientApp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about,name="about-page"),
    path('form/',views.form,name="form-page"),
    path('edit/<person_id>',views.edit,name="edit-page"),
    path('delete/<person_id>',views.delete,name="delete-page"),
    path('profile/',views.profile,name="profile-page"),
    path('register/',views.register),
    path('show_user/',views.show_user),
    path('show_cust/',views.show_cust,name="show_cust-page"),
    path('regis_cust/',views.regis_cust),
    path('edit_cust/<tel>',views.edit_cust,name='edit_cust-page'),



]