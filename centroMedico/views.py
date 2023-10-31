from atexit import register
from django.shortcuts import redirect, render
from .forms import RegistroForm  # Asegúrate de importar el formulario personalizado

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Inicia sesión automáticamente al usuario
            register(request, user)
            return redirect('index')  # Redirige a la página deseada después del registro
    else:
        form = RegistroForm()

    return render(request, 'templates/registro.html', {'form': form})

