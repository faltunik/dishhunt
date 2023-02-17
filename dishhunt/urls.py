
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include
from users import views
from dish import views as dishviews
from rest_framework.routers import DefaultRouter



user_router = DefaultRouter()
# register our viewset with router
user_router.register('user', views.UserViewSet, basename = 'user')

dish_router = DefaultRouter()
# register our viewset with router
dish_router.register('dish', dishviews.DishViewSet, basename = 'dish')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(dish_router.urls)),
    path('user/', include(user_router.urls)),
    path('auth', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
