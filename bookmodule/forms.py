from django import forms
from .models import Student, Address,ImageModel

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class StudentForm(forms.ModelForm):
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Use checkboxes for multiple selection
    )
    class Meta:
        model = Student
        fields = ['name', 'age', 'addresses']



class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'
