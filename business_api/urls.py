from django.urls import path, include
from business_api import views
from rest_framework.routers import DefaultRouter

"""
router = DefaultRouter
router.register('...viewset', views....ViewSet, base_name='..viewset')
"""

router = DefaultRouter()
router.register('account/register', views.RegisterViewSet)
router.register('feed', views.BusinessFeedViewSet)

urlpatterns = [
    path('account/login/', views.LoginApiView.as_view()),
    path('', include(router.urls)),
]
