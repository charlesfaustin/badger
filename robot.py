import sys
from enum import Enum
from models import Robot, MarsMap
from exceptions import InvalidArgumentException
from utils import chunkup

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise InvalidArgumentException("incorrect number of arguments passed to the script")

    text_file = open(sys.argv[1])
    file_content = text_file.read()
    file_content = file_content.split('\n')
    input_ready_for_program = [x.strip() for x in file_content if x.strip() != '']

    map_coords_string = input_ready_for_program[0].replace(" ",'')
    map_x_coord = int(map_coords_string[0])
    map_y_coord = int(map_coords_string[1])

    map_object = MarsMap(map_x_coord, map_y_coord)
    
    # the remaining lines, grouped in pairs, each pair is for one robot
    remaining_lines = input_ready_for_program[1:]
    #check to make sure number of lines are even
    if len(remaining_lines) % 2 != 0:
        raise Exception("file has odd number of instruction lines for robots")

    # group them in pairs, then do for loop
    chunked_list = chunkup(remaining_lines,2)

    for list_object in chunked_list:
    
        robot_coords_orientation = list_object[0].replace(" ",'')

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
        output = map_object.process_robot_actions(robot_object, list_object[1])
        print(output)
