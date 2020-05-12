from django.urls import path

from projects.api.views import ProjectListView, ProjectCreateView, \
                               ProjectDetailView, ProjectUpdateView, \
                               ProjectDeleteView, ProjectsListView, \
                               ProjectAddUsers, ProjectRemoveUsers

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('create/', ProjectCreateView.as_view()),
    path('detail/<pk>/', ProjectDetailView.as_view()),
    path('update/<pk>/', ProjectUpdateView.as_view()),
    path('delete/<pk>/', ProjectDeleteView.as_view()),
    path('projects_in_sector/<pk>/', ProjectsListView.as_view()),
    path('add_users_project/<pk>/', ProjectAddUsers.as_view()),
    path('remove_users_project/<pk>/', ProjectRemoveUsers.as_view())
]