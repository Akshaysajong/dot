from django.contrib import admin
from django.urls import path,include
from . import views
# from django.conf import settings

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('dot/dashboard/', views.dot_dashboard, name='dot_dashboard'),
    path('logout/', views.logoutuser, name="logout" ),
    path('dot/adduser/', views.dot_adduser, name='dot_adduser'), 
    path('dot/groups/', views.dot_groups, name='dot_groups'), 
    path('dot/addgroups/', views.dot_add_groups, name='dot_add_groups'), 
    path('dot/viewusers/', views.dot_viewusers, name='dot_viewusers'),
    path('dot/addgroup/permissions/', views.dot_add_groups_permissions, name='dot_add_groups_permissions'),

    #hoteladmin add hotels
    path('dot/addhotel/', views.dot_addhotel, name='dot_addhotel'),
    path('dot/addhoteldb/', views.dot_addhoteldb, name='dot_addhoteldb'),
    # path('dot/viewhotel/', views.dot_viewhotel, name='dot_viewhotel'),
    path('ajax_country/', views.ajax_country, name='ajax_country'),
    path('ajax_state/', views.ajax_state, name='ajax_state'),
    # path('dot/add_hotels/', views.dot_add_hotels, name='dot_add_hotels'),
    path('dot/content/', views.dot_content, name='dot_content'),


    path('dot/destination_area/', views.dot_destination_area, name='dot_destination_area'),
    path('dot/add_destination_area/', views.dot_add_destination_area, name='dot_add_destination_area'),
    path('dot/view_destinationarea/', views.dot_view_destinationarea, name='dot_view_destinationarea'),
    path('dot/destinations/', views.dot_destinations, name='dot_destinations'),
    path('dot/add_destination/', views.dot_add_destination, name='dot_add_destination'),
    path('dot/view_destination/', views.dot_view_destination, name='dot_view_destination'),
    path('dot/edit_destinationarea/', views.dot_edit_destinationarea, name='dot_edit_destinationarea'),
    path('delete_darea/', views.delete_darea, name='delete_darea'),
    path('dot/editdestination/', views.dot_editdestination, name='dot_editdestination'),
    path('delete_destination/', views.delete_destination, name='delete_destination'),
    path('dot/update_destination/', views.dot_update_destination, name='dot_update_destination'),

]
