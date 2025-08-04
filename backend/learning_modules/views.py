from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import LearningModule, Lesson, Quiz
from .serializers import (
    LearningModuleSerializer, 
    LearningModuleListSerializer,
    LessonSerializer,
    QuizSerializer
)

class LearningModuleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LearningModule.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'difficulty_level']
    search_fields = ['title', 'title_es', 'description', 'description_es']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return LearningModuleListSerializer
        return LearningModuleSerializer
    
    @action(detail=False, methods=['get'])
    def categories(self, request):
        """Get all available categories with their info"""
        categories = []
        for value, label in LearningModule.CATEGORY_CHOICES:
            count = LearningModule.objects.filter(category=value, is_active=True).count()
            categories.append({
                'value': value,
                'label': label,
                'count': count
            })
        return Response(categories)
    
    @action(detail=True, methods=['get'])
    def lessons(self, request, pk=None):
        """Get all lessons for a specific module"""
        module = self.get_object()
        lessons = module.lessons.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['module', 'lesson_type']