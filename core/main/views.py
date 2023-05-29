from django.shortcuts import render, redirect
from .models import HomeBanner, SiteTitle
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model
from users.models import CustomUser
from .models import Products, ProductsCategory, HeppyCustomers, HomeBanner, Banners, OurBackground, TeamMembers
from .models import Services, AboutSixtennClothing

def index(request):
    banner_list = HomeBanner.objects.all()
    latest_products = Products.objects.all()[:6]
    latest_products = latest_products[::-1]
    
    about_sixtenn_clothing = AboutSixtennClothing.objects.all()[0]
    
    if request.method == "POST":
        star_1 = request.POST.get("star_1")
        star_2 = request.POST.get("star_2")
        star_3 = request.POST.get("star_3")
        star_4 = request.POST.get("star_4")
        star_5 = request.POST.get("star_5")
        
        my_id = next((star for star in [star_1, star_2, star_3, star_4, star_5] if star), None)
        user = CustomUser.objects.get(username = request.user.username)
        
        try:
            prod = Products.objects.get(id = int(my_id))
        except:
            return redirect("login_register")
            
        if user in prod.reviews.all():
            prod.reviews.remove(user)
        else:
            prod.reviews.add(user)
            
            
    
    return render(request, "main/index.html", context = {
        "page": "home",
        "banner_list": banner_list,
        "sitetitle": SiteTitle.objects.all()[0],
        'latest_products': latest_products,
        "about_sixtenn_clothing": about_sixtenn_clothing,
    })
    
def products(request):
    prod_category = ProductsCategory.objects.all()
    prods = Products.objects.all()
    
    banner = Banners.objects.filter(page__name = "Products")[0]
    
    if request.method == "POST":
        star_1 = request.POST.get("star_1")
        star_2 = request.POST.get("star_2")
        star_3 = request.POST.get("star_3")
        star_4 = request.POST.get("star_4")
        star_5 = request.POST.get("star_5")
        
        my_id = next((star for star in [star_1, star_2, star_3, star_4, star_5] if star), None)
        user = CustomUser.objects.get(username = request.user.username)
        
        try:
            prod = Products.objects.get(id = int(my_id))
        except:
            return redirect("login_register")
            
        if user in prod.reviews.all():
            prod.reviews.remove(user)
        else:
            prod.reviews.add(user)
            
    return render(request, "main/products.html", context = {
        "page": "products",
        "sitetitle": SiteTitle.objects.all()[0],
        "prod_category": prod_category,
        "prods": prods,
        "banner": banner
        
    })
    
def about(request):
    happy_customers_list = HeppyCustomers.objects.all()
    banner = Banners.objects.filter(page__name = "About")[0]
    our_bg = OurBackground.objects.all()[0]
    team_members = TeamMembers.objects.all()
    serices = Services.objects.all()[:3:]
    
    
    return render(request, "main/about.html", context = {
        "page": "about",
        "isAboutOrContact": True,
        "happy_customers_list": happy_customers_list,
        "sitetitle": SiteTitle.objects.all()[0],
        "banner": banner,
        "our_bg": our_bg,
        "team_members": team_members,
        "serices": serices
    })


def login_register(request):
    logout(request)
    banner = Banners.objects.filter(page__name = "LogReg")[0]
    if request.method == "POST":
        
        if request.POST.get("btn") == "login":
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            if any(i in username+" "+password for i in "=-'\""):
                return redirect("login_register")
            
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("index")
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                messages.error(request,"Invalid username or password.")

        elif request.POST.get("btn") == "register":
            
            username = request.POST.get("username")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            user_email = request.POST.get("email")
            
            if any(i in username+" "+password1+" "+password2+" "+user_email for i in "=-'\""):
                return redirect("login_register")
            
            
            form = NewUserForm(request.POST)

            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activation link has been sent to your email id'
                message = render_to_string('main/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')

                email = EmailMessage(
                    mail_subject,
                    message,
                    to=[to_email],
                    from_email='Lamajo <your_email@example.com>', 
                )

                email.content_subtype = 'html'
                email.send()

                return render(request, "main/pls_check_email.html", context={
                    "reg_form": form,
                    "user_email": user_email, 
                    })
 
    reg_form = NewUserForm()       
    
    return render(request, "main/login_register.html", context = {
        "reg_form": reg_form,
        "page": "loginregister",
        "sitetitle": SiteTitle.objects.all()[0],
        "banner": banner
    })
    
    


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return render(request, "main/verif_email.html") 
    else:  
        return render(request, "main/invalid_link.html")  


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login_register")

    