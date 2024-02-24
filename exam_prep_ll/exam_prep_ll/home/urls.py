from django.urls import path

from exam_prep_ll.home.views import index, dashboard

urlpatterns = (
    path("", index, name='index'),
    path("dashboard/", dashboard, name='dashboard')

)