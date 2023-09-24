from pathlib import Path
from argparse import ArgumentParser

import requests
from markdownify import markdownify as md
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # parse arguments
    parser = ArgumentParser()
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)

    args = parser.parse_args()

    # get problem
    url = f"https://adventofcode.com/{args.year}/day/{args.day}"
    print(url)
    r = requests.request("GET", url)

    # write into files
    p = Path(f"{args.year}/{args.day}")
    p.mkdir(parents=True, exist_ok=True)

    (p / "problem.md").write_text(md(r.text))

    soup = BeautifulSoup(r.text, "html.parser")
    for c in soup.find_all("code"):
        print(c.text)
        ans = input("is this the test input? ")
        if ans == "y":
            (p / "test.txt").write_text(c.text)
            break
    (p / "main.py").write_text(Path("template.py").read_text())

    # can't get input, but can prepare the file
    (p / "input.txt").touch()
