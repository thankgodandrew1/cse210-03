import random

class Puzzle:

    def __init__(self):
        """Constructs a new Word 
        Args: 
            self(Word): a new instance of Word
        """
        self._words = ['silence',
                    #    'bluff',
                    #    'downfall',
                    #    'climb',
                    #    'lying',
                    #    'weaver',
                    #    'snob',
                    #    'kickoff',
                    #    'match',
                    #    'showcase',
                    #    'parish',
                    #    'wares',
                    #    'soup',
                    #    'mount',
                    #    'extend',
                    #    'brown',
                    #    'expert',
                    #    'mosaic',
                    #    'coil',
                    #    'aide',
                    #    'breeder',
                    #    'concoct',
                    #    'pathway',
                    #    'hearing',
                    #    'bayou',
                    #    'tired',
                    #    'humidity',
                    #    'backpack',
                    #    'crust',
                    #    'dent',
                    #    'market',
                    #    'knock',
                    #    'smite',
                    #    'windy',
                    #    'coin',
                    #    'throw',

                    #    'regimen',
                    #    'drain',
                    #    'bereft',
                    #    'matte',
                    #    'bill',
                    #    'medal',
                    #    'prickly',
                    #    'sarcasm',
                    #    'stuffy',
                    #    'allege',
                    #    'monopoly',
                    #    'lighter',
                    #    'repair',
                    #    'worship',
                    #    'vent',
                    #    'hybrid',
                    #    'buffet',
                    ]
        self._word = ''
        self.letters = []
 

    def new_word(self):
        self._word = random.choice(self._words)
        
        self.hide_word()
        return self._word

    def hide_word(self):
        self.letters = []
        for i in range(len(self._word)):
            self.letters.append('_')
        return self.letters

    def print_blanks(self):
        self.blanks = ' '.join(self.letters)
        print(self.blanks)
