from django.urls import path
from profiles_api.views import HelloApiView

urlpatterns=[
    path('hello_api_view/',HelloApiView.as_view())
]
