from django.shortcuts import render, HttpResponse

# Create your views here.

def login(request):
    return render(request, 'login.html')

def recover(request):
    return render(request, 'recover.html')

def register(request):
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def watchlist(request):
    return render(request, 'watchlist.html')

def wallet(request):
    return render(request, 'wallet.html')

def about(request):
    return render(request, 'about.html')

def how_to_use(request):
    return render(request, 'how_to_use.html')

def contact(request):
    return render(request, 'contact.html')

def account(request):
    return render(request, 'account.html')