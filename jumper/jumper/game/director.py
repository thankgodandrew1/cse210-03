from game.terminal_service import TerminalService
from game.parachute import Parachute
from game.puzzle import Puzzle

class Director:


    """A person who directs the game
    Attributes:
        terminal (TerminalService): the game's jumper
        is_guessing (boolean): whether or not to keep playing
        parachute (Parachute): Player's parachute
        jumper (Jumper): For getting and displaying information on the terminal        
    """
    def __init__(self):
        """Constructs a new Director
        Args: 
            self(Director): an instance of Director.
        """
        self._word = Puzzle()
        self._parachute = Parachute()
        self._is_playing = True
        self._terminal_service = TerminalService()
        self.guessed_word = ""
        self.tries = 5
        self.hidden_word = []
        


    def start_game(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        self.guessed_word = self._word.new_word()
        self.hidden_word = self._word.letters
        self._word.print_blanks()
        self._parachute.show_parachute(self.tries)
        while self._is_playing:
            guess = self._get_inputs()
            self._do_updates(guess)
            self._do_outputs()

    def _get_inputs(self):
        guess_letter = self._terminal_service.read_text('Guess a letter [a-z]: ')
        return guess_letter

    def _do_updates(self, guess):
        wrong_letter = []
        found_letter = False
        chosen_word = []

        for letter in self.guessed_word:
            chosen_word.append(letter)

        for i in range(0, len(chosen_word)):
            letter = chosen_word[i]
            if guess == letter:
                self._word.letters[i] = letter
                found_letter = True
                self._terminal_service.write_text('Yay! You guessed a correct letter :)')

        if found_letter == False:
            self.tries -= 1
            self._terminal_service.write_text('Incorrect letter! Please try again :)')
            wrong_letter.append(guess)
            self._terminal_service.write_text(wrong_letter)

        self._word.print_blanks()
        self._parachute.show_parachute(self.tries)
            

    def _do_outputs(self):
        '''
        When all the parachute strings are gone  or when all the blanks are filled...
        '''
        if self.tries == 0:
            self._is_playing = False
            self._terminal_service.write_text('Oops, sorry you lost')
        
        # see if there any underscores left in the list 
        if "_" not in self._word.letters:
            self._is_playing = False
            self._terminal_service.write_text('Congrats! You win!')