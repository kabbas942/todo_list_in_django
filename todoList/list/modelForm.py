from django import forms
from list.models import todoList
class todoListForm(forms.ModelForm):
    class Meta:
        model = todoList
        fields = '__all__'
        
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control','type': 'date'}),
            'completed' : forms.DateTimeInput(attrs={'class': 'form-control','type': 'date'}),
            # Add more fields and their corresponding HTML classes
        }