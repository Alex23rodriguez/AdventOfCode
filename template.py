# imports

###
test_txt = open("test.txt").read()

input_txt = open("input.txt").read()
print(f"read {len(input_txt.splitlines())} lines")
###
# read util functions


###
def prepare(inp):
    lines = inp.splitlines()
    # UPDATE
    out = [l for l in lines]
    return out


teststart = prepare(test_txt)
start = prepare(input_txt)
###
# util functions

###
# main
