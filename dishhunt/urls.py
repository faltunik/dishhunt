
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include
from users import views
from rest_framework.routers import DefaultRouter



user_router = DefaultRouter()
# register our viewset with router
user_router.register('user', views.UserViewSet, basename = 'user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dish.urls')), 
    path('user/', include(user_router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
