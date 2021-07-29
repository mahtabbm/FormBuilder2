from django.urls import path, include
from business_api import views
from rest_framework.routers import DefaultRouter

"""
router = DefaultRouter
router.register('...viewset', views....ViewSet, base_name='..viewset')
"""

router = DefaultRouter()
router.register('register', views.RegisterViewSet)
#router.register('feed', views.BusinessFeedViewSet)
router.register('form', views.FormViewSet)
#router.register('part', views.PartViewSet)
#router.register('option', views.OptionViewSet)

urlpatterns = [
    path('login/', views.LoginApiView.as_view()),
    path('', include(router.urls)),
]
