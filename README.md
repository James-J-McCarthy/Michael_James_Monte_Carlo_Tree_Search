# Michael_James_Monte_Carlo_Tree_Search

## How to use: 

Open repo in python editor. All code is in Python. 

Run the file titled main.py to start the program. The computer will makes moves 
displayed as a print out to the terminal. 

the algorithm make moves in response by collecting user input via input().

Your input must be in the format 'rowNumber columnNumber' with a space in between, where
the top right corner of the board is input: '1 3'

the program stops once the game ends. 

wrong inputs will not be parsed and will cuase error: common ones and their meaning are noted here;  
    -   if lots of "sentinal errors" are printed: move entered on top of a preexisting move. 
        -   note, going on top of another peice does not always cause an error
    - this error: "ValueError: invalid literal for int() with base 10: '&'",
    means the program was previous running when it was started. 

if the game ends and input is still open, it sometimes crashes right away, in this case start it over. 

at anypoint, enter a non space input like so: '1n4' and your move input will be ignored
in favor of a print out of all current children states' boards and corresponding scores. 

