import unittest
from utils import chunkup
from models import Robot, MarsMap
from exceptions import (InvalidArgumentException, BadOrientationException,
    BadMovementException,  NoOrientationException, InstructionListException)


class TestUtils(unittest.TestCase):
    """tests utils"""

    def test_chunkup(self):
        self.assertEqual(chunkup([1,2,3,4],2), [[1,2],[3,4]])


class TestRobotExceptions(unittest.TestCase):
    """tests exceptions from robot class"""

    def test_robot_init_exception(self):
        """tests init exceptions"""

        with self.assertRaises(InvalidArgumentException) as context:
            Robot(70,1)

    def test_robot_init_exception(self):
        """tests init exceptions"""
        robot = Robot(1,1)
        with self.assertRaises(BadOrientationException) as context:
            robot.set_orientation("Z")

    def test_robot_bad_orientation_exception(self):
        """tests bad orientation exceptions"""
        robot = Robot(1,1)
        robot.set_orientation("N")
        with self.assertRaises(BadOrientationException) as context:
            robot.set_orientation("Z")

    def test_robot_no_orientation_exception(self):
        """tests no orientation exceptions"""
        robot = Robot(2,2)
        with self.assertRaises(NoOrientationException) as context:
            robot.process_movement("N")

    def test_robot_bad_movement_exception(self):
        """tests bad movement exceptions"""
        robot = Robot(2,2)
        robot.set_orientation("N")
        with self.assertRaises(BadMovementException) as context:
            robot.process_movement("O")

class TestMarsMapExceptions(unittest.TestCase):
    def test_instruction_list_exception(self):
        """tests instruction list exceptions"""
        mars_map = MarsMap(7,8)
        robot = Robot(2,2)
        instruction_list = "RFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRFRF"
        with self.assertRaises(InstructionListException) as context:
            mars_map.process_robot_actions(robot, instruction_list)    

class TestMarsMapOutPut(unittest.TestCase):
    def test_output_1(self):
        """tests program output """
        mars_map = MarsMap(5,3)
        instruction_list = "RFRFRFRF"
        robot = Robot(1,1)
        robot.set_orientation("E")
        output = mars_map.process_robot_actions(robot,instruction_list)
        self.assertEqual(output,"11E")

    def test_output_2(self):
        """tests program output """
        mars_map = MarsMap(5,3)
        instruction_list = "FRRFLLFFRRFLL"
        robot = Robot(3,2)
        robot.set_orientation("N")
        output = mars_map.process_robot_actions(robot,instruction_list)
        self.assertEqual(output,"33NLOST")

    def test_output_3(self):
        """tests program output """
        mars_map = MarsMap(5,3)
        instruction_list = "LLFFFLFLFL"
        robot = Robot(0,3)
        robot.set_orientation("W")
        output = mars_map.process_robot_actions(robot,instruction_list)
        self.assertEqual(output,"23S")

if __name__ == '__main__':
    unittest.main()
