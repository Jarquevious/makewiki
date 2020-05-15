
from django.urls import path
from accounts.views import home_view, signup_view

app_name='accounts'
urls = [
    path('signup/',  signup_view, name ='signup')
]


