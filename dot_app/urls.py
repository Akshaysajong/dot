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
    path('dot/viewhotels/', views.dot_viewhotels, name='dot_viewhotels'),
    path('dot/edit_hotel/', views.dot_edit_hotel, name='dot_edit_hotel'),
    path('dot/edit_hoteldb/', views.dot_edit_hoteldb, name='dot_edit_hoteldb'),
    path('delete_hotel/', views.delete_hotel, name='delete_hotel'),
    path('dot/update_hotel/', views.dot_update_hotel, name='dot_update_hotel'),
    path('ajax_country/', views.ajax_country, name='ajax_country'),
    path('ajax_state/', views.ajax_state, name='ajax_state'),
    path('dot/content/', views.dot_content, name='dot_content'),


    path('dot/destination_area/', views.dot_destination_area, name='dot_destination_area'),
    path('dot/add_destination_area/', views.dot_add_destination_area, name='dot_add_destination_area'),
    path('dot/view_destinationarea/', views.dot_view_destinationarea, name='dot_view_destinationarea'),
    path('dot/destinations/', views.dot_destinations, name='dot_destinations'),
    path('dot/add_destination/', views.dot_add_destination, name='dot_add_destination'),
    path('dot/view_destination/', views.dot_view_destination, name='dot_view_destination'),
    path('dot/edit_destinationarea/', views.dot_edit_destinationarea, name='dot_edit_destinationarea'),
    path('delete_darea/', views.delete_darea, name='delete_darea'),
    path('dot/update_destinationarea/', views.dot_update_destinationarea, name='dot_update_destinationarea'),
    path('dot/editdestination/', views.dot_editdestination, name='dot_editdestination'),
    path('delete_destination/', views.delete_destination, name='delete_destination'),
    path('dot/update_destination/', views.dot_update_destination, name='dot_update_destination'),
    path('dot/addorganization/', views.dot_addorganization, name='dot_addorganization'),
    path('dot/addorganization_db/', views.dot_addorganization_db, name='dot_addorganization_db'),
    path('dot/organizationlist/', views.dot_organizationlist, name='dot_organizationlist'),
    path('dot/edite_organization/', views.dot_edite_organization, name='dot_edite_organization'),
    path('dot/updateorganization/', views.dot_updateorganization, name='dot_updateorganization'),
    path('dot/addfacilitytype/', views.dot_addfacilitytype, name='dot_addfacilitytype'),
    path('dot/viewfacilitytype/', views.dot_viewfacilitytype, name='dot_viewfacilitytype'),
    path('dot/addfacility/', views.dot_addfacility, name='dot_addfacility'),
    path('dot/addfacilitydb/', views.dot_addfacilitydb, name='dot_addfacilitydb'),
    path('dot/viewfacilitylist/', views.dot_viewfacilitylist, name='dot_viewfacilitylist'),
]
