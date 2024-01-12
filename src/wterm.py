#!/usr/bin/python3

import math

# Not released yet but soon :)
CURRENT = "v0.0.1"

# TODO: check operations and values arg doc 
class Wterm:
    def __init__(self) -> None:
        print(f"[x] Starting Wterm {CURRENT}")

    def irreversible(self, m, n, r, t, initial_p, final_p, steps) -> str:
        """ Calculates the isoterm irreversible process
        Args:
            m: [int] =
            n: [int] =
            r: [int] =
            t: [int] =
            initial_p: [int] =
            final_p: [int] =
            steps: [int] =
        Returns:
            [str(int)] = Irreversible work
        """
        delta_p = (final_p - initial_p) / m
        values = True

        work: int = 0

        while values:
            for j in range(0, steps + 1):
                initial_press = delta_p / (initial_p + (j * delta_p))
                work = (n * r * t) * initial_press + work
            return "[X] Irreversible Work is: " + str(work)

    def reversible(self, n, r, t, initial_p, final_p) -> str:
        """ Calculates the isoterm reversible process
        Args:
            n: [int] =
            r: [int] =
            t: [int] =
            initial_p: [int] =
            final_p: [int] =
        Returns:
            [str(int)] = Reversible work
        """
        work: int = -(n * r * t) * math.log(initial_p / final_p)
        return "[X] Reversible Work is: " + str(work)