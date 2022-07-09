from django import forms
from local_settings import AVAILABLE_CITIES, PRICE_CATEGORIES, RESTAURANT_RATING, CUISINE


class UserForm(forms.Form):
    user_city = forms.ChoiceField(help_text='Your city',
                                  choices=AVAILABLE_CITIES,
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  )
    price_category = forms.ChoiceField(choices=PRICE_CATEGORIES,
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    restaurant_rating = forms.ChoiceField(choices=RESTAURANT_RATING,
                                          widget=forms.Select(attrs={'class': 'form-control'}))
    cuisine_choice_list1 = forms.ChoiceField(choices=CUISINE,
                                             widget=forms.Select(attrs={'class': 'form-control'}))
    cuisine_choice_list2 = forms.ChoiceField(choices=CUISINE,
                                             widget=forms.Select(attrs={'class': 'form-control'}))

