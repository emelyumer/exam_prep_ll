from django.urls import path

from exam_prep_ll.profiles.views import create_profile, ProfileDetails, ProfileEdit, ProfileDelete

urlpatterns = (
    path("create/", create_profile, name='create_profile'),
    path('details/', ProfileDetails.as_view(), name='details_profile'),
    path('edit/', ProfileEdit.as_view(), name='edit_profile'),
    path('delete/', ProfileDelete.as_view(), name='delete_profile'),

)