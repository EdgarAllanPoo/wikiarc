from django.shortcuts import render
from django.http import HttpResponse
from .forms import BlogForm, RawBlogForm
from .models import Blog

# Create your views here.

def blog_create_view(request):
    myform = RawBlogForm()
    if request.method == "POST":
        myform = RawBlogForm(request.POST)
        Blog.object.create(**my_form.cleaned_data)
    context = {
        "form" : myform
    }
    return render(request, "wikiblog/blog_create.html", context)


#def blog_create_view(request):
#    form = BlogForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#    context = {
#        'form' : form
#    }
#    return render(request, "wikiblog/blog_create.html", context)

def blog_detail_view(request):
    obj1 = Blog.objects.get(id = 1)
    context = {
        "title" : obj1.title,
        "body" : obj1.body,
    }
    return render(request, "wikiblog/index.html", context)

def home_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "Coba",
        "my_number" : 123,
    }
    return render(request, "wikiblog/index.html", my_context)
    # HttpResponse('<h1>hello world</h1>') #("<a href = './templates/wikiblog/index.html'></a>"

def page1_view(request):
    return render(request, "wikiblog/page1.html", {})

def page2_view(request):
    return render(request, "wikiblog/page2.html", {})

def page3_view(request):
    return render(request, "wikiblog/page3.html", {})

def page4_view(request):
    return render(request, "wikiblog/page4.html", {})

def page5_view(request):
    return render(request, "wikiblog/page5.html", {})

def create_page_view(request):
    form_blog_baru = RawBlogForm()
    if request.method == "POST":
        form_blog_baru = RawBlogForm(request.POST)
        Blog.object.create(**form_blog_baru.cleaned_data)
    context = {
        "title" : title,
        "title_minor" : title_minor,
        "body" : body,
        "author" : author
    }
    return render(request, "wikiblog/create.html", context)

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

#https://www.youtube.com/watch?v=obU8sw2A0MA
