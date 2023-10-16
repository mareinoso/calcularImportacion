from django.shortcuts import render, redirect
from .models import Importacion
from .forms import AgregarForm

# Create your views here.
def importacionData(request):
    importados = Importacion.objects.all()
    data = {'importados' : importados}
    return render(request, 'importaciones.html', data) 

def agregarImportacion(request):
    if request.method == 'POST':
        form = AgregarForm(request.POST)
        if not form.is_valid():
            return render(request, 'agregar_importacion.html', {'form': form})
        form.save()
        return redirect('/importaciones/')
        
    else:
        form = AgregarForm()
        return render(request, 'agregar_importacion.html', {'form': form})