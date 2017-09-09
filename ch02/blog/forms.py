#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    @version: 1.0
    @author : Carrot
    @time   : 2017/9/9 17:32
"""

from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 100)
    email = forms.EmailField(required=False, label = "Your e-mail address")
    message = forms.CharField(widget = forms.Textarea)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
