s = """Faerun to Tristram = 65;Faerun to Tambi = 129;Faerun to Norrath = 144;Faerun to Snowdin = 71;Faerun to Straylight = 137;Faerun to AlphaCentauri = 3;Faerun to Arbre = 149;Tristram to Tambi = 63;Tristram to Norrath = 4;Tristram to Snowdin = 105;Tristram to Straylight = 125;Tristram to AlphaCentauri = 55;Tristram to Arbre = 14;Tambi to Norrath = 68;Tambi to Snowdin = 52;Tambi to Straylight = 65;Tambi to AlphaCentauri = 22;Tambi to Arbre = 143;Norrath to Snowdin = 8;Norrath to Straylight = 23;Norrath to AlphaCentauri = 136;Norrath to Arbre = 115;Snowdin to Straylight = 101;Snowdin to AlphaCentauri = 84;Snowdin to Arbre = 96;Straylight to AlphaCentauri = 107;Straylight to Arbre = 14;AlphaCentauri to Arbre = 46"""

from itertools import permutations

edges = {frozenset(places.split(" to ")): int(distance) for places, distance in [line.split(" = ") for line in s.split(";")]}

# max() instead for part 2
print min([sum([edges[frozenset(pair)] for pair in zip(perm, perm[1:])]) for perm in permutations(reduce(lambda x, y: x | y, edges.keys()))])
