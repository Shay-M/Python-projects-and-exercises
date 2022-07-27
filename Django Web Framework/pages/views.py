from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# args and **kwargs are mostly used in function definitions.
#  args and **kwargs allow you to pass an unspecified number of arguments to
# a function, so when writing the function definition, you do not need to know
# how many arguments will be passed to your function. *args is used to send a
# non-keyworded variable length argument list to the function. Here’s an example
#  to help you get a clear

# https://book.pythontips.com/en/latest/args_and_kwargs.html


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    # return HttpResponse("<h1>hii</h1>")
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_title": "About from my_title",
        "my_list": ['A', 'B', 'C']
    }
    return render(request, "about.html", my_context)
