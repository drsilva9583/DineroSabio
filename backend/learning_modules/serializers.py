from rest_framework import serializers
from .models import LearningModule, Lesson, Tip, Quiz, Example

class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ['id', 'tip_text', 'tip_text_es', 'is_highlighted']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'question', 'question_es', 'is_myth', 'explanation', 'explanation_es']

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ['id', 'title', 'title_es', 'scenario', 'scenario_es', 'analogy', 'analogy_es', 'image_description']

class LessonSerializer(serializers.ModelSerializer):
    tips = TipSerializer(many=True, read_only=True)
    quizzes = QuizSerializer(many=True, read_only=True)
    examples = ExampleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Lesson
        fields = [
            'id', 'title', 'title_es', 'content', 'content_es',
            'lesson_type', 'order', 'calculator_config',
            'tips', 'quizzes', 'examples'
        ]

class LearningModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField()
    
    class Meta:
        model = LearningModule
        fields = [
            'id', 'title', 'title_es', 'description', 'description_es',
            'category', 'icon', 'estimated_time', 'difficulty_level',
            'lessons_count', 'lessons', 'created_at'
        ]
    
    def get_lessons_count(self, obj):
        return obj.lessons.count()

# Simplified serializer for listing modules (without full lesson content)
class LearningModuleListSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    
    class Meta:
        model = LearningModule
        fields = [
            'id', 'title', 'title_es', 'description', 'description_es',
            'category', 'icon', 'estimated_time', 'difficulty_level',
            'lessons_count'
        ]
    
    def get_lessons_count(self, obj):
        return obj.lessons.count()