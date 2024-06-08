from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import Userss
from django.contrib import messages
from .forms import UserForm
import pdfkit
from django.template import loader
path_wkthmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)






def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = UserForm()
        profiles = Userss.objects.all()
        message=messages.success(request,"Verilenler bazasina qeyd edildi")
    return render(request, 'main.html', {'form': form, 'profiles': profiles})

def profiles(request):
    users=Userss.objects.all()
    return render(request,'users.html', {'users': users})



def detail(request, id):
    user = Userss.objects.get(id=id)
    template = loader.get_template("template.html")
    html = template.render({"user": user})
    options = {"page-size": "Letter","encoding": "UTF-8",}
    pdf = pdfkit.from_string(html, False, options,configuration=config)
    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="download.pdf"'
    return response












