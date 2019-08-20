from django.urls import path

from .views import BookmarkListView, BookmarkCreateView, BookmarkDetail, BookmarkUpdate

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetail.as_view(), name='detail' ),
    path('update/<int:pk>/', BookmarkUpdate.as_view(), name='update'),

]