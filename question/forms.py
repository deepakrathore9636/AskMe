from django import forms
from question.models import AskMe


class AskMeForm(forms.ModelForm):
    class Meta:
        model = AskMe
        fields = ['name', 'student_class', 'student_email', 'phone_number', 'question']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
