from django.contrib import admin
from .models import MixModelRequest
from django.utils.html import format_html
# Register your models here.

@admin.register(MixModelRequest)
class MixModelRequestAdmin(admin.ModelAdmin):
    list_display = ('orderName', 'solicitor', 'date', 'get_duration', 'price', 'status_color_display')

    def get_duration(self, obj):
        return f"{obj.duration} days"
    get_duration.short_description = "Duration"

    def status_color_display(self, obj):
        """Display status color as a colored square."""
        color = obj.status_color
        status_name = obj.get_status_display()
        return format_html(
            '<span style="display:inline-block; width:20px; height:20px; background-color:{}; border-radius:3px;"> </span> {}', color, status_name
        )
    status_color_display.short_description = "Status"