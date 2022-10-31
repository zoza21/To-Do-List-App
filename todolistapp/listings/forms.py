from django import forms
from .models import Todolist


class Todoform(forms.Form):
	item = forms.CharField(label="Item",required=True,widget=forms.TextInput(attrs={'class':'item'}))
	details = forms.CharField(label="Details",required=True,widget=forms.TextInput(attrs={'class':'details'}))
	


class Listform(forms.ModelForm):
	class Meta:
		model = Todolist
		fields = '__all__'
		


