#Rock paper scissor game

class main:

    moveOne = str(raw_input("Player 1 Your Move.... ").lower())
    moveTwo = str(raw_input("Player 2 Your Move.... ").lower())


    def compare(c1, c2):
        if c1 == c2:
            return "Its a draw"
        elif c1 == "rock":
            if c2 == "scissors":
                return "Player 1 Wins"
            else:
                return "Player 2 Wins"
        elif c1 == "paper":
            if c2 == "rock":
                return "player 1 Wins"
            else:
                return "Player 2 Wins"
        elif c1 == "scissors":
            if c2 == "paper":
                return "Player 1 Wins"
            else:
                return "Player 2 Wins"
        else:
            return("Invalid Input. Try Again with Rock, Paper or Scissors")

    print main.compare(moveOne, moveTwo)




        

    
