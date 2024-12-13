# %% imports
import sys

sys.path.append("../..")
from fractions import Fraction
from pathlib import Path

import numpy

from util import timed

# %% read files
test_txt = Path("test.txt").read_text()
test_lines = test_txt.splitlines()
print(f"read {len((test_lines))} test lines")
input_txt = Path("input.txt").read_text()
input_lines = input_txt.splitlines()
print(f"read {len((input_lines))} lines")


# %% read functions
def xy(s):
    s = s[s.find(":") + 2 :]
    x, y = s.split()
    x = int(x[1:-1].strip("="))
    y = int(y[1:].strip("="))
    return x, y


def parse_input(txt: str):
    lines = [l.split("\n") for l in txt.strip().split("\n\n")]
    ans = []
    for a, b, p in lines:
        ans.append(
            {
                "A": xy(a),
                "B": xy(b),
                "P": xy(p),
            }
        )

    return ans


with timed():
    teststart = parse_input(test_txt)
    start = parse_input(input_txt)


# %% main
def to_matrix(d):
    return numpy.array(
        [
            [Fraction(d["A"][0]), Fraction(d["B"][0])],
            [Fraction(d["A"][1]), Fraction(d["B"][1])],
        ]
    )


def inverse(m):
    (a, b), (c, d) = m
    det = Fraction(1, a * d - b * c)

    return det * numpy.array(
        [
            [d, -b],
            [-c, a],
        ]
    )


def get_lin_comb(d):
    m = to_matrix(d)
    inv = inverse(m)

    return inv @ d["P"]


def cost(p: list[Fraction]):
    a, b = p
    if a.denominator != 1 or b.denominator != 1:
        return 0
    return a.numerator * 3 + b.numerator


# %%
sum([cost(get_lin_comb(t)) for t in start])


# %%
# %% PART 2
# %%
def get_lin_comb2(d):
    m = to_matrix(d)
    inv = inverse(m)

    return inv @ (numpy.array(d["P"]) + 10000000000000)


sum(([cost(get_lin_comb2(t)) for t in start]))
