instructions = open("day6-input").readlines()

def switch(lights, operators):
  for instruction in instructions:
    operator = None
    # pick the right operator from the dict supplied
    for s, o in operators.iteritems():
      if s in instruction:
        operator = o

    # pull the coordinate pairs out
    a, b = [[int(n) for n in word.split(",")] for word in instruction.split(" ") if "," in word]

    # go over all the coordinates, applying the selected operator
    for x in range(a[0], b[0] + 1):
      for y in range(a[1], b[1] + 1):
        lights[x][y] = operator(lights[x][y])

# Part 1
lights = []
for i in range(1000):
  lights.append([False] * 1000)

switch(lights,
       {"toggle": lambda x: not x,
       "turn on" : lambda x: True,
       "turn off": lambda x: False})

print "Part 1: ", sum([item for sublist in lights for item in sublist])

# Part 2
lights = []
for i in range(1000):
  lights.append([0] * 1000)

switch(lights,
       {"toggle": lambda x: x + 2,
       "turn on" : lambda x: x + 1,
       "turn off": lambda x: max(0, x - 1)})

print "Part 2: ", sum([item for sublist in lights for item in sublist])
