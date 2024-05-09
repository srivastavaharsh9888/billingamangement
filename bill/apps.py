from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'my_app'

    def ready(self):
        # Prevent default admin site from auto-discovering any admin options
        # Optionally include any signals or other startup code here
        pass
