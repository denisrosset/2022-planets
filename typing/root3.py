"""
Root-finding solver based on Brent's method

See `<https://en.wikipedia.org/wiki/Brent%27s_method>`_
"""
from __future__ import annotations

from math import cos
from typing import Callable, Optional, Tuple

x_rel_tol: float = 1e-12  #: X relative tolerance
x_abs_tol: float = 1e-12  #: X absolute tolerance
y_tol: float = 1e-12  #: Y tolerance
verbose: bool = True  #: Whether to display progress


def test_convergence(a: float, b: float, fb: float) -> Tuple[bool, Optional[str]]:
    """
    Checks convergence of a root finding method

    Args:
        a: Contrapoint
        b: Best guess
        fb: f(b)

    Returns:
        Whether the root finding converges to the specified tolerance and why
    """
    if fb == 0:
        return (True, "Exact root found")
    x_delta = abs(a - b)
    if x_delta <= x_abs_tol:
        return (True, "Met x_abs_tol criterion")
    if x_delta / max(a, b) <= x_rel_tol:
        return (True, "Met x_rel_tol criterion")
    y_delta = abs(fb)
    if y_delta <= y_tol:
        return (True, "Met y_tol criterion")
    return (False, None)


def inverse_quadratic_interpolation_step(
    a: float, b: float, c: float, fa: float, fb: float, fc: float
) -> float:
    """
    Computes an approximation for a zero of a 1D function from three function values

    Note:
        The values ``fa``, ``fb``, ``fc`` need all to be distinct.

    See `<https://en.wikipedia.org/wiki/Inverse_quadratic_interpolation>`_

    Args:
        a: First x coordinate
        b: Second x coordinate
        c: Third x coordinate
        fa: f(a)
        fb: f(b)
        fc: f(c)

    Returns:
        An approximation of the zero
    """
    L0 = (a * fb * fc) / ((fa - fb) * (fa - fc))
    L1 = (b * fa * fc) / ((fb - fa) * (fb - fc))
    L2 = (c * fb * fa) / ((fc - fa) * (fc - fb))
    return L0 + L1 + L2


def secant_step(a: float, b: float, fa: float, fb: float) -> float:
    """
    Computes an approximation for a zero of a 1D function from two function values

    Note:
        The values ``fa`` and ``fb`` need to have a different sign.

    Args:
        a: First x coordinate
        b: Second x coordinate
        fa: f(a)
        fb: f(b)

    Returns:
        An approximation of the zero
    """
    return b - fb * (b - a) / (fb - fa)


def bisection_step(a: float, b: float) -> float:
    """
    Computes an approximation for a zero of a 1D function from two function values

    Note:
        The values ``f(a)`` and ``f(b)`` (not needed in the code) need to have a different sign.

    Args:
        a: First x coordinate
        b: Second x coordinate

    Returns:
        An approximation of the zero
    """
    return min(a, b) + abs(b - a) / 2


def brent(f: Callable[[float], float], a: float, b: float) -> float:
    """
    Finds the root of a function using Brent's method, starting from an interval enclosing the zero

    Args:
        f: Function to find the root of
        a: First x coordinate enclosing the root
        b: Second x coordinate enclosing the root

    Returns:
        The approximate root
    """

    fa = f(a)  #: f(a)
    fb = f(b)  #: f(b)

    assert fa * fb <= 0, "Root not bracketed"

    if abs(fa) < abs(fb):
        # force abs(fa) >= abs(fb), make sure that b is the best root approximation known so far
        # and a is the contrapoint
        b, a = a, b
        fb, fa = fa, fb

    c = a  #: Previous iterate
    fc = fa  #: f(c)
    d = a  #: Iterate before the previous iterate
    fd = fa  #: f(d)
    last_step: Optional[str] = None
    step: Optional[str] = None
    iter = 1  #: Current iteration number (1-based)
    converged = None
    reason = None

    def print_state():
        """
        Prints information about an iteration
        """
        dx = abs(a - b)
        dy = abs(fa - fb)
        print(f"{iter}\t{b:.3e}\t{fb:.3e}\t{dx:.3e}\t{dy:.3e}\t{last_step}")

    if verbose:
        print("Iter\tx\t\tf(x)\t\tdelta(x)\tdelta(f(x))\tstep")
        print_state()

    while not converged:
        iter = iter + 1
        last_step = step
        if fa != fc and fb != fc:
            s = inverse_quadratic_interpolation_step(a, b, c, fa, fb, fc)
            step = "quadratic"
        else:
            s = secant_step(a, b, fa, fb)
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
            s = bisection_step(a, b)
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
        converged, reason = test_convergence(a, b, fb)
        if verbose:
            print_state()

    if verbose:
        assert reason is not None
        print(reason)

    return b


if __name__ == "__main__":
    print(brent(cos, 0.0, 3.0))
