from django.urls import path
from users.api.views import UserViewSet, UserDetail, UserUpdate, UserDelete

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'})),
    path('informacoes/<int:pk>/', UserDetail.as_view()),
    path('alterar_informacoes/<int:pk>/', UserUpdate.as_view()),
    path('excluir_usuario/<int:pk>/', UserDelete.as_view())
]