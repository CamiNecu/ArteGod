from django.shortcuts import render,HttpResponse

def home(request):
    obras = [
        {
            'titulo': 'La joven de la perla',
            'autor': 'Johannes Vermeer',
            'imagen': 'https://i.blogs.es/03ac8b/la-joven-de-la-perla/1366_2000.jpeg'
        },
        {
            'titulo': 'Autorretrato de Vincent Van Gogh (1889)',
            'autor': 'Vincent van Gogh',
            'imagen': 'https://upload.wikimedia.org/wikipedia/commons/b/b2/Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project.jpg'
        },
    ]
    return render(request, "core/home.html", {'obras': obras})

def quienes(request):
    return render(request, "core/quienes.html")

def preguntasfre(request):
    return render(request, "core/preguntasfre.html")

def galimagenes(request):
    return render(request, "core/galimagenes.html")

# Create your views here.