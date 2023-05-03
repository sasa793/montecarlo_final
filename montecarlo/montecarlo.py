import pandas as pd
import numpy as np

class Die:
    """A die has N sides, or “faces”, and W weights, and can be rolled to select a face.W weights defaults to 1  for each face but can be changed after object is created. The die has one behavior, this is to be rolled one or more times. Includes 3 methods: change_weight, roll, and show_die."""
    
    def __init__(self, faces):
        """Takes an array of faces as an argument and internally initalizes the weights to 1.0 for each face. Both faces and weights are saved into a private dataframe that is to be shared with other methods"""
        self.faces = faces
        self.weights = [1.0] * len(self.faces)
        self._df = pd.DataFrame({'faces': self.faces, 'weights': self.weights})
        
    def change_weight(self, face, weight):
        """This method changes the weight of a single side. Two arguments are taken, the face value to be changed and the new weight. It checks to see if the face passed is a valid array of weights and if the weight is valid/a float or convertible to a float."""
        if face not in self.faces:
            print("Error: {face} is not a valid face value.")
            return
        try:
            float(weight)
        except ValueError:
            print("Error: weight must be a float.")
            return
        index = self._df.index[self._df['faces'] == face]
        self._df.at[index, 'weights'] = weight

    def roll(self, n=1):
        """This is a random sample from the vector of faces according to the weights that returns a list of outcomes that's not stored internally. It takes a parameter for how many times the die is rolled but efaults to 1."""
        results = []
        norm_weights = np.array(self.weights)/sum(self.weights)
        for i in range(n):
            result = np.random.choice(self.faces, p=norm_weights)
            results.append(result)
        return results
    
    def show_die(self):
        """This method shows the user the die's current set of faces and weights in a dataframe."""
        return self._df

    
class Game:
    """Where one or more die of the same kind one or more time where the games are initalized with one or more similarly defined dice objects. By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and associated faces, but each die object may have its own weights.The most recent play results are kept in the class. Includes 2 methods: play and show (narrow or wide)"""
    
    def __init__(self, dice):
        """Takes a single parameter, a list of already instantiated similar Die objects."""
        self.dice = dice
        self._results = pd.DataFrame()
        
    def play(self, n_rolls):
        """Takes a parameter to specify how many times the dice should be rolled, the results are then saved to a private dataframe of shape N rolls by M dice. The roll number is a named index. The results table containing data has a column for roll number, die number (it's list index), and the face rolled in that instance. """
        for index, die in enumerate(self.dice):
            self._results[index+1] = die.roll(n_rolls)

    def show_results(self, form = 'wide'):
        """This method passes the private dataframe to the user where a parameter is taken to return the dataframe in narrow or wide form. Narrow has a two column index with the roll and die number, and a column of face rolled. While the wide dataframe will have a single column index with the roll number and each die number as a column."""
        if form == 'wide':
            return self._results

        elif form == 'narrow':
            return self._results.melt(var_name='Die', value_name='Value')
        
        else:
            raise ValueError("Wrong result type")
           
        
class Analyzer:
    """This class takes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object. Includes 3 methods: jackpot, combo, and face_counts_per_roll"""
    
    def __init__(self, game):
        """Takes a game object as its input parameter. At initialization time, it also infers the data type of the die faces used."""
        self.game = game
        self.face_type = type(game.dice[0].faces[0])
        self.combos_df = pd.DataFrame()
        self.counts_df = pd.DataFrame()
    
    def jackpot(self):
        """Demonstrates how many times the game resulted in all faces being identical and returns that number to the user as an integer. The dataframe of results, containing roll number as a named index, are stored as a public attribute."""
        return (self.game.show_results(form='wide').nunique(axis=1) == 1).sum()
    
    def combo(self):
        """Computes how many times the distinct combination of faces are rolled along with their counts. These combinations are sorted and saved as a multi-columned index. The results are stored as a dataframe in a public attribute."""
        sorted_rolls = self.game.show_results(form='wide').apply(lambda row: tuple(sorted(row)), axis=1)
        self.combos_df = sorted_rolls.value_counts().reset_index(name='counts').set_index("index")
        self.combos_df = self.combos_df.sort_values(by='counts', ascending=False)
    
    def face_counts_per_roll(self):
        """Computes how often a given face is rolled in each event. The results are storred as a dataframe in a public attribute. Said dataframe has an index of the roll number and face values as columns(wide form)"""
        faces = sorted({face for die in self.game.dice for face in die.faces})
        
        self.counts_df = pd.DataFrame(index=self.game.show_results(form='wide').index, columns=faces)
        self.counts_df = self.counts_df.fillna(0)
        
        for i, row in self.game.show_results(form='wide').iterrows():
            row_counts = row.value_counts()
            self.counts_df.loc[i, row_counts.index] = row_counts.values