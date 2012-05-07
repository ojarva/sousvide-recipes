# -*- coding: utf-8
from django import forms
from django.utils.safestring import mark_safe
from django.utils.encoding import StrAndUnicode, force_unicode
from django.utils.html import escape, conditional_escape
from django.forms.util import flatatt
from models import Making

class NumberInput(forms.Widget):
    input_type="number"
    input_type="range"

    def __init__(self, attrs=None):
        default_attrs = {"type": "number"}
        if attrs:
            default_attrs.update(attrs)
        super(NumberInput, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(u'<input %s value="%s" />' % (flatatt(final_attrs),
                conditional_escape(force_unicode(value))))


class RangeInput(forms.Widget):
    input_type="range"

    def __init__(self, attrs=None):
        default_attrs = {'min': '1', 'max': '5', "type": "range"}
        if attrs:
            default_attrs.update(attrs)
        super(RangeInput, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        if value is None: value = '1'
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(u'<input %s value="%s" />' % (flatatt(final_attrs),
                conditional_escape(force_unicode(value))))


class MakingForm(forms.ModelForm):
   class Meta:
       model = Making
       exclude = ('group',)
       widgets = {
        "rating": RangeInput(),
        "time": NumberInput(),
       }

"""
class MakingForm(forms.Form):
    time = forms.CharField(max_length=8, widget=NumberInput(), label="Aika (minuuttia)")
    temperature = forms.CharField(max_length=8, label="Lämpötila")
    comments = forms.CharField(widget=forms.widgets.Textarea(), label="Kommentit")
    rating = forms.CharField(max_length=1, widget=RangeInput(), label="Onnistuminen")
    in_progress = forms.BooleanField(label="Kesken")
"""

class RecipeForm(forms.Form):
    ingredient = forms.CharField(max_length=80, label="Ainesosa")

class DescrForm(forms.Form):
    description = forms.CharField(widget=forms.widgets.Textarea(), label="Kuvaus")
