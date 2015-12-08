strings = [s.rstrip() for s in open("day8-input").readlines()]

print sum([len(s) for s in strings]) - sum([len(eval(s)) for s in strings])

print sum([2 + s.count("\"") + s.count("\\") for s in strings])
