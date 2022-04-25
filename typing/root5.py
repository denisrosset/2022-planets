"""
Root-finding solver based on Brent's method

See `<https://en.wikipedia.org/wiki/Brent%27s_method>`_
"""
from __future__ import annotations

from dataclasses import dataclass
from math import cos
from typing import Callable, Literal, Optional, Tuple, Union


@dataclass(frozen=True)
class Settings:
    """
    Settings for the root-finding algorithm
    """

    x_rel_tol: float = 1e-12  #: X relative tolerance
    x_abs_tol: float = 1e-12  #: X absolute tolerance
    y_tol: float = 1e-12  #: Y tolerance
    verbose: bool = False  #: Whether to display progress

    def __post_init__(self) -> None:
        """
        Verifies sanity of parameters
        """
        assert self.x_rel_tol >= 0
        assert self.x_abs_tol >= 0
        assert self.y_tol >= 0
        assert (
            self.x_rel_tol > 0 or self.x_abs_tol > 0 or self.y_tol > 0
        ), "At least one convergence criteria must be set"

    def converged(self, a: float, b: float, fb: float) -> Tuple[bool, Optional[str]]:
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
        if x_delta <= self.x_abs_tol:
            return (True, "Met x_abs_tol criterion")
        if x_delta / max(a, b) <= self.x_rel_tol:
            return (True, "Met x_rel_tol criterion")
        y_delta = abs(fb)
        if y_delta <= self.y_tol:
            return (True, "Met y_tol criterion")
        return (False, None)

    @staticmethod
    def default_verbose() -> Settings:
        """
        Returns default verbose settings
        """
        return Settings(verbose=True)


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


@dataclass(frozen=True)
class BrentState:
    """
    State for Brent's method

    Note:
        We have the following invariants.

        - ``fa = f(a)`` and ``fb = f(b)`` have opposite signs

        - ``abs(fb) <= abs(fa)`` so that ``b`` is the best guess
    """

    a: float  #: Contrapoint
    b: float  #: Current iterate, best root approximation known so far
    c: float  #: Previous iterate
    d: float  #: Iterate before the previous iterate
    fa: float  #: f(a)
    fb: float  #: f(b)
    fc: float  #: f(c)
    last_step: Optional[
        Union[Literal["quadratic"], Literal["secant"], Literal["bisection"]]
    ]  #: Type of previous step
    iter: int  #: Current iteration number (1-based)

    @staticmethod
    def make(f: Callable[[float], float], a: float, b: float) -> BrentState:
        """
        Initializes a state from an interval that brackets a root of the given function

        Args:
            f: Function to find the root of
            a: First x coordinate
            b: Second x coordinate

        Returns:
            The initial state
        """
        fa = f(a)
        fb = f(b)
        # check the first invariant
        assert fa * fb <= 0, "Root not bracketed"
        if abs(fa) < abs(fb):
            # force the second invariant
            b, a = a, b
            fb, fa = fa, fb
        c, fc = a, fa
        d, fd = a, fa
        return BrentState(a=a, b=b, c=c, d=d, fa=fa, fb=fb, fc=fc, last_step=None, iter=1)


def brent_step(f: Callable[[float], float], state: BrentState, delta: float) -> BrentState:
    """
    Performs a step of Brent's method

    Args:
        f: Function to find the root of
        state: Previous state
        delta: x absolute tolerance

    Returns:
        New state
    """
    a, b, c, d = state.a, state.b, state.c, state.d
    fa, fb, fc = state.fa, state.fb, state.fc
    last_step = state.last_step
    iter = state.iter
    step: Optional[Union[Literal["quadratic"], Literal["secant"], Literal["bisection"]]] = None
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
    elif last_step == "bisection" and abs(b - c) < delta:
        perform_bisection = True
    elif last_step != "bisection" and abs(c - d) < delta:
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
    return BrentState(a=a, b=b, c=c, d=d, fa=fa, fb=fb, fc=fc, last_step=step, iter=iter + 1)


def brent(
    f: Callable[[float], float], a: float, b: float, settings: Settings = Settings()
) -> float:
    """
    Finds the root of a function using Brent's method, starting from an interval enclosing the zero

    Args:
        f: Function to find the root of
        a: First x coordinate enclosing the root
        b: Second x coordinate enclosing the root
        settings: Algorithm settings

    Returns:
        The approximate root
    """
    state = BrentState.make(f, a, b)
    converged = None
    reason = None

    def print_state(s: BrentState):
        """
        Prints information about an iteration
        """
        dx = abs(s.a - s.b)
        dy = abs(s.fa - s.fb)
        ls: Optional[str] = s.last_step
        if ls is None:
            ls = ""
        print(f"{s.iter}\t{s.b:.3e}\t{s.fb:.3e}\t{dx:.3e}\t{dy:.3e}\t{ls}")

    if settings.verbose:
        print("Iter\tx\t\tf(x)\t\tdelta(x)\tdelta(f(x))\tstep")
        print_state(state)

    while not converged:
        state = brent_step(f, state, settings.x_abs_tol)
        converged, reason = settings.converged(state.a, state.b, state.fb)
        if settings.verbose:
            print_state(state)

    if settings.verbose:
        assert reason is not None
        print(reason)

    return state.b


if __name__ == "__main__":
    print(brent(cos, 0.0, 3.0, Settings.default_verbose()))
