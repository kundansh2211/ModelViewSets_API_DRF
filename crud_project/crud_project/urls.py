
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from crud_app.views import MobileViewSet

router = DefaultRouter()
router.register('mobile', MobileViewSet, basename='mobile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls))
]
