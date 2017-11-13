from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update_photo/$',
        view=views.UserUpdatePhotoView.as_view(),
        name='update_photo'
    ),
    url(
        regex=r'^~update_data/$',
        view=views.UserUpdateDataView.as_view(),
        name='update_data'
    ),
]
