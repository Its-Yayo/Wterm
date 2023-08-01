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
    global action
    wterm = Wterm()

    parser = argparse.ArgumentParser(description="Wterm - A tool for thermodynamics")

    try:
        parser.add_argument("-a", "--action", dest='action', help="[Reversible/Irreversible]")
        parser.add_argument("-m", dest="m", help="[Value for M]")
        parser.add_argument("-n", dest="n", required=True, help="[Value for N]")
        parser.add_argument("-r", dest="r", required=True, help="[Value for R]")
        parser.add_argument("-t", dest="t", required=True, help="[Value for T]")
        parser.add_argument("-i", "--initial", dest="initial", required=True, help="[Value for initial pressure]")
        parser.add_argument("-f", "--final", dest="final", required=True, help="[Value for final pressure]")
        parser.add_argument("-s", "--steps", dest="steps", help="[Value for steps]")

        args = parser.parse_args()
        action = args.action.lower()

        m = args.m
        n = args.n
        r = args.r
        t = args.t
        initial = args.initial
        final = args.final
        steps = args.steps

    except Exception as e:
        print("[X] Your instruction has an error:", e)

    if action == "Reversible":
        wterm.reversible(n, r, t, initial, final)
        sys.exit(1)

    elif action == "Irreversible":
        wterm.irreversible(m, n, r, t, initial, final, steps)
        sys.exit(1)

    else:
        print("[X] Invalid Action. Wterm quitting...")


if __name__ == '__main__':
    main()
