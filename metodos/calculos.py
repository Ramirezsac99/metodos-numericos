from sympy import symbols, sympify, diff, factorial

x = symbols('x')

def newton_raphson(f_str, x0, tol=1e-6, max_iter=50):
    f = sympify(f_str)
    df = diff(f, x)
    iteraciones = []
    xi = float(x0)
    for i in range(max_iter):
        fxi = float(f.subs(x, xi))
        dfxi = float(df.subs(x, xi))
        if abs(dfxi) < 1e-12:
            break
        xi1 = xi - fxi / dfxi
        error = abs((xi1 - xi) / xi1) * 100 if xi1 != 0 else 0
        iteraciones.append({
            'i': i, 'xi': round(xi, 6), 'fxi': round(fxi, 6),
            'dfxi': round(dfxi, 6), 'xi1': round(xi1, 6), 'error': round(error, 5)
        })
        if abs(xi1 - xi) < tol:
            xi = xi1
            break
        xi = xi1
    return iteraciones, round(xi, 8)

def newton_raphson_mod(f_str, x0, m, tol=1e-6, max_iter=50):
    f = sympify(f_str)
    df = diff(f, x)
    iteraciones = []
    xi = float(x0)
    for i in range(max_iter):
        fxi = float(f.subs(x, xi))
        dfxi = float(df.subs(x, xi))
        if abs(dfxi) < 1e-12:
            break
        xi1 = xi - m * fxi / dfxi
        error = abs((xi1 - xi) / xi1) * 100 if xi1 != 0 else 0
        iteraciones.append({
            'i': i, 'xi': round(xi, 6), 'fxi': round(fxi, 6),
            'dfxi': round(dfxi, 6), 'xi1': round(xi1, 6), 'error': round(error, 5)
        })
        if abs(xi1 - xi) < tol:
            xi = xi1
            break
        xi = xi1
    return iteraciones, round(xi, 8)

def secante(f_str, x0, x1, tol=1e-6, max_iter=50):
    f = sympify(f_str)
    iteraciones = []
    a, b = float(x0), float(x1)
    for i in range(max_iter):
        fa, fb = float(f.subs(x, a)), float(f.subs(x, b))
        if abs(fb - fa) < 1e-12:
            break
        c = b - fb * (b - a) / (fb - fa)
        error = abs((c - b) / c) * 100 if c != 0 else 0
        iteraciones.append({
            'i': i, 'xi_1': round(a, 6), 'xi': round(b, 6),
            'fxi_1': round(fa, 6), 'fxi': round(fb, 6),
            'xi1': round(c, 6), 'error': round(error, 5)
        })
        if abs(c - b) < tol:
            b = c
            break
        a, b = b, c
    return iteraciones, round(b, 8)

def biseccion(f_str, a, b, tol=1e-6, max_iter=50):
    f = sympify(f_str)
    iteraciones = []
    a, b = float(a), float(b)
    for i in range(max_iter):
        c = (a + b) / 2
        fc = float(f.subs(x, c))
        fa = float(f.subs(x, a))
        error = abs((b - a) / 2)
        iteraciones.append({
            'i': i, 'a': round(a, 6), 'b': round(b, 6),
            'c': round(c, 6), 'fc': round(fc, 6), 'error': round(error, 6)
        })
        if abs(fc) < tol or error < tol:
            break
        if fa * fc < 0:
            b = c
        else:
            a = c
    return iteraciones, round(c, 8)

def taylor(f_str, x0, n):
    f = sympify(f_str)
    iteraciones = []
    aprox = 0
    for i in range(n + 1):
        derivada = diff(f, x, i)
        valor_deriv = derivada.subs(x, x0)
        termino = valor_deriv / factorial(i)
        aprox += termino * (x - x0)**i
        iteraciones.append({
            'n': i,
            'derivada': str(valor_deriv),
            'termino': str(termino),
            'aprox': str(aprox)
        })
    return iteraciones, str(aprox)