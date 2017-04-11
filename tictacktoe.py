"""
A simple TicTacToe game

TODO: AI
Made by: Jonas Herseth
"""

class TicTacToe(object):
    """
    A simple TicTacToe game
    """
    def __init__(self):
        self.x = []
        self.o = []
        self.validmoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.turncounter = 0
        self.winningpos = [(1, 2, 3), (4, 5, 6), (7, 8, 9),\
                           (1, 4, 7), (2, 5, 8), (3, 6, 9),\
                           (1, 5, 9), (3, 5, 7)]

    def draw_pos(self, pos):
        """
        Draws X'es and O's in the different positions

        :param pos: the position to draw an X or O
                    Values from 1 to 9 as follows:
                     -----------
                    | 7 | 8 | 9 |
                     -----------
                    | 4 | 5 | 6 |
                     -----------
                    | 1 | 2 | 3 |
                     -----------
        :return: returns the value (x, o or blank) for each position
        """
        if pos in self.x:
            return "x"
        elif pos in self.o:
            return "o"
        else:
            return " "

    def draw_board(self):
        """
        Draw the Tic Tac Toe board
        """
        print("-------------")
        # print first xo line
        print("| ", end='')
        print(self.draw_pos(7), end='')
        print(" | ", end='')
        print(self.draw_pos(8), end='')
        print(" | ", end='')
        print(self.draw_pos(9), end='')
        print(" |", end='\n')
        print("-------------")
        # print second xo line
        print("| ", end='')
        print(self.draw_pos(4), end='')
        print(" | ", end='')
        print(self.draw_pos(5), end='')
        print(" | ", end='')
        print(self.draw_pos(6), end='')
        print(" |", end='\n')
        print("-------------")
        # print third xo line
        print("| ", end='')
        print(self.draw_pos(1), end='')
        print(" | ", end='')
        print(self.draw_pos(2), end='')
        print(" | ", end='')
        print(self.draw_pos(3), end='')
        print(" |", end='\n')
        print("-------------")

    def is_valid(self, allmoves, userinput):
        """
        Checks whether a move is valid or not

        :param allmoves: a list of all moves done so far
        :param userinput: move to check
        :return:     1 if valid move
                     0 if input not a valid move
                    -1 if the move has already been done
        """
        if userinput not in self.validmoves:
            return 0
        elif userinput in allmoves:
            return -1
        else:
            return 1

    def check_winner(self):
        """

        :return: "x" if x is the winner, "o" if o is the winner, else False if no winner
        """
        for n in self.winningpos:
            if n[0] in self.x and n[1] in self.x and n[2] in self.x:
                return "x"
            if n[0] in self.o and n[1] in self.o and n[2] in self.o:
                return "o"
        return False

    def get_input(self):
        """
        Gets a new move from the user.
        """
        userinput = ""
        try:
            userinput = int(input("Enter a position: "))
        except ValueError:
            print("Invalid input, try again.")

        if self.is_valid(self.x + self.o, userinput) == 1:
            if self.turncounter % 2:
                self.o.append(userinput)
                self.turncounter += 1
            else:
                self.x.append(userinput)
                self.turncounter += 1
        elif self.is_valid(self.x + self.o, userinput) == -1:
            print("That move has already been made")


def main():
    """
    Main game loop
    """
    finished = False
    t = TicTacToe()
    t.draw_board()
    while not finished:
        t.get_input()
        t.draw_board()
        if t.check_winner():
            print("{} is the winner".format(t.check_winner()))
            finished = True
        if len(t.o) + len(t.x) == 9:
            print("The game is a draw!")
            finished = True


if __name__ == "__main__":
    main()
