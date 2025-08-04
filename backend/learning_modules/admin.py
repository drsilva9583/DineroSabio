from django.contrib import admin
from .models import LearningModule, Lesson, Tip, Quiz, Example

@admin.register(LearningModule)
class LearningModuleAdmin(admin.ModelAdmin):
    list_display = ['icon', 'title', 'category', 'difficulty_level', 'estimated_time', 'is_active']
    list_filter = ['category', 'difficulty_level', 'is_active']
    search_fields = ['title', 'title_es']
    ordering = ['order', 'created_at']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'lesson_type', 'order']
    list_filter = ['module', 'lesson_type']
    search_fields = ['title', 'title_es']
    ordering = ['module', 'order']

@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ['tip_text', 'lesson', 'is_highlighted']
    list_filter = ['is_highlighted', 'lesson__module']

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['question', 'lesson', 'is_myth']
    list_filter = ['is_myth', 'lesson__module']

@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ['title', 'lesson']
    list_filter = ['lesson__module']