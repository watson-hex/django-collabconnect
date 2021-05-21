from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'todo', views.TodoView, 'todo')
router.register(r'profile', views.ProfileView, 'profile')
router.register(r'teacher', views.TeacherView, 'teacher')
router.register(r'skill', views.SkillView, 'skill')

# TODO: #2 Better url names
urlpatterns = [
    path('searchfor/<str:search>/', views.detail, name='detail'),
    path('searchfordata/', views.details, name='details'),
    path('get_profile/', views.Profilegetter, name='Profilegetter'),
    path('lolcheck/', views.profile_list, name='lolcheck'),
    path('api/', include(router.urls)),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())]
