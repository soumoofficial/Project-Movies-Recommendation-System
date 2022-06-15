# Development Page
from django.shortcuts import render
from .models import Movie_list
from .models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'prs/index.html')
def home(request):
    return render(request,'prs/home.html')
def rs(request):
    return render(request,'prs/recommender.html')
def about(request):
    return render(request,'prs/about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<1 or len(phone)<10 or len(content)<10:
            messages.error(request,' Please fill up the details correctly')
        else :
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, ' Form Submitted Successfully')
    return render(request,'prs/contact.html',)
def show(request):
    if request.method == "POST":
        searched = request.POST['searched']
        m = []
        if searched == '':
            searched = "No search item"
        else :
            movies = Movie_list.objects.filter(Movie_name__contains=searched)
            print(movies)

            if not movies:
                searched = "Search Not Found"
            else:
                searched = "You searched for " + searched
                m = movies[0]
        return render(request,'prs/show.html',{'searched': searched,'movies':m})