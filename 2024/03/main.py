import re

with open("input.txt") as f:
    text = f.read()

# %%
start = 0
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
ans = 0
while match := re.search(pattern, text[start:]):
    ans += int(match.group(1)) * int(match.group(2))
    start += match.span()[1]

print(ans)

# %%
# PART 2
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
txt = text
ans = 0
enabled = True
while match := re.search(pattern, txt):
    txt = txt[match.span()[1] :]
    if match.group() == "don't()":
        enabled = False
        continue

    if match.group() == "do()":
        enabled = True
        continue

    if enabled:
        ans += int(match.group(1)) * int(match.group(2))

print(ans)
