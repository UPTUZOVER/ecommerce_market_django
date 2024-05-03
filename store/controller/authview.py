from django.shortcuts import render, redirect
from django.contrib import messages
from store.forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout

def register(request, *args, **kwargs):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Login to Continue")
            return redirect('/login')
    context = {'form': form}
    return render(request,"auth/register.html",context)



def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "you are already logged in")
        return redirect('/')
    else:
        
            
        if request.method == 'POST':
            name = request.POST.get("username")
            passwd  = request.POST.get("password")
            user = authenticate(request, username=name, password=passwd) 
            if user is not None:
                login(request, user)
                messages.success(request, "logged in Successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("/login")
        return render(request,"auth/login.html")


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "logged out successfully")
    return redirect("/")
    
        
























































