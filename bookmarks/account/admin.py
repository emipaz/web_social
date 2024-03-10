from django.contrib import admin

# Register your models here.
from .models import Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fecha_nacimiento', 'foto']
    raw_id_fields = ['usuario']