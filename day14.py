s = """Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.;Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.;Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.;Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.;Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.;Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.;Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.;Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.;Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds."""

reindeer = [(r, int(s), int(t), int(rt)) for r, _, _, s, _, _, t, _, _, _, _, _, _, rt, _ in [line.split(" ") for line in s.split(";")]]

final_time = 2503

# part 1
print max([(final_time / (t + rt)) * s * t + min(final_time % (t + rt), t) * s for r, s, t, rt in reindeer])

# find the leading reindeer at each time interval. the ugly bit at the start is to handle the case where two reindeer tie.
rankings = [[i for i, r in enumerate(rank) if r == max(rank)] for rank in [[(time / (t + rt)) * s * t + min(time % (t + rt), t) * s for r, s, t, rt in reindeer] for time in range(1, final_time + 1)]]

# flatten the rankings
rankings = [i for sublist in rankings for i in sublist]

print [rankings.count(r) for r in range(len(reindeer))]

