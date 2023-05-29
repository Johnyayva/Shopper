from django.shortcuts import render, redirect
from main.models import SiteTitle, HeppyCustomers, Banners
from .models import AboutOfice, Accordion, ContactUs
from .forms import ContacUsModelForm

def contact(request):
    if request.user.is_authenticated:
        return redirect("login_register")
    banner = Banners.objects.filter(page__name = "Contact")[0]
    about_ofice = AboutOfice.objects.all()[0]
    accordion_list = Accordion.objects.all()
    happy_customers_list = HeppyCustomers.objects.all()

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        if any(i in full_name+" "+email+" "+subject+" "+message for i in "=-'\""):
            return redirect("login_register")
            
        form = ContacUsModelForm(request.POST)
        
        if form.is_valid():
            ContactUs.objects.create(**form.cleaned_data)
            return redirect("contact")
    else:
        form = ContacUsModelForm()
        
    
    return render(request, "main/contact.html", context = {
        "page": "contact",
        "isAboutOrContact": True,
        "sitetitle": SiteTitle.objects.all()[0],
        "about_ofice": about_ofice,
        "accordion_list": accordion_list,
        "form": form,
        "happy_customers_list": happy_customers_list,
        "banner": banner
})
