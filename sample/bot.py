import random
import math
from stubs import *

## Game stuff
def add(loc1, loc2):
	return (loc1[0] + loc2[0], loc1[1] + loc2[1])


def sub(loc1, loc2):
	return (loc1[0] - loc2[0], loc1[1] - loc2[1])


def dist(loc1, loc2):
	return (loc2[0] - loc1[0]) ** 2 + (loc2[1] - loc1[1]) ** 2


def inbounds(a, b):
	return a >= 0 and b >= 0 and a < get_board_width() and b < get_board_height()


def normalize(num):
	return 1 if num > 0 else -1 if num < 0 else 0


def getdir(loc1, loc2):
	diff = sub(loc2, loc1)
	greater = 1 if abs(diff[1]) > abs(diff[0]) else 0
	temp = [0, 0]
	temp[greater] = diff[greater]
	if abs(diff[1 - greater]) != 0 and abs(diff[greater]) / abs(diff[1 - greater]) < 2:
		temp[1 - greater] = diff[1 - greater]
	return (normalize(temp[0]), normalize(temp[1]))


def clockwise(loc):
	angle = math.atan2(1, 0)
	angle -= math.pi / 4
	pos = (normalize(math.cos(angle)), normalize(math.sin(angle)))
	return pos


def counter_clockwise(loc):
	angle = math.atan2(1, 0)
	angle += math.pi / 4
	pos = (normalize(math.cos(angle)), normalize(math.sin(angle)))
	return pos


class Robot:
	def __init__(self):
		self.team = get_team()
		self.type = get_type()
		self.location = get_location()
		self.board_width = get_board_width()
		self.board_height = get_board_height()
		self.round_num = get_round_num()

	def run(self):
		self.round_num += 1
		self.oil = get_oil()
		self.health = get_health()
		self.is_stunned = is_stunned()
		self.location = get_location()

	def try_attack(self):
		if self.oil < self.attack_cost:
			return False
		enemies = self.get_enemies()
		for enemy in enemies:
			if dist(self.location, enemy.location) <= self.attack_range:
				attack(enemy.location)
				return True
		return False

	def try_build(self, robot_type):
		for dx in range(-1, 2):
			for dy in range(-1, 2):
				if dx == 0 and dy == 0:
					continue
				loc = add(self.location, (dx, dy))
				if sense_location(loc).type == RobotType.NONE:
					create(robot_type, loc)
					return loc
		return None

	def try_move_loc(self, loc):
		if not can_sense_location(loc):
			return False
		sensed = sense_location(loc)
		if sensed.type != RobotType.NONE:
			return False
		if dist(self.location, loc) > self.speed:
			return False
		move(loc)
		return True

	def try_move(self):
		range = [-1, 0, 1]
		if self.type == RobotType.BUILDER:
			range = [-2, -1, 0, 1, 2]
		for dx in range:
			for dy in range:
				if dx == 0 and dy == 0:
					continue
				loc = add(self.location, (dx, dy))
				if sense_location(loc).type == RobotType.NONE:
					move(loc)
					return True
		return False




class HQ(Robot):

	def __init__(self):
		super().__init__()
		self.num_builders = 0
		self.max_builders = 1

	def run(self):
		super().run()
		if self.num_builders < self.max_builders:
			if self.oil > GameConstants.BUILDER_COST:
				loc = self.try_build(RobotType.BUILDER)
				if loc:
					add_to_blockchain([TEAM_KEY, BUILDER_BUILT, loc[0], loc[1], self.num_builders])
					self.num_builders += 1
					return


class Builder(Robot):

	def __init__(self):
		super().__init__()
		self.speed = GameConstants.BUILDER_SPEED
		self.sense_range = GameConstants.BUILDER_SENSE_RANGE
		self.refineries = 0
		self.barracks = 0
		self.max_refineries = 2
		self.max_barracks = 2

	def run(self):
		super().run()
		if self.refineries >= self.max_refineries and self.barracks >= self.max_barracks:
			return
		if self.refineries < self.max_refineries:
			if self.oil > GameConstants.REFINERY_COST:
				loc = self.try_build(RobotType.REFINERY)
				if loc:
					self.refineries += 1
		elif self.barracks < self.barracks:
			if self.oil > GameConstants.BARRACKS_COST:
				loc = self.try_build(RobotType.BARRACKS)
				if loc:
					self.barracks += 1


class Refinery(Robot):
	def __init__(self):
		super().__init__()

	def run(self):
		super().run()


class Barracks(Robot):
	def __init__(self):
		super().__init__()
		self.spawnables = [RobotType.TANK, RobotType.GUNNER, RobotType.GRENADER]
		self.costs = {
			RobotType.TANK: GameConstants.TANK_COST,
			RobotType.GUNNER: GameConstants.GUNNER_COST,
			RobotType.GRENADER: GameConstants.GUNNER_COST
		}

	def run(self):
		super().run()
		troop = random.choice(self.spawnables)
		if self.oil >= self.costs[troop]:
			self.try_build(troop)


class Tank(Robot):
	def __init__(self):
		super().__init__()

	def run(self):
		super().run()
		if self.try_attack():
			return
		else:
			self.try_move()


class Gunner(Robot):
	def __init__(self):
		super().__init__()

	def run(self):
		super().run()
		if self.try_attack():
			return
		else:
			self.try_move()


type_to_obj = {
	RobotType.HQ: HQ,
	RobotType.BUILDER: Builder,
	RobotType.REFINERY: Refinery,
	RobotType.BARRACKS: Barracks,
	RobotType.TANK: Tank,
	RobotType.GUNNER: Gunner
}

obj = type_to_obj[get_type()]
robot = obj()


def turn():
	robot.run()
