from django.contrib import admin
from django.urls import path, include

# Define the main URLS for project
urlpatterns = [

    # Django admin page
    path('admin/', admin.site.urls),

    # Send API requests to the dogapi app
    path('api/', include('dogapi.urls')),

]