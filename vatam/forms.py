from django import forms

class OrderForm(forms.Form):        #men qoshdim 0324 6:36pm
    # name = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'css_input'}))      #man qoshdim0324,0753pm
    phone = forms.CharField(max_length=200)