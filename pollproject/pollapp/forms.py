from django.forms import ModelForm
from pollapp.models import Spoll

class Myform(ModelForm):
	class Meta:
		model=Spoll
		fields='__all__'	