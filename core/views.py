from django.shortcuts import render,HttpResponse

def home(request):
    obras = [
        {
            'titulo': 'La joven de la perla',
            'autor': 'Johannes Vermeer',
            'imagen': 'core/assets/img/JovenPerla.jpeg'
        },
        {
            'titulo': 'Autorretrato de Vincent Van Gogh (1889)',
            'autor': 'Vincent van Gogh',
            'imagen': 'core/assets/img/VincentSelf1889.jpg'
        },
        {
            'titulo': 'Der Kuss',
            'autor': 'Gustav Klimt',
            'imagen': 'core/assets/img/TheKiss.jpg'
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