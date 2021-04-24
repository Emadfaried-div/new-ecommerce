from django.shortcuts import render, redirect
from django.contrib.auth import logout,authenticate, login,update_session_auth_hash
from product.models import Category
from ecomapp.models import Setting
from django.contrib import messages
from .forms import SingUpForm, UserUpdateForm, ProfileUpdateForm
from UserApp.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def user_login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('ecomapp:home')
      
        else:
            messages.error(request, 'Invalid password or username!,Please try again.')
            # Return an 'invalid login' error message.

    category= Category.objects.all()
    setting = Setting.objects.get(id=1)
    context={"setting":setting,
                "category":category,
     
     }    
    return render(request,'user_login.html',context)




def user_logout(request):
    logout(request)
    return redirect('ecomapp:home')


def user_register(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            email=form.cleaned_data.get('email')
            user = authenticate(username=username, password=password_raw,email=email)
            login(request, user)
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="user_image/avatar.jpg"
            data.save()
            messages.warning(request, "Your Account has been created successfuly")
            return redirect('UserApp:user_login')
        else:
            form = SingUpForm()
    else:
        form = SingUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {'category': category,
               'setting': setting,
               'form': form}
    return render(request, 'user_register.html', context)



def usrprofiledata(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user= request.user
    profile=UserProfile.objects.get(user_id=current_user.id)

    context={"setting":setting,
                "category":category,
                "profile":profile,
     
     } 
    return render(request, 'userprofile.html', context)


@login_required
def user_update(request):
    if request.method=="POST":
        user_form= UserUpdateForm(request.POST, instance=request.user)
        profile_form= ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile )
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect("UserApp:userprofile")
    else:
        user_form= UserUpdateForm(instance=request.user)
        profile_form= ProfileUpdateForm(instance=request.user.userprofile )
        category = Category.objects.all()
        setting = Setting.objects.get(id=1)
        context={"setting":setting,
                "category":category,
        "user_form":user_form,
            "profile_form":profile_form,
            
            }
    return render(request, "userupdate.html", context)


@login_required
def user_password(request):
    if request.method == "POST":
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user= form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'your password was successfuly updated!.')
            return redirect("UserApp:userprofile")
        else:
            messages.error(request, 'Please correct the error below!.<br>')
            return redirect("UserApp:user_password")
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(id=1)
        form=PasswordChangeForm(request.user)
        context={"setting":setting,
                "category":category,
                "form":form,
                }
        return render(request,"userpasswordupdate.html",context)
    







