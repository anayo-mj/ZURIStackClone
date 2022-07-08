from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'questions'#added 'apps.' since we moved apps into an apps folder
