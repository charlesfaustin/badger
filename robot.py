import sys
from enum import Enum
import copy

class InvalidArgumentException(Exception):
    pass

class Robot:
    allowed_orientations = ["N", "E", "S", "W"]
    allowed_movements = ["R", "L", "F"]
    orientation = None

    def __init__(self, xcoord,ycoord):
        self.xcoord = xcoord
        self.ycoord = ycoord

    def set_orientation(self, direction):
        if direction not in self.allowed_orientations:
            raise InvalidArgumentException("invalid orientation")
        self.orientation = direction

    def process_movement(self, movement):
        if self.orientation is None:
            raise InvalidArgumentException("set orientation first")
        if movement not in self.allowed_movements:
            raise InvalidArgumentException("invalid movement")
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
        #print("{} {}".format(robot, instructionline))
        instruction_list = list(instructionline)
        some_str_var= ""
        for x in instruction_list:
            some_str_var = ""
            #print("positon before next step is x:{},y:{} , orientation is {}".format(robot.xcoord, robot.ycoord, robot.orientation))
            #print("action is: {}".format(x))
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


        print(some_str_var)


    def __str__(self):
        return "map with upper-right bound of {},{}".format(self.xcoord, self.ycoord)


# todo: unit test
def chunkup(list_object,items_per_list):
    chunked_list = [list_object[i * items_per_list:(i + 1) * items_per_list] for i in range((len(list_object) + items_per_list - 1) // items_per_list )]
    return chunked_list

if __name__ == "__main__":
    #print(sys.argv)
    if len(sys.argv) != 2:
        raise InvalidArgumentException("incorrect number of arguments passed to the script")

    text_file = open(sys.argv[1])
    file_content = text_file.read()
    file_content = file_content.split('\n')
    input_ready_for_program = [x.strip() for x in file_content if x.strip() != '']

    map_coords_string = input_ready_for_program[0]
    map_x_coord = int(map_coords_string[0])
    map_y_coord = int(map_coords_string[1])

    map_object = MarsMap(map_x_coord, map_y_coord)
    
    # the remaining lines, grouped in pairs, each pair is for one robot
    remaining_lines = input_ready_for_program[1:]
    # later do check to make sure number of lines are even, otherwise throw errot

    # group them in pairs, then do for loop
    chunked_list = chunkup(remaining_lines,2)
    #print(chunked_list)
    for list_object in chunked_list:

    
        robot_coords_orientation = list_object[0]

        # get start x-coordinate  of robot
        robot_x_coord = int(robot_coords_orientation[0])

        # get start y-coordinate  of robot
        robot_y_coord = int(robot_coords_orientation[1])

        # get start orientation of robot
        robot_orientation = robot_coords_orientation[2]

        # create robot
        robot_object = Robot(robot_x_coord,robot_y_coord)

        #set orientation
        robot_object.set_orientation(robot_orientation)

        #pass the robot, and its instruction list to the map

        map_object.process_robot_actions(robot_object, list_object[1])
        print("-----------------------------------------------------")








    #each for loop starts a new robot
    #1st line (out of 2 lines) for that grouping sets location & orientation
    # 2nd line mutates the robot location and orientation
    #print final end location

