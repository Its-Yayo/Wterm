#!/usr/bin/python3

import sys
import argparse
import math

current_version = "v0.0.1"

class Wterm:
    def __init__(self) -> None:
        print(f"[x] Starting Wterm {current_version}")

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
            [str(int)] = The irreversible work
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
            [str(int)] = The reversible work
        """
        work: int = -(n * r * t) * math.log(initial_p / final_p)
        return "[X] Reversible Work is: " + str(work)

def main() -> None:
    parser = argparse.ArgumentParser(description="Wterm - A tool for thermodynamics")
    try:
        parser.add_argument("-w", "--work", dest='Work', help="[Reversible/Irreversible]")
        parser.add_argument("-m", dest="M", help="[Value for M]")
        parser.add_argument("-n", dest="N", required=True, help="[Value for N]")
        parser.add_argument("-r", dest="R", required=True, help="[Value for R]")
        parser.add_argument("-t", dest="T", required=True, help="[Value for T]")
        parser.add_argument("-i", "--initial", dest="Initial", required=True, help="[Value for initial pressure]")
        parser.add_argument("-f", "--final", dest="Final", required=True, help="[Value for final pressure]")
        parser.add_argument("-s", "--steps", dest="Steps", help="[Value for steps]")
    except Exception as e:
        print("[X] Your instruction has an error:", e)

    pass

if __name__ == '__main__':
    main()