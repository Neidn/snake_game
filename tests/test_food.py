######################################################################
#  F O O D   T E S T   C A S E S
######################################################################
# pylint: disable=too-many-public-methods
import unittest

from service.food import Food


class TestFood(unittest.TestCase):
    """Test Cases for Food"""

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
        self.food = Food()

    def tearDown(self):
        """This runs after each test"""
        pass

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################
    def test_food(self):
        """Test food"""
        self.assertEqual(self.food.shape(), "circle")
        self.assertEqual(self.food.color()[0], "blue")

    def test_refresh(self):
        """Test refresh"""
        previous_position = self.food.position()
        self.food.refresh()
        self.assertNotEqual(self.food.position(), previous_position)
