from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "course_List/index.html")
def personalized_main(request, name):
    return render(request, "course_List/pers.html", {
        "name": name.capitalize()
    })