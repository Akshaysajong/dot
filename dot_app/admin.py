from django.contrib import admin
from .models import *
from django.contrib.auth.models import Permission

admin.site.register(Permission)
admin.site.register(destination_area)
admin.site.register(destinstions)
admin.site.register(destination_img)
admin.site.register(destn_geography)
admin.site.register(destn_facility)
admin.site.register(facility_price)
admin.site.register(facility_image)
admin.site.register(organization)
# admin.site.register(organization_images)
admin.site.register(userprofile)
admin.site.register(country)
admin.site.register(state)
admin.site.register(city)
admin.site.register(content)
admin.site.register(content_images)
admin.site.register(hotel_type)
admin.site.register(customer)
admin.site.register(cust_profile)
admin.site.register(staff_department)
admin.site.register(best_things)
admin.site.register(card)
admin.site.register(feedback)
admin.site.register(icons)
admin.site.register(booking)
admin.site.register(destination_type)


