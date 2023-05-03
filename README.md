# montecarlo_final
Everything Pertaining to my DS5100 Final Project

# Metadata
Author name: Sarah Elmasry

Project name: Monte Carlo Simulator

# Synopsis
To install the package classes: 

- !pip install -e .

The above line of code can be used in either the command line or jupyter notebook

To import the package: 

- from montecarlo import Die, Game, Analyzer

To create a die: 

- my_die = Die([1, 2, 3, 4, 5, 6])

To play a game:

- my_game = Game([my_dice1, my_dice1]) my_game.play(7)

To analyze a game: 

- my_analyzer = Analyzer(my_game)

Jackpot:

- my_analyzer.jackpot())

Combos:

- my_analyzer.combo()

Face_counts_per_roll: 

- my_analyzer.face_counts_per_roll()


# API Description

***Die***: A die has N sides, or “faces”, and W weights, and can be rolled to select a face. W weights defaults to 1  for each face but can be changed after object is created. The die has one behavior, this is to be rolled one or more times. 

-methods

-Change_weight: changes weight of a single side

-Parameters:

-face: face being changed

-new_weight: the new weight introduced

-Raises: Value error uf weight is not valid/float
        
-Roll_die: Rolls the die one or more times
    
-Parameters:
        
-n_rolls: how many time the die is rolled(defaults to one)
            
-Returns: results which is a list of outcomes
        
-Show_die: Demonstrates the die's current set of faces and weights 
    
-Returns: A df of faces and weights of the die
    

***Game***:Where one or more die of the same kind one or more time where the games are initalized with one or more similarly defined dice objects. By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and associated faces, but each die object may have its own weights.The most recent play results are kept in the class. 

-methods

-Play: Plays the game when called Specifies how many times the dice should be rolled

-Paramters:

-n_rolls: Specifies how many times the dice should be rolled
            
-Show_results:

-Paramaters:
     
-Form: wide or narrow style of returning a dataframe

-Returns: A df consisting of die and roll number and face
    

***Analyzer***: This class takes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object.

-methods

-Jackpot: How many times the game resulted in all faces being identical
    
-Paramters:

-None

-Returns: The number of matches as an integer and a df containing roll and die number and face rolled

-Combo: How many times the distinct combination of faces are rolled along with their counts 

-Paramters:

-None

-Returns: A df with combinations are sorted as a multi-columned index

-Face_counts_per_roll:
 
-Stored as a df with an index of the roll number and face values as columns
    

# Manifest

* montecarlo_final
    * montecarlo
        * __init__.py
        * montecarlo_test.py
        * montecarlo.py
    * montecarlo.egg-info
        * dependency_links.txt
        * PKG-INFO
        * requires.txt
        * SOURCES.txt
        * top_level.txt
    * LICENSE
    * .gitignore
    * montecarlo_demo.ipynb
    * montecarlo_test_results.txt
    * README.md
    * setup.py