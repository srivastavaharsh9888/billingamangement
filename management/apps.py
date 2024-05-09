from django.apps import AppConfig


class ManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'management'

    def ready(self):
        # Prevent default admin site from auto-discovering any admin options
        # Optionally include any signals or other startup code here
        pass