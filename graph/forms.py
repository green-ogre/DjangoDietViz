from django import forms


class DataForm(forms.Form):
    weight = forms.FloatField(label="Morning Weight (lb)", min_value=0.0, help_text='e.g. 182.4')
    calories = forms.FloatField(label="Total Calories (kcal)", min_value=0.0, help_text='e.g. 3500')
    protein = forms.FloatField(label="Total Protein (g)", min_value=0.0, help_text='e.g. 180')