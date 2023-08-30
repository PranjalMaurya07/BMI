from django.http import HttpResponse
from django.shortcuts import redirect,render
from myapp.models import *
from myapp.forms import createform

def index(request):
    result=0
    context={}
    try:
        if request.method == "POST":
            form_data=bmi.objects.all()
            weight=eval(request.POST.get('Weight'))
            height=eval(request.POST.get('Height'))
            result=round(10000*(weight/(height*height)),2)
            if ((result > 25 and result < 29.9) or (result > 29.9) or (result < 18.5) or (result > 18.5 and result < 25)):
                w1=round((18.5*height*height)/10000,2)
                w2=round((25*height*height)/10000,2)
            else:
                pass
            context={
                'height':height,
                'weight':weight,
                'w1':w1,
                'w2':w2,
                'output':result
            }
    except:
        pass
    print(result)
    return render(request,'index.html',context)
        
