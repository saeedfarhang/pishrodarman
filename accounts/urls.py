from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'accounts'
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('profile',views.profile,name='profile'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('logout/',views.logout_view,name='logout'),
    
    path('', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
