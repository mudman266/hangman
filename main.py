# Josh Williams
# Hangman

from main_screen import Ui_MainWindow

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import random


puzzleBank = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet", "Kilo",
              "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor",
              "Whiskey", "XRay", "Yankee", "Zulu"]

letters_guessed = []
wrong_guesses = 0
visible_letters = []


def select_puzzle():
    p = random.randint(0, len(puzzleBank) - 1)
    puz = list(puzzleBank[p].upper())
    print("Puzzle selected: {:}".format(puz))
    return puz


class Hangman(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnGuess.clicked.connect(self.guess)
        self.ui.btnHead.setVisible(False)
        self.puzzle = select_puzzle()

    def guess(self):
        guessing = self.ui.linInput.text()
        # Validate the input is a letter
        if guessing.isalpha():
            if len(guessing) > 1:
                print("More than 1 letter input. Exiting...")
                qtw.QMessageBox.critical(self, "Too Many Letters", "You have Entered more than 1 letter. Try again.")
            else:
                print("Letter found in input")
                # Has the letter been guessed already?
                if guessing.upper() in letters_guessed:
                    print("Letter guessed already")
                    qtw.QMessageBox.critical(self, "Letter Guessed Already", "You have already guessed that letter. Try again.")
                else:
                    # Add the guessed item to the list and redraw the board
                    print("New letter guessed: {:}".format(guessing))
                    letters_guessed.append(guessing.upper())
                    self.draw_board()

    def draw_board(self):
        word = ""
        for letter in letters_guessed:
            word += "  " + letter
        self.ui.lblLetters.setText(word)


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = Hangman()
    widget.show()

    app.exec_()
