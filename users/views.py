from django.contrib.messages.api import add_message
from django.shortcuts import redirect, render
from .models import Profile,Message
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import CustomUserCreationForm, ProfileForm, MessageForm, ApplicationForm
from.utils import searchProfiles, paginateProfiles
# Create your views here.
from .decorators import admin_only, allowed_users, unauthenticated_user

@unauthenticated_user
def loginUser(request):
    page= 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method =="POST":
        username= request.POST['username'].lower()
        password= request.POST['password']
        try:
            user= User.objects.get(username=username)

        except:
            messages.error(request, "username doesnt exist")
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if (user.profile.has_applied and user.profile.is_approved):
                return redirect(request.GET['next'] if 'next' in request.GET else 'account' )

            elif user.profile.has_applied and user.profile.is_approved == False : 
                    return render(request,'users/account_pending_approval.html')
            else:
                return redirect('edit_account')

        else:
            messages.error(request,"username or password is incorrect")
    context={
        "page":page
    }
    return render(request, 'users/login_register.html', context)

def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('login')

@unauthenticated_user
def registerUser(request):
    page= 'register'
    form = CustomUserCreationForm()
    if request.method =="POST":
        print(request.POST)
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            # changing username to lower case
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account was created")
            login(request,user)
            return redirect('edit_account')
        else:
            messages.error(request, "An error occured during registration")
    context={
            "form":form,
            "page": page
        }
    return render(request, 'users/login_register.html', context)


def profiles(request):
    profiles,search_query= searchProfiles(request)
    custom_range, profiles= paginateProfiles(request,profiles,1)
    context={
        "profiles":profiles,
        "search_query":search_query,
        "custom_range":custom_range
    }
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):

    profile= Profile.objects.get(id=pk)
    context ={
        "profile": profile,
    }
    return render(request, 'users/user-profile.html', context)


@login_required(login_url="login")
def userAccount(request):

    profile= request.user.profile
    projects= profile.project_set.all()
    context={
        "profile":profile,
        "projects":projects,
    }
    return render(request,'users/account.html', context)


@login_required(login_url="login")
def editAccount(request):
    profile= request.user.profile
    form= ProfileForm(instance=profile)
    if request.method == 'POST':
        form= ProfileForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            if profile.has_applied and profile.is_approved:
                profile.save()
                return redirect('account')
            else:
                    profile.has_applied= True
                    profile.save()
                    return redirect("pending_approval")

            

    context={
        "form":form
    }
    return render(request, 'users/profile_form.html', context)


# def createSkill(request):
#     profile= request.user.profile
#     if request.method=="POST":
#         form= SkillForm(request.POST)
#         if form.is_valid():
#             skill=form.save(commit=False)
#             skill.owner= profile
#             skill.save()
#             messages.success(request, "Skill was Added Successfuly")
#             return redirect('account')


#     context={
#         "form":form
#     }
#     return render(request, 'users/skill_form.html', context)

# def updateSkill(request, pk):
#     profile= request.user.profile
#     skill= profile.skill_set.get(id=pk)
#     form = SkillForm(instance=skill)
#     if request.method=="POST":
#         form= SkillForm(request.POST, instance=skill)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Skill was updated successfuly")

#             return redirect('account')


    

@login_required(login_url='login')
def deleteSkill(request, pk):
    profile= request.user.profile
    obj= profile.skill_set.get(id=pk)
    if request.method=="POST":
        obj.delete()
        messages.success(request, 'Skill was deleted successfuly')
        return redirect('account')
    context={
        "obj":obj
    }
    return render(request, 'delete_template.html', context)

@login_required(login_url='login')
def inbox(request):
    profile= request.user.profile
    messagesRequest= profile.messages.all()
    unreadCount= messagesRequest.filter(is_read=False).count()
    context={
        'messagesRequest':messagesRequest,
        "unreadCount":unreadCount
    }
    return render(request,'users/inbox.html', context )
@login_required(login_url='login')

def applications(request):
    profile= request.user.profile
    messagesRequest= profile.application.all()
    unreadCount= messagesRequest.filter(is_read=False).count()
    context={
        'messagesRequest':messagesRequest,
        "unreadCount":unreadCount
    }
    return render(request,'users/applications.html', context )

@login_required(login_url='login')
def viewMessage(request, pk):

    profile= request.user.profile
    messageRequest= profile.messages.get(id=pk)
    if messageRequest.is_read == False:
        messageRequest.is_read= True
        messageRequest.save()
    context={
        'messageRequest': messageRequest
    }
    return render(request, "users/message.html", context)
def viewApplication(request, pk):
    profile= request.user.profile
    messageRequest= profile.application.get(id=pk)
    if messageRequest.is_read == False:
        messageRequest.is_read= True
        messageRequest.save()
    context={
        'messageRequest': messageRequest
    }
    return render(request, "users/application.html", context)

def createMessage(request, pk):
    recipient= Profile.objects.get(id=pk)
    form = MessageForm()
    try:
        sender= request.user.profile
    except:
        sender= None

    if request.method =="POST":
        form= MessageForm(request.POST)
        if form.is_valid():
            message= form.save(commit=False)
            message.sender= sender
            message.recipient= recipient
            if sender:
                message.name= sender.name
                message.email= sender.email
            message.save()

            messages.success(request, "Your message was successfully sent ")

            return redirect('user_profile', pk=recipient.id)
    context={
        "form":form,
        "recipient": recipient

    }
    return render(request, 'users/message_form.html', context)

def applicationMessage(request, pk):
    recipient= Profile.objects.get(id=pk)
    form = ApplicationForm()
    try:
        sender= request.user.profile
    except:
        sender= None

    if request.method =="POST":
        form= ApplicationForm(request.POST)
        if form.is_valid():
            message= form.save(commit=False)
            message.sender= sender
            message.recipient= recipient
            if sender:
                message.name= sender.name
                message.email= sender.email
            message.save()

            messages.success(request, "Your Application was successfully sent ")

            return redirect('user_profile', pk=recipient.id)
    context={
        "form":form,
        "recipient": recipient

    }
    return render(request, 'users/application_form.html', context)


@login_required(login_url='login')
def AccountPendingApproval(request):

    return render(request, 'users/account_pending_approval.html')



#admin account
@login_required(login_url='login')
@admin_only
def adminAccount(request):
    agency= Profile.objects.all()
    agency_pending_approval= agency.filter(is_approved=False)
    total_pending_approval=agency_pending_approval.count()
    approved_agencies= agency.filter(is_approved=True, is_suspended = False)
    total_approved_agencies= approved_agencies.count()
    suspended_agencies= agency.filter(is_suspended=True)
    total_suspended_agencies= suspended_agencies.count()


    context={
        'agency_pending_approval':agency_pending_approval,
        'total_pending_approval' :total_pending_approval,
        'total_approved_agencies':total_approved_agencies,
        'approved_agencies':approved_agencies,
        "suspended_agencies":suspended_agencies,
        'total_suspended_agencies':total_suspended_agencies
    }

    return render(request, 'users/admin/admin_dashboard.html', context)

@login_required(login_url='login')
@admin_only
def approveAgency(request, pk):
    profile= Profile.objects.get(id=pk)
    profile.is_approved=True
    profile.save()
    return redirect('admin_dashboard')


@login_required(login_url='login')
@admin_only
def suspendAgency(request, pk):
    profile= Profile.objects.get(id=pk)
    profile.is_suspended=True
    profile.save()
    return redirect('admin_dashboard')


@login_required(login_url='login')
@admin_only
def reapproveAgency(request, pk):
    profile= Profile.objects.get(id=pk)
    profile.is_suspended=False
    profile.save()
    return redirect('admin_dashboard')


@login_required(login_url='login')
@admin_only
def viewapplication(request, pk):
    profile= request.user.profile
    agency_application= Profile.objects.get(id=pk)

    context={
        "agency_application": agency_application
    }
    return render(request, "users/admin/agency_application.html", context)
