print ("Below is the code for ")
print ("Designing the tic tac toe Python 3X3 grid gameboard of tic tac toe Python")

 
def tictactoe_grid(value):  
    print("\n")  
    print("\t      |      |")  
    print("\t    {} |  {}   |  {}".format(value[0], value[1], value[2]))  
    print('\t______|______|______')  
# printing the first three boxes of the 3X3 game board   
    print("\t      |      |") 
    print("\t   {}  |  {}   |  {}".format(value[3], value[4], value[5]))  
    print('\t______|______|______')  
    print("\t      |      |")  
# printing the second three boxes of the 3X3 game board   
    print("\t  {}   |  {}   |  {}".format(value[6], value[7], value[8]))  
    print("\t      |      |")  
    print("\n") 
# printing the last three boxes of the 3X3 game board   

tictactoe_grid("3X3XXXOOO")
