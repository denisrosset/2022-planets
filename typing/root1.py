"""
Root-finding solver based on Brent's method

See `<https://en.wikipedia.org/wiki/Brent%27s_method>`_
"""

from math import cos

x_rel_tol = 1e-12  # X relative tolerance
x_abs_tol = 1e-12  # X absolute tolerance
y_tol = 1e-12  # Y tolerance
verbose = True  # Whether to display progress

f = cos
a = 0.0  # first point that brackets the root
b = 3.0  # second point that brackets the root
fa = f(a)  # f(a)
fb = f(b)  # f(b)

assert fa * fb <= 0, "Root not bracketed"

if abs(fa) < abs(fb):
    # force abs(fa) >= abs(fb), make sure that b is the best root approximation known so far
    # and a is the contrapoint
    b, a = a, b
    fb, fa = fa, fb

c = a  # Previous iterate
fc = fa  # f(c)
d = a  # Iterate before the previous iterate
fd = fa  # f(d)
last_step = None
step = None
iter = 1  # Current iteration number (1-based)
converged = False  # Whether we have converged

if verbose:
    print("Iter\tx\t\tf(x)\t\tdelta(x)\tdelta(f(x))\tstep")
    dx = abs(a - b)
    dy = abs(fa - fb)
    print(f"{iter}\t{b:.3e}\t{fb:.3e}\t{dx:.3e}\t{dy:.3e}\t{last_step}")

while not converged:
    iter = iter + 1
    last_step = step
    if fa != fc and fb != fc:
        # perform a quadratic interpolation step
        # https://en.wikipedia.org/wiki/Inverse_quadratic_interpolation
        L0 = (a * fb * fc) / ((fa - fb) * (fa - fc))
        L1 = (b * fa * fc) / ((fb - fa) * (fb - fc))
        L2 = (c * fb * fa) / ((fc - fa) * (fc - fb))
        s = L0 + L1 + L2
        step = "quadratic"
    else:
        # perform a secant step
        s = b - fb * (b - a) / (fb - fa)
        step = "secant"
    perform_bisection = False
    if a <= b and not ((3 * a + b) / 4 <= s <= b):
        perform_bisection = True
    elif b <= a and not (b <= s <= (3 * a + b) / 4):
        perform_bisection = True
    elif last_step == "bisection" and abs(s - b) >= abs(b - c) / 2:
        perform_bisection = True
    elif last_step != "bisection" and abs(a - b) >= abs(c - d) / 2:
        perform_bisection = True
    elif last_step == "bisection" and abs(b - c) < x_abs_tol:
        perform_bisection = True
    elif last_step != "bisection" and abs(c - d) < x_abs_tol:
        perform_bisection = True
    if perform_bisection:
        # perform a bisection step
        s = min(a, b) + abs(b - a) / 2
        step = "bisection"
    fs = f(s)
    d = c
    c = b
    fc = fb
    # check which point to replace to maintain (a,b) have different signs
    if f(a) * f(s) < 0:
        b = s
        fb = fs
    else:
        a = s
        fa = fs
    # keep b as the best guess
    if abs(fa) < abs(fb):
        b, a = a, b
        fb, fa = fa, fb

    # Checks convergence
    if fb == 0:
        converged = True
        if verbose:
            print("Exact root found")
    x_delta = abs(a - b)
    if x_delta <= x_abs_tol:
        converged = True
        if verbose:
            print("Met x_abs_tol criterion")
    if x_delta / max(a, b) <= x_rel_tol:
        converged = True
        if verbose:
            print("Met x_rel_tol criterion")
    y_delta = abs(fb)
    if y_delta <= y_tol:
        converged = True
        if verbose:
            print("Met y_tol criterion")

    if verbose:
        dx = abs(a - b)
        dy = abs(fa - fb)
        print(f"{iter}\t{b:.3e}\t{fb:.3e}\t{dx:.3e}\t{dy:.3e}\t{last_step}")

print(f"The approximate root is {b}")
