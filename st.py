from shlex import *
import os
import sys


program = 'write "Hello Universe and the skies"'


def main() -> int:
    for p, op in enumerate(program):
        print("HAHAHAHAHAHAH")
        print(f"pang {p + 1} beses nabilang ang aking pagiging abnoy")
        if program[p] == 'write':
            print(program[p+1])
        # print(op)

if __name__ == '__main__':
    main()