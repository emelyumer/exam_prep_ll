from django.urls import path

from djangoProject.albums.views import CreateViewAlbumView, DetailAlbumView, EditViewAlbumView, DeleteAlbumView

urlpatterns = (
    path("add/", CreateViewAlbumView.as_view(), name="create album"),
    path("<int:pk>/details/", DetailAlbumView.as_view(), name="details_album"),
    path("<int:pk>/edit/", EditViewAlbumView.as_view(), name="edit_album"),
    path("<int:pk>/delete/", DeleteAlbumView.as_view(), name="delete_album"),

)