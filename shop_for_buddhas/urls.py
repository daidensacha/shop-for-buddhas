from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('blog/', include('blog.urls')),
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configure site adminn panel headings
admin.site.site_header = 'Shop for Buddhas Admin'
admin.site.site_title = 'Shop for Buddhas'
admin.site.index_title = 'Welcome to Shop for Buddhas Admin Panel'
