filename = "test.txt"


def getcoords(xystr):
    x, y = xystr.split(", ")
    return int(x[2:]), int(y[2:])


with open(filename) as f:
    input = f.readlines()
    input = [line.split("at ")[1:] for line in input]
    input = [(getcoords(s[0].split(":")[0]), getcoords(s[1].strip())) for s in input]

###

sensors, beacons = zip(*input)
###
sensors, beacons
###
beacons[0]
