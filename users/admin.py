from django.contrib import admin

from .models import Userss



@admin.register(Userss)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','surname','age']

    list_display_links=['name','surname']

    search_fields=['name']

    list_filter=['age']
    class Meta:
        model=Userss
