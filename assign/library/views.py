from django.shortcuts import render, redirect

# Create your views here.
from .forms import *

from django.contrib import messages

# ============ADDING=================
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='/login/')
def publisherview(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # other fields, append more items
            post.user = request.user
            post.save()
            messages.success(request, "successfully saved")

        else:
            messages.error(request, "failed to save")

    form = PublisherForm
    return render(request, 'publisher.html', {'form': form})


def authorview(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "Good")
        else:
            messages.error(request, "Not good")

    form = AuthorForm
    return render(request, 'author.html', {'form': form})


def bookview(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Nice")
        else:
            messages.error(request, "Not acceptable")

    form = BookForm
    return render(request, 'book.html', {'form': form})


#==================FILTERING/SEACHING==================
# import your filters
from .filters import *
def publishersearchview(request):
    # fitst we get all publishers
    #allpublishers = Publisher.objects.all()
    allpublishers = Publisher.objects.filter(user_id=request.user)
    # django will create a form
    filteredpublishers = PublisherFilter(request.POST, queryset=allpublishers )

    # return to template for display, NB: in template use  'filteredpublishers'
    return render(request,'publishersearch.html',
                  {'filteredpublishers': filteredpublishers})





# ====================UPDATING RECORDS====================\
from django.shortcuts import get_object_or_404
def publisher_editview(request, pk):
    # get the publisher with pk
    post = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        # we load the form with published data based on primary key
        form = PublisherForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # other fields, append more items
            post.save()
            messages.success(request, "Updated!")
            return redirect('/psearch')

        else:
            messages.error(request, "Failed to Update")
    else:
       form = PublisherForm(instance=post)
    return render(request, 'publisher.html', {'form': form})


#==============DELETE==============
def publisher_delete(request, pk):
    Publisher.objects.get(pk=pk).delete()
    return redirect('/psearch')




#===============login =============
from django.contrib.auth import authenticate, login,logout
def loginuser(request):
    if request.method=="POST":
        # get username and password
        username = request.POST['username'];
        password = request.POST['password'];

        # authenticate
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/publisheradd')  # success
        else:
            return render(request, 'registration/login.html', {'msg':"Login Failed"})


    else:
        return render(request,'registration/login.html')


# ==========Logout====
def logoutuser(request):
    logout(request)
    return redirect("/login")



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user.is_staff = False
            return redirect('/publisheradd')
        else:
            raise forms.ValidationError('Looks like a username with '
                                        'that email or password already exists')
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})










