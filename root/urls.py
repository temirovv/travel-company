from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from apps.payments.views import PaymeCallBackAPIView


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('api/payments/merchant/', PaymeCallBackAPIView.as_view()),
]

urlpatterns += i18n_patterns(
    path('aziz-admin/', admin.site.urls),
    path('', include('apps.tour_packages.urls')),
    path('payment/', include('apps.payments.urls')),
    path('accounts/', include('apps.users.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
)
