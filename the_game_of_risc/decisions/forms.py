from django import forms
from django.forms.widgets import RadioSelect



from .models import Decision

class DecisionForm(forms.ModelForm):

    class Meta:
        model = Decision
        fields = ('answer',)
        # choices = (('True', 'Accepted'), ('False', 'Denied'))
        # widgets = {
        #      'answer':  forms.ChoiceField(widget=RadioSelect(), choices=choices)
        # }
