from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context={'page':'home'}
    pepoles = [
        {'name': 'mahadi', 'age': 16},
        {'name': 'likon', 'age': 30},
        {'name': 'shakil', 'age': 30},
    ]
    vegetables=['pumpkin','tomatow','ptatow']

    text="""Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ab placeat sit quidem nihil alias ipsa quas, officia voluptatum doloremque! Nesciunt illum iure enim, autem alias ad molestiae ab accusamus? Quisquam.
"""

    return render(request,"home/index.html", context={'page':'Home','vegetables':vegetables,'pepoles': pepoles,'text':text})


def about(request):
    context={'page':'about'}

    return render(request, "home/about.html",context)

def contact(request):
    context={'page':'contact'}

    return render(request, "home/contact.html",context)

def success_page(request):
    return HttpResponse("This is success page 2")
