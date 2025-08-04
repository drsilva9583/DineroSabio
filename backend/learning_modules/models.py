from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LearningModule(models.Model):
    """Main educational modules for Dinero Sabio"""
    CATEGORY_CHOICES = [
        ('saving', 'How to Start Saving'),
        ('immigrants', 'Financial Tips for Immigrants'),
        ('myths', 'Money Myths Debunked'),
        ('investments', 'Cultural Investment Examples'),
    ]
    
    title = models.CharField(max_length=200)
    title_es = models.CharField(max_length=200, help_text="Spanish title")
    description = models.TextField()
    description_es = models.TextField(help_text="Spanish description")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon = models.CharField(max_length=50, default='💰')  # Emoji for UI
    estimated_time = models.IntegerField(help_text="Estimated time in minutes")
    difficulty_level = models.IntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced')], default=1)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
    
    def __str__(self):
        return f"{self.icon} {self.title}"
    
class Lesson(models.Model):
    """Individual lessons within modules"""
    LESSON_TYPES = [
        ('content', 'Educational Content'),
        ('calculator', 'Interactive Calculator'),
        ('story', 'Story/Example'),
        ('quiz', 'Quiz/Assessment'),
    ]
    
    module = models.ForeignKey(LearningModule, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    title_es = models.CharField(max_length=200)
    content = models.TextField()
    content_es = models.TextField()
    lesson_type = models.CharField(max_length=20, choices=LESSON_TYPES, default='content')
    order = models.IntegerField(default=0)
    
    # For interactive elements
    calculator_config = models.JSONField(null=True, blank=True, help_text="Configuration for calculators")
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.module.title} - {self.title}"

class Tip(models.Model):
    """Quick tips and actionable advice"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='tips')
    tip_text = models.CharField(max_length=300)
    tip_text_es = models.CharField(max_length=300)
    is_highlighted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.tip_text[:50]

class Quiz(models.Model):
    """Quizzes for myth-busting and knowledge checks"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='quizzes')
    question = models.CharField(max_length=500)
    question_es = models.CharField(max_length=500)
    
    # For "Mito o Realidad" type questions
    is_myth = models.BooleanField(help_text="True if this is a myth, False if it's reality")
    explanation = models.TextField()
    explanation_es = models.TextField()
    
    def __str__(self):
        return f"Quiz: {self.question[:50]}"

class Example(models.Model):
    """Cultural examples and analogies"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='examples')
    title = models.CharField(max_length=200)
    title_es = models.CharField(max_length=200)
    
    # Story content
    scenario = models.TextField(help_text="The example scenario")
    scenario_es = models.TextField()
    analogy = models.TextField(help_text="How it relates to investing/saving")
    analogy_es = models.TextField()
    
    # Visual elements
    image_description = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title