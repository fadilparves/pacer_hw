from django.contrib import admin
from .models import Score

# Register your models here.

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'score')
    search_fields = ['user_id', 'score']

admin.site.register(Score, ScoreAdmin)
