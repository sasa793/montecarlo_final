import numpy as np
import pandas as pd
import unittest
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer

class MonteCarloTestSuite(unittest.TestCase):
    
    
    def test_die_created(self):
        """Tests to determine that all the present die faces has a weight of 1.0"""
        my_die = Die([1, 2, 3, 4])
        expected = [1.0, 1.0, 1.0, 1.0]
        actual= list(my_die._df.weights)
        self.assertEqual(expected, actual)
        
    
    def test_change_weight(self):
        """Tests to see if the weight was correctly changed for the specified die face"""
        my_die = Die([1, 2, 3, 4, 5, 6])
        my_die.change_weight(5, 7.5)
        expected = 7.5
        actual = my_die.show_die().iloc[4]['weights']
        self.assertEqual(expected,actual)
      
        
    def test_roll(self):
        """Tests to see if the roll method works and outputs the correct value"""
        my_die = Die([1, 2, 3, 4, 5, 6])
        dtest = my_die.roll(2)
        self.assertEqual(len(dtest),2)
       
        
    def test_show_die(self):
        """Tests to see if df created has the right dimensions"""
        my_die = Die([1, 2, 3, 4, 5, 6])
        test_value = my_die.show_die().shape == (6, 2)    
        message = "Error: Incorrect dimensions of die df."    
        self.assertTrue(test_value, message)

        
    def test_play_game(self):
        """Tests the play method to assess whether the corrrect number of columns and rows are made"""
        my_dice1= Die([1, 2, 3, 4, 5, 6])
        my_dice2= Die([7, 8, 9, 10, 11, 12])
        my_game = Game([my_dice1, my_dice2])   
        my_game.play(5)
        vtest = my_game._results.shape == (5, 2)
        message = "Error: Incorrect data frame dimensions."
        self.assertTrue(vtest, message)        
        
    
    def test_show_results(self):
        """Tests to see if the show_results method defaults correctly (to the wide format)"""
        my_dice1= Die([1, 2, 3, 4, 5, 6])
        my_dice2= Die([7, 8, 9, 10, 11, 12])
        my_game = Game([my_dice1, my_dice2])
        my_game.play(5)
        expected = (5,2)
        actual = my_game.show_results().shape
        self.assertEqual(expected, actual)
        
        
    def test_jackpot(self):
        """Tests to see if the jackpots that the analyzer finds matches the jackpots count/jackpots actual hit. I created this forcing it to hit a certain amount"""
        my_dice1= Die([2, 2])
        my_dice2= Die([2, 2])
        my_game = Game([my_dice1, my_dice2])
        my_game.play(5)
        my_analyzer = Analyzer(my_game)
        tjackpot= my_analyzer.jackpot()
        self.assertTrue((tjackpot) == 5)
        
        
    def test_combo(self):
        """Tests the combo method of the analyzer class"""
        my_dice1= Die([1, 2, 3, 4])
        my_dice2= Die([1, 2, 3, 4])
        my_dice_list = [my_dice1, my_dice2]
        my_game = Game(my_dice_list)
        my_game.play(5)
        my_analyzer = Analyzer(my_game)
        my_analyzer.combo()
        tdf = my_analyzer.combos_df.size
        self.assertGreater(tdf, 0)
        
        
    def test_face_counts_per_roll(self):
        """Tests to see if the face counts df matches the correct shape for num of rolls and dice"""
        my_dice1= Die([1, 2, 3, 4])
        my_dice2= Die([1, 2, 3, 4])
        my_game = Game([my_dice1, my_dice2])
        my_game.play(5)
        my_analyzer = Analyzer(my_game)
        my_analyzer.face_counts_per_roll()    
        expected = (5, 4)
        actual = my_analyzer.counts_df.shape
        self.assertEqual(expected, actual)

        
# if __name__ == "__main__":
#     unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)
    
if __name__ == '__main__':

    unittest.main(verbosity=3)