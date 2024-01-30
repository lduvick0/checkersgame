# Specifications for the main.py file:
# 1 point: The main.py file must import the entire checkers library.
import checkers
# 1 point: The code must check if it’s running as main,
# and if so, call a function called game containing the main functionality, described next.
if __name__ == "__main__":
    # 2 point: The game function will ask the user for the size of the board and will call the build_board function.
    # It will then print out the full board (you can just print the variable out; no need for extra formatting).
    # It will next print out how many empty cells, how many red cells, and how many black cells are in the board
    # using a function from your checkers.py file.

    def game():
        bSize=int(input("Enter the size of the board: "))
        mBoard=checkers.build_board(bSize)
        print(mBoard)
        rCount =checkers.get_count(mBoard,"Red")
        bCount = checkers.get_count(mBoard, "Black")
        eCount = checkers.get_count(mBoard, "Empty")
        print(f"\nRed count: {rCount}")
        print(f"Black count: {bCount}")
        print(f"Empty count: {eCount}")


    game()