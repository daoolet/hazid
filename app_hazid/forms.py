from django import forms

from .models import Survey


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [field.name for field in Survey._meta.get_fields() if field.name not in ("created_at", "author")]


