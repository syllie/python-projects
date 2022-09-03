import unittest
import randomgame


class TestRandomGame(unittest.TestCase):
    def test_input(self):
        number = 5
        guess = 5
        result = randomgame.run_guess(guess, number)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
