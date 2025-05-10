from django import forms

class CourseForm(forms.Form):
    course_name = forms.CharField(label='ゴルフ場入力')