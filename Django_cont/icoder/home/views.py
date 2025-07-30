from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from .models import UserProfile

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    
    if request.method == 'POST':
        # messages.error(request, 'Welcome to contact')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "please fill the form correctly")
        else:
            contact_obj = Contact(name=name, email=email, phone=phone, content=content)
            contact_obj.save()
            messages.success(request, "your message has been sucessfully send!")
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET.get('query', '')
    if query:
        allpostsTitle = Post.objects.filter(title__icontains=query)
        allpostscontent = Post.objects.filter(content__icontains=query)
        allposts = allpostsTitle.union(allpostscontent)
    
    elif len(query)>75:
        allposts = Post.objects.none()
    else:
        allposts = Post.objects.none() 
    if allposts.count() == 0:
        messages.warning(request, "no search result found")
    params = {'allposts': allposts, 'query': query}
    return render(request, 'home/search.html', params)
  
# authentication APIs
   
def handleSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        dob = request.POST['dob']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2'] 
        # profile_pic = request.FILES['profile_pic']
        profile_pic = request.FILES.get('profile_pic')  # safe
 
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another.")
            return redirect('home')
        
        elif len(username) >10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')
        
        elif not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')
        
        elif pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('home')
        
        elif len(phone) < 10:
            messages.error(request, "Phone number must be at least 10 characters long")
            return redirect('home')
        else:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()

            userprofile = UserProfile(user=myuser, phone=phone, address=address, dob=dob, profile_pic=profile_pic)
            userprofile.save()

            messages.success(request, "Your iCoder account has been successfully created.")
            return redirect('home')
    else:
        return HttpResponse('404 - not found')

def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginprofile_pic = request.FILES.get('loginprofile_pic',None)
        loginpass = request.POST['loginpass']
        user = authenticate(username = loginusername, password = loginpass, profile_pic=loginprofile_pic)
        if user is not None:
            login(request, user)
            messages.success(request, "success logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, please try again!")
            return redirect('home')
    return HttpResponse('404 - not found')


def handlelogout(request):
    # if request.method == 'POST':
            logout(request)
            messages.success(request, "success logged out")
            return redirect('home')
            
