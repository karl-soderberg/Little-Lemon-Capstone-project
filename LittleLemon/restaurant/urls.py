from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers  import DefaultRouter
from restaurant.views import BookingViewSet

router = DefaultRouter()
router.register(r'tables', BookingViewSet)


urlpatterns = [
    path('', views.home, name="home"),
    path('booking/', include(router.urls)),
    path('menu/', views.MenuView.as_view(), name="menu"),
    path('menu/<int:pk>/', views.SingleMenuVeiew.as_view(), name="menu_item"),  
    path('api-token-auth/', obtain_auth_token, name='api_token_auth') 
]