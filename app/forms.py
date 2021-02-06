from django.forms import ModelForm
from app.models import Carros

# Create your models here.
class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['modelo', 'marca', 'ano']
        