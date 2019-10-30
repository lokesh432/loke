from django.shortcuts import render
from . import forms

from django.views.generic import ListView
# Create your views here.


def Student_view(request):

    form=forms.UserModelForm()
    if request.method=='POST':
        form=forms.UserModelForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
    return render(request,'testapp/results.html',{'form':form})
'''
class LtView(ListView):
    template_name='testapp/results.html'
    model=forms.UserModelForm()
    def get(self,request):
        
'''
