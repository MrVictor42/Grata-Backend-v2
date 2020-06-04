from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('images/', include('images.urls')),
    path('sectors/', include('sectors.urls')),
    path('projects/', include('projects.urls')),
    path('meetings/', include('meetings.urls')),
    path('agendas/', include('agenda.urls')),
    path('rules/', include('rules.urls')),
    path('comments/', include('comments.urls')),
    path('choices/', include('choices.urls')),
    path('questtionnaires/', include('questionnaires.urls')),
    path('questions/', include('questions.urls')),
    path('gradedQuesttionaire/', include('gradedQuesttionaire.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)