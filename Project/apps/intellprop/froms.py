from django import forms

# -*-coding:utf-8-*-

class UploadForm(forms.Form):
    """上传表单"""
    file = forms.FileField(
        widget= forms.ClearableFileInput(attrs={'multiple': True}),
        label= '选择文件...',
        help_text= '最大100M'
    )