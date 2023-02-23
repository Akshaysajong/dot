from django.contrib import admin
from django.urls import path,include
from . import views
# from .views import get_data
from django.conf import settings
from django.conf.urls.static import static
# from .import DestinationViewSet
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('api/destinations',views.DestinationViewSet, basename="destinations")
from .views import LocationList, LocationDetail,autocompleteList,autocompleteDetail
from rest_framework import filters
# from django.conf import settings
from .views import facilityReviewListCreateAPIView,destinationReviewListCreateAPIView
from .views import AccountView
from django.urls import path, include
# from rest_framework import routers
from .views import facilityReviewAPIView,destinationReviewViewSet,travelmemoriesViewSet

# router = routers.DefaultRouter()
# router.register('api/facilityreviews_view', facilityReviewAPIView)
# router = routers.DefaultRouter()
# router.register('api/destinationreviews', destinationReviewViewSet)
# router = routers.DefaultRouter()
# router.register('api/accounts',views.AccountViewSet,basename="accounts")

urlpatterns = [
    # path('data/',get_data, name='data'),
    # path('api/',include('dot_app.urls')),

    # path('', include(router.urls)),
    path('login/', views.login_user, name='login'),
    path('dot/dashboard/', views.dot_dashboard, name='dot_dashboard'),
    path('logout/', views.logoutuser, name="logout" ),
    path('dot/adduser/', views.dot_adduser, name='dot_adduser'), 
    path('dot/groups/', views.dot_groups, name='dot_groups'), 
    path('dot/addgroups/', views.dot_add_groups, name='dot_add_groups'), 
    path('dot/viewusers/', views.dot_viewusers, name='dot_viewusers'),
    path('dot/edit_user/', views.dot_edit_user, name='dot_edit_user'),
    path('dot/addgroup/permissions/', views.dot_add_groups_permissions, name='dot_add_groups_permissions'),
    path('dot/delete_user/', views.dot_delete_user, name='dot_delete_user'),
    path('dot/updateuser/', views.dot_updateuser, name='dot_updateuser'),

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
    # path('dot/add_staff/', views.dot_add_staffdb, name='dot_add_staff'),

    # api
    
    # path('api/cust_profile/',views.cust_profileRegister.as_view(),name='cust_profileRegister'),
    path('api/greenktchen_homepage_content/',views.homepage_contentgreenkitchen, name='homepage-content'),
    # static
    path('api/homepage_contentdot/',views.homepage_contentdot, name='homepage-contentdot'),

    path('api/register/',views.Register.as_view(),name='register'),
    path('api/login/',views.LoginView.as_view(),name='login'),
    path('api/dot_homepage/',views.dot_homepageAPI.as_view(), name='dot_homepage'),
    path('api/dot_button_details/',views.dot_button_detailsAPI.as_view(), name='dot_button_details'),
    path('api/dot_destination_details/',views.dot_destination_detailsAPI.as_view(), name='dot_destination_details'),
    path('api/dot_destination_humpidetails/',views.dot_destination_humpidetailsAPI.as_view(), name='dot_destination_humpidetails'),
    path('api/dot_wanderlust_humpidetails/',views.dot__wanderlust_humpidetailsAPI.as_view(), name='dot_wanderlust_humpidetails'),
    path('api/dot_wanderlust_bookingdetails/',views.dot__wanderlust_bookingAPI.as_view(), name='dot_wanderlust_bookingdetails'),
    path('api/dot__more_stays/',views.dot__more_staysAPI.as_view(), name='dot__more_stays'),
    path('api/categorysearch',views.categorysearchView.as_view(), name='categorysearch'),
    path('api/searchauto/', autocompleteList.as_view(), name='searchauto-list'),
    path('api/searchauto/<int:pk>/', autocompleteDetail.as_view(), name='searchauto-detail'),
    path('api/searchauto/search/', autocompleteList.as_view(filter_backends=[filters.SearchFilter]), name='searchauto-search'),
    path('api/contentdetails/',views.contentdetailsAPI.as_view(), name='contentdetails'),
    path('api/subscription/', views.SubscriptionView.as_view(), name='subscription'),
    path('api/myaccount/', views.AccountView.as_view(), name='myaccount-list'),
    path('api/loginvalidation/',views.LoginvalidationView.as_view(),name='loginvalidation'),   
    path('api/locations/', LocationList.as_view(), name='location-list'),
    path('api/locations/<int:pk>/', LocationDetail.as_view(), name='location-detail'),
    path('api/locations/search/', LocationList.as_view(filter_backends=[filters.SearchFilter]), name='location-search'),
    path('api/filtersearch_results/',views.filtersearch_resultsView.as_view(({'get': 'list'})), name='filtersearch_results'),
    path('api/facilityaddreviews/', facilityReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('api/facilityreview_view/', facilityReviewAPIView.as_view(({'get': 'list'})), name='facilityreview_view'),
    path('api/destinationaddreviews/', destinationReviewListCreateAPIView.as_view(), name='destinationaddreviews'),
    path('api/destinationfacilityreview_view/', destinationReviewViewSet.as_view(({'get': 'list'})), name='destinationfacilityreview_view'),
    path('api/memorydetails/<int:id>/', views.MemoryDetailAPIView.as_view(), name='memory-detail'), 

    path('api/organization_details/',views.organization_detailsAPI.as_view(), name='organization_details'),   
    # path('api/editaccount/', views.EditCustomerView.as_view(), name='editaccount-list'), 
    path('api/editaccount/<int:pk>/', views.EditCustomerView.as_view(), name='editaccount-detail'),   
    path('api/travelhistory/',views.travelhistoryAPI.as_view(),name='travelhistory'),
    path('api/addmemories/',views.MemoryCreateView.as_view(), name='memory_create'),
    path('api/travelmemories/', travelmemoriesViewSet.as_view(({'get': 'list'})), name='destinationfacilityreview_view'),
    
    # path('memoryimages/', ImageList.as_view(), name='image-list'),
    # path('memoryimages/<int:pk>/', ImageDetail.as_view(), name='image-detail'),
    # path('customers/(?P<id>\d+)/$',views.EditCustomerView.as_view(),name='editaccount-list'),
  

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
    path('dot/delete_organization/', views.dot_delete_organization, name='dot_delete_organization'),
    path('dot/updateorganization/', views.dot_updateorganization, name='dot_updateorganization'),
    path('delete_organization/', views.delete_organization, name='delete_organization'),
    path('dot/addfacilitytype/', views.dot_addfacilitytype, name='dot_addfacilitytype'),
    path('dot/viewfacilitytype/', views.dot_viewfacilitytype, name='dot_viewfacilitytype'),
    path('dot/edit_facilitytype/', views.dot_edit_facilitytype, name='dot_edit_facilitytype'),
    path('dot/update_facilitytype/', views.dot_update_facilitytype, name='dot_update_facilitytype'),
    path('dot/delete_facilitytype/', views.dot_delete_facilitytype, name='dot_delete_facilitytype'),
    path('dot/addfacility/', views.dot_addfacility, name='dot_addfacility'),
    path('dot/addfacilitydb/', views.dot_addfacilitydb, name='dot_addfacilitydb'),
    path('dot/viewfacilitylist/', views.dot_viewfacilitylist, name='dot_viewfacilitylist'),
    path('dot/edit_facility/', views.dot_edit_facility, name='dot_edit_facility'),
    path('dot/updatefacility/', views.dot_updatefacility, name='dot_updatefacility'),
    path('dot/orderlist/', views.dot_orderlist, name='dot_orderlist'),
    path('dot/bookinglist/', views.dot_bookinglist, name='dot_bookinglist'),
   
    path('dot/addstaff/', views.dot_addstaff, name='dot_addstaff'),
    path('dot/savestaff/', views.dot_savestaff, name='dot_addstaff'),
    path('dot/stafflist/', views.dot_stafflist, name='dot_stafflist'),
    path('dot/editstaff/', views.dot_editstaff, name='dot_editstaff'),
    path('dot/updatestaff/', views.dot_updatestaff, name='dot_updatestaff'),
    path('dot/deletestaff/', views.dot_deletestaff, name='dot_deletestaff'),
    path('dot/addcontent/', views.dot_addcontent, name='dot_addcontent'),
    path('dot/savecontent/', views.dot_savecontent, name='dot_savecontent'),
    path('dot/contentlist/', views.dot_contentlist, name='dot_contentlist'),
    path('dot/deletecontent/', views.dot_deletecontent, name='dot_deletecontent'),
    path('dot/editcontent/', views.dot_editcontent, name='dot_editcontent'),
    path('dot/updatecontent/', views.dot_updatecontent, name='dot_updatecontent'),
    path('dot/delete_contentimage/', views.dot_deletecontentimage, name='dot_deletecontentimage'),
    path('dot/deleteimgcontent/', views.dot_deleteimgcontent, name='dot_deleteimgcontent'),

    path('dot/addfaq_category/', views.dot_addfaq_category, name='dot_addfaq_category'),
    path('dot/savefaqcategory/', views.dot_savefaqcategory, name='dot_savefaqcategory'),
    path('dot/faqcategorylist/', views.dot_faqcategorylist, name='dot_faqcategorylist'),
    path('dot/editfaqcategory/', views.dot_editfaqcategory, name='dot_editfaqcategory'),
    path('dot/updatefaqcategory/', views.dot_updatefaqcategory, name='dot_updatefaqcategory'),

    path('dot/deletefaqcategory/', views.dot_deletefaqcategory, name='dot_deletefaqcategory'),
    path('dot/addfaq/', views.dot_addfaq, name='dot_addfaq'),
    path('dot/savefaq/', views.dot_savefaq, name='dot_savefaq'),
    path('dot/viewfaqlist/', views.dot_viewfaqlist, name='dot_viewfaqlist'),
    path('dot/editfaq/', views.dot_editfaq, name='dot_editfaq'),
    path('dot/updatefaq/', views.dot_updatefaq, name='dot_updatefaq'),
    path('dot/deletefaq/', views.dot_deletefaq, name='dot_deletefaq'),


]

# urlpatterns += router.urls