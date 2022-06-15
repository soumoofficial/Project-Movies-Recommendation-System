# Register your models here.
from django.contrib import admin
from .models import Movie_list
from .models import Contact
from import_export.admin import ImportExportModelAdmin

@admin.register(Movie_list)
class userdata(ImportExportModelAdmin):
    pass

admin.site.register(Contact)