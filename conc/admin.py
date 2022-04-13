from django.contrib import admin
from .models import TempScore, History

class TempScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'time')

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'avg_score', 'start_time', 'end_time', 'duration')

admin.site.register(TempScore, TempScoreAdmin)
admin.site.register(History, HistoryAdmin)
