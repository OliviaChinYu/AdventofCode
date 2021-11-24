import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

race = 2503 
reindeers = []

reindeer_points = {}

def part_one():
	for line in f:
		lst = line.split()
		reindeer = lst[0]
		speed = int(lst[3])
		duration = int(lst[6])
		rest = int(lst[-2])
		period = duration + rest
		period_dist = speed * duration
		period_count = race // period
		remainder = race % period
		remainder_dist = speed * duration if remainder > duration else speed * remainder
		total_dist = (period_count * period_dist) + remainder_dist
		reindeers.append((reindeer, total_dist))
	print(reindeers)
	biggest_dist = max(rd[1] for rd in reindeers)
	return biggest_dist

def part_two():
	for line in f:
		lst = line.split()
		reindeer = lst[0]
		speed = int(lst[3])
		duration = int(lst[6])
		rest = int(lst[-2])
		reindeers.append((reindeer, speed, duration, rest))
		reindeer_points[reindeer] = 0
	for i in range(1,race+1):
		reindeer_status = []
		for rd in reindeers:
			reindeer = rd[0]
			speed = rd[1]
			duration = rd[2]
			rest = rd[3]
			period = duration + rest
			period_dist = speed * duration
			period_count = i // period
			remainder = i % period
			remainder_dist = speed * duration if remainder > duration else speed * remainder
			total_dist = (period_count * period_dist) + remainder_dist
			reindeer_status.append((reindeer, total_dist))
		max_dist = max(rd[1] for rd in reindeer_status)
		for rd, dist in reindeer_status:
			if dist == max_dist:
				reindeer_points[rd] += 1
	print(reindeer_points)
	points = max(value for value in reindeer_points.values())
	return points


print(part_two())