"""
URL configuration for MUFC2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path

from MUFC2.api.event_api import create_event_endpoint, delete_event_endpoint, get_event_by_month_endpoint, \
    get_event_details_endpoint, get_event_by_day_endpoint, get_friend_event_list_endpoint, get_user_event_list_endpoint, \
    edit_event_details_endpoint
from MUFC2.api.friend_api import get_friend_details_endpoint, get_friends_from_user_endpoint, add_friend_endpoint, \
    update_friend_all_att_endpoint, update_friend_single_att_endpoint, delete_friend_endpoint, get_sorted_friend_list, \
    get_promptly_contact_friend_endpoint
from MUFC2.api.hobby_api import get_friend_hobbies_endpoint, get_sorted_hobby_popularity_endpoint, \
    filter_friends_with_all_hobbies_endpoint, add_hobby_to_friend_endpoint, remove_hobby_from_friend_endpoint
from MUFC2.api.user_api import create_user_endpoint, login_endpoint, get_user_from_id_endpoint, \
    update_all_user_fields_endpoint, update_user_attribute_endpoint, delete_user_endpoint

# import MUFC2.api.event_api
# import MUFC2.api.hobby_api
# import MUFC2.api.user_api
# import MUFC2.api.friend_api

urlpatterns = [
    path('admin/', admin.site.urls),
    # User urls
    path('api/user/create/', create_user_endpoint, name='create_user'),
    path('api/user/login/', login_endpoint, name='login'),
    path('api/user/<str:user_id>/', get_user_from_id_endpoint, name='get_user'),
    path('api/user/<str:user_id>/update_all/', update_all_user_fields_endpoint, name='update_user_all'),
    path('api/user/<str:user_id>/update_single/', update_user_attribute_endpoint, name='update_user_single'),
    path('api/user/<str:user_id>/delete/', delete_user_endpoint, name='delete_user'),


    # Friend urls
    path('api/friend/<str:friend_id>/', get_friend_details_endpoint, name='get_friend_details'),
    path('api/user/<str:user_id>/friends/', get_friends_from_user_endpoint, name='get_friend_list'),
    path('api/user/<str:user_id>/add_friend/', add_friend_endpoint, name='add_friend'),
    path('api/friend/<str:friend_id>/update_all/', update_friend_all_att_endpoint, name='update_friend_all'),
    path('api/friend/<str:friend_id>/update_single/', update_friend_single_att_endpoint, name='update_friend_single'),
    path('api/friend/<str:friend_id>/delete/', delete_friend_endpoint, name='delete_friend'),
    path('api/user/<str:user_id>/friends/sort/', get_sorted_friend_list, name='get_friend_list_sorted'),
    path('api/user/<str:user_id>/friends/promptly_contact/', get_promptly_contact_friend_endpoint, name='promptly_contact_friend'),

    # Hobby urls
    path('api/friend/<str:friend_id>/hobbies/', get_friend_hobbies_endpoint, name='get_friend_hobbies'),
    path('api/user/<str:user_id>/hobbies_sorted/', get_sorted_hobby_popularity_endpoint, name='get_hobbies_sorted_popularity'),
    path('api/user/<str:user_id>/friends_hobbies_filtered/', filter_friends_with_all_hobbies_endpoint, name='filter_friends_with_hobbies'),
    path('api/friend/<str:friend_id>/hobbies/add/', add_hobby_to_friend_endpoint, name='add_hobby'),
    path('api/friend/<str:friend_id>/hobbies/remove/', remove_hobby_from_friend_endpoint, name='remove_hobby'),

    # Event urls
    path('api/user/<str:user_id>/friend/<str:friend_id>/event/create/', create_event_endpoint, name='create_event'),
    path('api/event/<str:event_id>/', get_event_details_endpoint, name='get_event'),
    path('api/event/<str:event_id>/edit/', edit_event_details_endpoint, name='edit_event'),
    path('api/event/<str:event_id>/delete/', delete_event_endpoint, name='delete_event'),
    path('api/event/grouping_month/user/<str:user_id>/', get_event_by_month_endpoint, name='event_month'),
    path('api/event/grouping_day/user/<str:user_id>/', get_event_by_day_endpoint, name='event_day'),
    path('api/friend/<str:friend_id>/event_list/', get_friend_event_list_endpoint, name='friend_event_list'),
    path('api/user/<str:user_id>/event_list/', get_user_event_list_endpoint, name='user_event_list'),

]