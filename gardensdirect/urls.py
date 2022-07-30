from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static
from calculator import views
from admin_products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('main.urls'), name='index'),
    path('quote/', include('calculator.urls')),
    path('profile/', include('profiles.urls')),
    path('site_owner/', include('admin_products.urls'),)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "gardensdirect.views.page_not_found_view"
