from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

from home.models import Subject, Set, Question

@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    list_display = ('name',)

@admin.register(Set)
class SetAdmin(ImportExportModelAdmin):
    list_display = ('name',)

@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin):
    list_display = ('question',)



