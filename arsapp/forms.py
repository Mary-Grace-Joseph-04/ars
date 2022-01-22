from django import forms
from django.contrib.auth.forms import UserCreationForm
from arsapp.models import reservedetails
from .models import MyUser, places, classes

class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=10)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender= forms.CharField(max_length=32)
    nationality= forms.CharField(max_length=32)
    address= forms.CharField(max_length=1024)

    class Meta:
        model = MyUser
        fields = ['username','first_name','email','last_name','password1','dob','gender','nationality','address','password2']
        widgets={
            'dob': DateInput(attrs={'type':'date'})
        }

class reservedetailsform(forms.ModelForm):
    departure_city=forms.ModelChoiceField(queryset=places.objects.all())
    arrival_city=forms.ModelChoiceField(queryset=places.objects.all())
    Class=forms.ModelChoiceField(queryset=classes.objects.all())
    date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = reservedetails
        fields = ['departure_city','arrival_city','Class','date']


    def clean(self):
        cleaned_data = super(reservedetailsform, self).clean()
        departure_city = cleaned_data.get("departure_city")
        arrival_city = cleaned_data.get("arrival_city")
        date = cleaned_data.get("date")
        today = date.today() 

        if departure_city == arrival_city:
            self._errors['arrival_city'] = self.error_class(['Both arrival and destination is same'])
            del self.cleaned_data['arrival_city']

        if date < today:
            self._errors['date'] = self.error_class(['enter a valid date'])
            del self.cleaned_data['date']

        return cleaned_data

    # def __init__(self, *args, **kwargs):
    #     self._user = kwargs.pop('user')
    #     super(reservedetailsform, self).__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     inst = super(reservedetailsform, self).save(commit=False)
    #     inst.user = self._user
    #     if commit:
    #         inst.save()
    #         self.save_m2m()
    #     return inst

