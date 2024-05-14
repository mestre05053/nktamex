from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api-html", views.api_html, name="api-html"),
    #### STORE PROCEDURES ###
    path("store-proc", views.store_proc, name="store-proc"),
    path("create-proc", views.create_store_get_users, name="create-proc"),
    path("get-proc-users", views.get_proc_users, name="get-proc-users"),
    ####API###
    path('api-list/', views.LISTAPI.as_view(), name='api-list'),
    path('api-create/', views.RecordCreatedApi.as_view(), name='api-create'),
    path('api-update/', views.RecordUpdateApi.as_view(), name='api-update'),
    #### ART ####
    path('art-get/', views.ArtGet.as_view(), name='art-get'),
    path('art-post/', views.ArtPost.as_view(), name='art-post'),
]