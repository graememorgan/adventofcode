corners = {(0, 0), (0, 99), (99, 0), (99, 99)}

lights = corners | {(x, y) for y, row in enumerate(open("day18-input").read().splitlines()) for x, light in enumerate(row) if light == "#"}

neighbours = lambda x, y: len([(xx, yy) for xx in range(x - 1, x + 2) for yy in range(y - 1, y + 2) if (x, y) != (xx, yy) and (xx, yy) in lights]) 

for _ in range(100):
  lights = corners | {(x, y) for x in range(100) for y in range(100)
    if (x, y) not in lights and neighbours(x, y) == 3 
    or (x, y) in lights and 2 <= neighbours(x, y) <= 3}

print len(lights)
