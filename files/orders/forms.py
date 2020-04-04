from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # to = forms.EmailField()  
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone']


# class EmailPostForm(forms.Form):  
#     name = forms.CharField(max_length=25)  
#     email = forms.EmailField()  
#     to = forms.EmailField()  
#     comments = forms.CharField(required=False,  
# 			       widget=forms.Textarea)