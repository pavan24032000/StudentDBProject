from django.shortcuts import render
from StudentDBApp.models import Student


#Create your views here.
def studentview(request):
    studentlist = Student.objects.order_by('marks')
    dict1={'studentlist':studentlist}
    return render(request,'StudentDBApp/students.html',context=dict1);

from StudentDBApp import forms
from StudentDBApp.forms import StudentForm
#Create your views here.
def studentinputview(request):
    formsObj=forms.StudentForm()
    dict1={'form1':formsObj}
    return render(request,'StudentDBApp/input.html',context=dict1)


import time;
from StudentDBApp import forms;
def studentinputverifyview(request):
    if request.method == 'POST':
        formsObj = forms.StudentForm(request.POST);
        if formsObj.is_valid():
            print('Form-Request validation success and printing data');
            time.sleep(5)
            print('Name:', formsObj.cleaned_data['name'])
            print('Marks:', formsObj.cleaned_data['marks'])
            formsObj = forms.StudentForm();     #empty-form
    dict1 = {'form1': formsObj,'msg':'Data Submitted successfully...(Enter another data)'}
    return render(request, 'StudentDBApp/input.html',context=dict1);




