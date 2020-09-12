from .stubs import *


class Robot:
	def __init__(self):
		self.team = get_team()
		self.type = get_type()
		self.location = get_location()
		self.board_width = get_board_width()
		self.board_height = get_board_height()
		self.round_num = get_round_num()
		self.since_spawn = 0

	def run(self):
		self.round_num += 1
		self.since_spawn += 1
		self.oil = get_oil()
		self.health = get_health()
		self.is_stunned = is_stunned()
		self.location = get_location()


class HQ(Robot):
	def __init__(self):
		super().__init__()

	def run(self):
		super().run()


class Builder(Robot):
	def __init__(self):
		super().__init__()
		self.speed = GameConstants.BUILDER_SPEED
		self.sense_range = GameConstants.BUILDER_SENSE_RANGE

	def run(self):
		super().run()


class Refinery(Robot):
	def __init__(self):
		super().__init__()

	def run(self):
		super().run()


class Barracks(Robot):
	def __init__(self):
		super().__init__()

	def run(self):
		super().run()


class Tank(Robot):
	def __init__(self):
		super().__init__()
		self.speed = GameConstants.TANK_SPEED
		self.attack_range = GameConstants.TANK_ATTACK_RANGE
		self.attack_cost = GameConstants.TANK_ATTACK_COST

	def run(self):
		super().run()


class Gunner(Robot):
	def __init__(self):
		super().__init__()
		self.speed = GameConstants.GUNNER_SPEED
		self.attack_range = GameConstants.GUNNER_ATTACK_RANGE
		self.attack_cost = GameConstants.GUNNER_ATTACK_COST

	def run(self):
		super().run()


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

