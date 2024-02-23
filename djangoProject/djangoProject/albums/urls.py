from django.urls import path

from djangoProject.albums.views import CreateAlbumView, DetailAlbumView, EditAlbumView, DeleteAlbumView

urlpatterns = (
    path("add/", CreateAlbumView.as_view(), name="create album"),
    path("<int:pk>/details/", DetailAlbumView.as_view(), name="details_album"),
    path("<int:pk>/edit/", EditAlbumView.as_view(), name="edit_album"),
    path("<int:pk>/delete/", DeleteAlbumView.as_view(), name="delete_album"),

)