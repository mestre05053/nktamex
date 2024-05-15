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
    ###### Learning from book Django_RESTful_Web_Services_The_Easiest_Way_to_Bui...
    path('list-users',views.user_list, name='list-users'),
    path('user-detail/<int:pk>',views.user_detail, name='user-detail'),
    #### THIS IS THE WAY #### Learning www.django-rest-framework.org/tutorial/2-requests-and-responses/
    path('snippet',views.snippet_list, name='snippet'),
    path('snippet/<int:pk>',views.snippet_detail, name='snippet_detail'),
 
]