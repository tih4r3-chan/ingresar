from django.shortcuts import render
from .forms import RegistroForm  # Asegúrate de importar el formulario personalizado

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Inicia sesión automáticamente al usuario
            ingreso(request, user)
            return redirect('lista_ingresos')  # Redirige a la página deseada después del registro
    else:
        form = RegistroForm()

    return render(request, 'templates/registro.html', {'form': form})

