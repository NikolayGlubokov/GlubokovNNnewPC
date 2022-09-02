from .models import City
from django.forms import Form, ModelForm, TextInput

class CityForm(ModelForm):

    class Meta:
        model = City
        fields = ('name',)
        widgets = {
            'name':TextInput(attrs={'class':'city',
                                    'name':'city',
                                    'placeholder':'Введите город'})
        }

