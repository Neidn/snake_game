######################################################################
#  F O O D   T E S T   C A S E S
######################################################################
# pylint: disable=too-many-public-methods
import unittest

from service.scoreboard import ScoreBoard


class TestScoreBoard(unittest.TestCase):
    """Test Cases for ScoreBoard"""

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
        self.scoreboard = ScoreBoard()

    def tearDown(self):
        """This runs after each test"""
        pass

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################
    def test_initial_score(self):
        """Test initial score"""
        self.assertEqual(self.scoreboard.score, 0)

    def test_increase_score(self):
        """Test increase score"""
        self.scoreboard.increase_score()
        self.assertEqual(self.scoreboard.score, 1)

    def test_update_score(self):
        """Test update score"""
        self.scoreboard.update_score()
        self.assertEqual(self.scoreboard.score, 0)

    def test_game_over(self):
        """Test game over"""
        self.scoreboard.game_over()
        self.assertEqual(self.scoreboard.color(), ("red", "red"))
