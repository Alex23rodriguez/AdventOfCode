from argparse import ArgumentParser
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

if __name__ == "__main__":
    # parse arguments
    parser = ArgumentParser()
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)

    args = parser.parse_args()

    # get problem
    url = f"https://adventofcode.com/{args.year}/day/{args.day}"
    print(url)
    cookie = input("Provide session cookie: ").strip('"')
    if cookie:
        headers = {"Cookie": f"session={cookie}"}
        r = requests.get(url, headers=headers)
        r2 = requests.get(f"{url}/input", headers=headers)
    else:
        r = requests.get(url)
        r2 = None

    assert r.status_code == 200, f"request failed with code {r.status_code}"

    # write into files
    p = Path(f"{args.year}/{args.day:02}")
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

    if r2:
        (p / "input.txt").write_text(r2.text)
    else:
        (p / "input.txt").touch()
