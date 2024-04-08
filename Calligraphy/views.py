from .models import CalligraphyStyle, Artwork  # might be an issue here. CalligraphyStyle is it being used?
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
# views.py


def authenticate_user(request):
    """
        Authenticates the user based on the provided username and password.

        Redirects to the login page if authentication fails.
        Redirects to the display screen if authentication succeeds.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponseRedirect: Redirects to the appropriate page.
        """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(
            reverse('Calligraphy:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('Calligraphy:display_screen')
        )

# Sign up new users
def signup_view(request):
    """
    Helps you create a new account.

    If you fill out a form correctly, you get a new account and can start using it.

    Args:
        request (HttpRequest): The thing you send when you want to make a new account.

    Returns:
        HttpResponse: It gives you a form to fill out or sends you somewhere else.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('Calligraphy:display_screen'))  # Replace 'home' with the name of your home page URL
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# upon successful login user will be redirected to display_screen (home page)
@login_required     # this is my show user example
def display_screen(request):
    """
    Shows you the main page of the app.

    If you haven't logged in, it takes you back to the login page.

    Args:
        request (HttpRequest): The thing you send when you want to see the main page.

    Returns:
        HttpResponse: It shows you the main page if you're logged in, otherwise it sends you to login first.
    """
    context = {'user': request.user}
    return render(request, 'Calligraphy/displayScreen.html', context)


def landing_page(request):
    """
    Shows you the first page of the app.

    Args:
        request (HttpRequest): The thing you send when you start the app.

    Returns:
        HttpResponse: It shows you the first page of the app.
    """
    return render(request, 'Calligraphy/landing_page.html')

# about calligrpahy page
def about_calligraphy(request):
    """
    Tells you a little about writing beautifully.

    Args:
        request (HttpRequest): The thing you send when you want to learn about writing beautifully.

    Returns:
        HttpResponse: It tells you a little about writing beautifully.
    """
    context = {}
    return render(request, 'Calligraphy/about_calligraphy.html', context)

# style page
def styles_list(request):
    """
    Shows you a list of different ways to write beautifully.

    Args:
        request (HttpRequest): The thing you send when you want to see different ways of writing beautifully.

    Returns:
        HttpResponse: It shows you a list of different ways to write beautifully.
    """
    #context = {}
    styles = CalligraphyStyle.objects.all()
    return render(request, 'Calligraphy/styles_list.html',{'styles': styles}) #context)

# types of artwork page
def artwork_list(request): #style_id=None):
    """
    Shows you a list of beautiful drawings.

    Args:
        request (HttpRequest): The thing you send when you want to see beautiful drawings.

    Returns:
        HttpResponse: It shows you a list of beautiful drawings.
    """
    context={}
    return render(request, 'Calligraphy/artwork_list.html', context)#{'artworks': artworks})

# logout option
def login_user(request):
    """
    Shows you a page to put in your username and password.

    Args:
        request (HttpRequest): The thing you send when you want to login.

    Returns:
        HttpResponse: It shows you a page where you can put in your username and password.
    """
    return render(request, 'login.html')


def logout_user(request):
    """
    Shows you a page to say goodbye.

    Args:
        request (HttpRequest): The thing you send when you want to logout.

    Returns:
        HttpResponse: It shows you a page to say goodbye.
    """
    # Logout logic here if needed
    return render(request, 'logout.html')
# Create your views here.
