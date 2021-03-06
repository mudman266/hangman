# Josh Williams
# Hangman

from main_screen import Ui_MainWindow

from PyQt5 import QtWidgets as qtw
import random

puzzleBank = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet", "Kilo",
              "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor",
              "Whiskey", "XRay", "Yankee", "Zulu"]

letters_guessed = []
debugging = True


def select_puzzle():
    p = random.randint(0, len(puzzleBank) - 1)
    puz = list(puzzleBank[p].upper())
    print("Puzzle selected: {:}".format(puz))
    return puz


class Hangman(qtw.QMainWindow):
    wrong_guesses = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnGuess.clicked.connect(self.guess)
        self.ui.btnHead.setVisible(False)
        self.ui.btnBody.setVisible(False)
        self.ui.btnLeg1.setVisible(False)
        self.ui.btnLeg2.setVisible(False)
        self.ui.btnArm1.setVisible(False)
        self.ui.btnArm2.setVisible(False)
        self.puzzle = select_puzzle()

    def guess(self):
        if debugging:
            print("Getting the input")
        guessing = self.ui.linInput.text()
        # Validate the input is a letter
        if guessing.isalpha():
            if debugging:
                print("Alpha input found.")
            if len(guessing) > 1:
                # Too many letters entered
                if debugging:
                    print("More than 1 letter input.")
                qtw.QMessageBox.critical(self, "Too Many Letters", "You have Entered more than 1 letter. Try again.")
            else:
                # Has the letter been guessed already?
                if guessing.upper() in letters_guessed:
                    print("Letter guessed already.")
                    qtw.QMessageBox.critical(self, "Letter Guessed Already",
                                             "You have already guessed that letter. Try again.")
                else:
                    # Add the guessed item to the list and redraw the board
                    print("New letter guessed: {:}".format(guessing))
                    letters_guessed.append(guessing.upper())
                    self.draw_board()
        else:
            # Non alpha character found
            print("Non-Alpha character found.")
            qtw.QMessageBox.critical(self, "Invalid Character", "Only letters A-Z accepted.")

        # Clear the previous input
        self.ui.linInput.setText("")
        self.ui.linInput.setFocus()

    def draw_board(self):
        # Update the guessed letters on screen
        guessed_word = ""
        for letter in sorted(letters_guessed):
            guessed_word += "  " + letter
        self.ui.lblLetters.setText(guessed_word)

        # Draw the correctly guessed letters
        correct_word = ""
        for letter in self.puzzle:
            if letter in letters_guessed:
                print("Letter found!")
                correct_word += letter
            else:
                print("Letter not found.")
                correct_word += " _ "
        self.ui.lblLettersGuessedTitle_2.setText(correct_word)

        # Draw the man for any wrong guesses
        if letters_guessed[len(letters_guessed) - 1] not in self.puzzle:
            self.wrong_guesses += 1
            if self.wrong_guesses > 5:
                print("Game Over")
                self.ui.btnLeg2.setVisible(True)
                self.game_over()
            if self.wrong_guesses == 5:
                print("Wrong answer 5. It's almost over.")
                self.ui.btnLeg1.setVisible(True)
            if self.wrong_guesses == 4:
                print("Wrong answer 4.")
                self.ui.btnArm2.setVisible(True)
            if self.wrong_guesses == 3:
                print("Wrong answer 3.")
                self.ui.btnArm1.setVisible(True)
            if self.wrong_guesses == 2:
                print("Wrong answer 2.")
                self.ui.btnBody.setVisible(True)
            if self.wrong_guesses == 1:
                print("Wrong answer 1.")
                self.ui.btnHead.setVisible(True)

        # Check for a winner
        if " _ " not in correct_word:
            print("Winner winner chicken dinner!")
            # Build the goal word to inform the winner!
            goal_word = ""
            for let in self.puzzle:
                goal_word += let
            qtw.QMessageBox.information(self, "Winner!", "Winner! Congrats! The correct word was: {:}".format(goal_word))
            exit(0)

    def game_over(self):
        print("Running Game Over")

        # Build the goal word to inform the loser, er.. user rather.
        goal_word = ""
        for let in self.puzzle:
            goal_word += let

        qtw.QMessageBox.information(self, "Game Over", "Game Over. The correct word was: {:}".format(goal_word))
        exit(0)


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = Hangman()
    widget.show()

    app.exec_()
