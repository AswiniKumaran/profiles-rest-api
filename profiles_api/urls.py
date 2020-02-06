from django.urls import path,include
from profiles_api.views import HelloApiView,HelloAPiViewSet,UserProfileSerializer
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hello_api_viewset',HelloAPiViewSet,base_name='hello_api_viewset')
router.register('profile',UserProfileSerializer)
urlpatterns=[
    path('hello_api_view/',HelloApiView.as_view()),
    path('',include(router.urls))
]
