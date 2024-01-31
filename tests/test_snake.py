######################################################################
#  S N A K E   T E S T   C A S E S
######################################################################
# pylint: disable=too-many-public-methods
import unittest

from service.snake import Snake


class TestSnake(unittest.TestCase):
    """Test Cases for Snake"""

    @classmethod
    def setUpClass(cls):
        """This runs once before the entire test suite"""
        pass

    @classmethod
    def tearDownClass(cls):
        """This runs once after the entire test suite"""
        pass

    def setUp(self):
        """This runs before each test"""
        self.snake = Snake()

    def tearDown(self):
        """This runs after each test"""
        pass

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################
    def test_create_snake(self):
        """Test create snake"""
        length_snake = 3

        # test create snake
        self.assertEqual(len(self.snake.segment_list), length_snake)

        # test head
        self.assertEqual(self.snake.head, self.snake.segment_list[0])

    def test_move(self):
        """Test move"""
        # test move
        self.snake.move()
        self.assertEqual(self.snake.head.xcor(), 20)

    def test_up(self):
        """Test up"""
        # test up
        self.snake.move_up()
        self.assertEqual(self.snake.head.heading(), 90)

    def test_down(self):
        """Test down"""
        # test down
        self.snake.move_down()
        self.assertEqual(self.snake.head.heading(), 270)

    def test_left(self):
        """Test left"""
        # test left
        self.snake.move_up()
        self.assertEqual(self.snake.head.heading(), 90)

        self.snake.move_left()
        self.assertEqual(self.snake.head.heading(), 180)

    def test_right(self):
        """Test right"""
        # test right
        self.snake.move_right()
        self.assertEqual(self.snake.head.heading(), 0)
