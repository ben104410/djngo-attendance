from django.shortcuts import render

def home(request):
    context= {
        'title': 'Home',
    }
    
    
    return render(request, 'home.html', context)

def about(request):
    """
    Renders the about page.
    """
    context = {
        'title': 'About Us',
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'title': 'Contact Us',
    }
    return render(request, 'contact.html', context)