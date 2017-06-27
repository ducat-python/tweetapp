from django.conf.urls import url

from .views import tweet_list

urlpatterns = [

    url(r'^list/', tweet_list, name='list')

]
