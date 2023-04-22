'''
Name:   card_matching_game_with_class_2.1.py

2023.04.22.15.19.36.279
initialize code 2.1
'''
import random

class CardGame:
    def __init__(self):
        self.board = ["▓" for _ in range(16)]
        self.pairedList = self.getPairedList()
        self.play()

    def play(self):
        self.displayBoard()
        while not self.isGameOver():
            try:
                x1 = int(input("\nPlease choose the x-coordinate of the first card: "))
                y1 = int(input("Please choose the y-coordinate of the first card: "))
                cardIndex1 = self.getCardIndex(x1, y1)
                self.flipCard(cardIndex1)
                self.displayBoard()

                x2 = int(input("\nPlease choose the x-coordinate of the second card: "))
                y2 = int(input("Please choose the y-coordinate of the second card: "))
                cardIndex2 = self.getCardIndex(x2, y2)
                self.flipCard(cardIndex2)
                self.displayBoard()

                if x1 == x2 and y1 == y2:
                    print("Hey! You can't pick the same number twice.\n")
                    print("please try again")


                elif self.board[cardIndex1] == self.board[cardIndex2]:
                    print("Congratulations! You found a match.")
                    self.pairedList[cardIndex1] = None
                    self.pairedList[cardIndex2] = None

                else:
                    print(
                        f"Sorry, the cards {self.pairedList[cardIndex1]} and {self.pairedList[cardIndex2]} do not match.")
                    self.board[cardIndex1] = "▓"
                    self.board[cardIndex2] = "▓"

            except ValueError:
                print("Invalid input. Please enter integers for the coordinates.")

    def getPairedList(self):
        numbers = [str(i) for i in range(1, 9)]
        pairedList = numbers + numbers
        random.shuffle(pairedList)
        return pairedList

    def getCardIndex(self, x, y):
        row = x - 1
        col = y - 1
        return (row * 4) + col

    def flipCard(self, index):
        self.board[index] = self.pairedList[index]

    def displayBoard(self):
        for i in range(4):
            print(" ".join(self.board[i*4:i*4+4]))
        #print("\n")

    def isGameOver(self):
        return all(card is None for card in self.pairedList)
if __name__ == "__main__":
    # game = CardGame()
    # game.play()
    game = CardGame()
