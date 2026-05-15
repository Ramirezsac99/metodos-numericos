from django.shortcuts import render
from .calculos import newton_raphson, newton_raphson_mod, secante, biseccion, taylor

def home(request):
    return render(request, 'metodos/home.html')

def vista_newton(request):
    resultado = None
    error_msg = None
    if request.method == 'POST':
        try:
            f = request.POST.get('funcion')
            x0 = float(request.POST.get('x0'))
            iteraciones, raiz = newton_raphson(f, x0)
            resultado = {'iteraciones': iteraciones, 'raiz': raiz, 'funcion': f}
        except Exception as e:
            error_msg = str(e)
    return render(request, 'metodos/newton.html', {'resultado': resultado, 'error': error_msg})

def vista_newton_mod(request):
    resultado = None
    error_msg = None
    if request.method == 'POST':
        try:
            f = request.POST.get('funcion')
            x0 = float(request.POST.get('x0'))
            m = int(request.POST.get('m'))
            iteraciones, raiz = newton_raphson_mod(f, x0, m)
            resultado = {'iteraciones': iteraciones, 'raiz': raiz, 'funcion': f}
        except Exception as e:
            error_msg = str(e)
    return render(request, 'metodos/newton_mod.html', {'resultado': resultado, 'error': error_msg})

def vista_secante(request):
    resultado = None
    error_msg = None
    if request.method == 'POST':
        try:
            f = request.POST.get('funcion')
            x0 = float(request.POST.get('x0'))
            x1 = float(request.POST.get('x1'))
            iteraciones, raiz = secante(f, x0, x1)
            resultado = {'iteraciones': iteraciones, 'raiz': raiz, 'funcion': f}
        except Exception as e:
            error_msg = str(e)
    return render(request, 'metodos/secante.html', {'resultado': resultado, 'error': error_msg})

def vista_biseccion(request):
    resultado = None
    error_msg = None
    if request.method == 'POST':
        try:
            f = request.POST.get('funcion')
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            iteraciones, raiz = biseccion(f, a, b)
            resultado = {'iteraciones': iteraciones, 'raiz': raiz, 'funcion': f}
        except Exception as e:
            error_msg = str(e)
    return render(request, 'metodos/biseccion.html', {'resultado': resultado, 'error': error_msg})

def vista_taylor(request):
    resultado = None
    error_msg = None
    if request.method == 'POST':
        try:
            f = request.POST.get('funcion')
            x0 = float(request.POST.get('x0'))
            n = int(request.POST.get('n'))
            iteraciones, polinomio = taylor(f, x0, n)
            resultado = {'iteraciones': iteraciones, 'polinomio': polinomio, 'funcion': f}
        except Exception as e:
            error_msg = str(e)
    return render(request, 'metodos/taylor.html', {'resultado': resultado, 'error': error_msg})