from re import findall

match = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

sues = [{k: int(v) for k, v in findall("([a-z]+): ([0-9]+)", line)} for line in open("day16-input").read().splitlines()]

print [
  reduce(
    lambda x, y: x and y,
    [
      # for part 1, just match[k] == v
      match[k] < v
      if k in ("cats", "trees")
      else
        (match[k] > v
        if k in ("pomeranians", "goldfish")
        else match[k] == v)
      for k, v
      in sue.iteritems()
    ],
    True)
  for sue
  in sues
  ].index(True) + 1
