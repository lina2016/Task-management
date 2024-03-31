from django.forms import ModelForm, Textarea

from app.models import TODO
class TODOForm(ModelForm):
    class Meta:
        model = TODO
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 3}),
        }
        fields = ['title' , 'description','status' , 'priority']
