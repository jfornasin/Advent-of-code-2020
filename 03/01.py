
file_object = open("advent.of.code.03.txt", "r")
lines = file_object.readlines()
lines[-1] = lines[-1] + '\n'

treesmap = list(map(lambda s: s[:-1], lines))

class Position:
    x = 0
    y = 0

currentpos = Position()
treescount = 0

def getnextposfunc(rightmov, downmov, length):
    def getnextpos(position):
        result = Position()
        result.x = (position.x + rightmov) % length
        result.y = position.y + downmov
        return result
    return getnextpos

def istreeposition(position, map):
    return map[position.y][position.x] == '#'

nextpos = getnextposfunc(3, 1, len(treesmap[0]))

while currentpos.y < len(treesmap) - 1:
    currentpos = nextpos(currentpos)
    treescount += (1 if istreeposition(currentpos, treesmap) else 0)

print(treescount)