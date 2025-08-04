from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LearningModuleViewSet, LessonViewSet

router = DefaultRouter()
router.register(r'modules', LearningModuleViewSet)
router.register(r'lessons', LessonViewSet)

urlpatterns = [
    path('api/learning/', include(router.urls)),
]