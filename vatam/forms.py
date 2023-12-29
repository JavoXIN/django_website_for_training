from django import forms

class OrderForm(forms.Form):
    # men qoshdim0324 6:36pm
    # name = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    # man qoshdim0324,0753pm
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    #day = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))  #men qoshdim 0523
    #time = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))  #men qoshdim 0523
