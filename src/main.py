#!/usr/bin/python3

import sys
import argparse
from wterm import Wterm

def main() -> None:
    wterm = Wterm()

    parser = argparse.ArgumentParser(description="Wterm - A tool for thermodynamics")

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

    if action == "reversible":
        wterm.reversible(n, r, t, initial, final)
        sys.exit(1)

    elif action == "irreversible":
        wterm.irreversible(m, n, r, t, initial, final, steps)
        sys.exit(1)

    else:
        print("[X] Invalid Action. Wterm quitting...")

if __name__ == '__main__':
    main()