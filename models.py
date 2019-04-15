import copy
from exceptions import (InvalidArgumentException, BadOrientationException,
    BadMovementException,  NoOrientationException, InstructionListException)

class Robot:
    allowed_orientations = ["N", "E", "S", "W"]
    allowed_movements = ["R", "L", "F"]
    orientation = None
    max_coord_value = 50

    def __init__(self, xcoord,ycoord):
        if (xcoord > self.max_coord_value) or (ycoord > self.max_coord_value):
            raise InvalidArgumentException("max value for a coordinate is 50")

        self.xcoord = xcoord
        self.ycoord = ycoord

    def set_orientation(self, direction):
        if direction not in self.allowed_orientations:
            raise BadOrientationException("invalid orientation")
        self.orientation = direction

    def process_movement(self, movement):
        if self.orientation is None:
            raise NoOrientationException("set orientation first")
        if movement not in self.allowed_movements:
            raise BadMovementException("invalid movement")
        if movement == "R":
            if self.orientation == "N":
                self.orientation = "E"

            elif self.orientation == "E":
                self.orientation = "S"

            elif self.orientation == "S":
                self.orientation = "W"

            elif self.orientation == "W":
                self.orientation = "N"
        if movement == "L":
            if self.orientation == "N":
                self.orientation = "W"

            elif self.orientation == "W":
                self.orientation = "S"

            elif self.orientation == "S":
                self.orientation = "E"

            elif self.orientation == "E":
                self.orientation = "N"

        if movement == "F":
            if self.orientation == "N":
                self.ycoord +=1

            elif self.orientation == "W":
                self.xcoord -= 1

            elif self.orientation == "S":
                self.ycoord -= 1

            elif self.orientation == "E":
                self.xcoord += 1
    def __str__(self):
        return "x:{} , y:{}, orientation:{}".format(self.xcoord, self.ycoord, self.orientation)


class MarsMap:
    scent_locations = []
    def __init__(self, xcoord,ycoord):
        self.xcoord = xcoord
        self.ycoord = ycoord

    def process_robot_actions(self, robot, instructionline):
        instruction_list = list(instructionline)
        if len(instruction_list) > 99:
            raise InstructionListException("instruction list is too long")

        some_str_var= ""
        for x in instruction_list:
            current_x = robot.xcoord
            current_y = robot.ycoord
            current_orientation = robot.orientation
            if (current_x,current_y) in self.scent_locations:
                dry_run_robot_object = copy.deepcopy(robot)
                dry_run_robot_object.process_movement(x)
                if (dry_run_robot_object.xcoord > self.xcoord) or (dry_run_robot_object.ycoord > self.ycoord):
                    continue
            robot.process_movement(x)
            if (robot.xcoord > self.xcoord) or (robot.ycoord > self.ycoord):
                self.scent_locations.append((current_x,current_y))
                some_str_var = "{}{}{}LOST".format(current_x,current_x,current_orientation)
                break
            some_str_var = "{}{}{}".format(robot.xcoord,robot.ycoord,robot.orientation)

        return some_str_var

    def __str__(self):
        return "map with upper-right bound of {},{}".format(self.xcoord, self.ycoord)
