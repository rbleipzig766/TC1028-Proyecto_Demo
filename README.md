Context:
Tic Tac Toe is a classic two-player game played on a 3x3 surface. Each player takes turns marking a cell with their symbol (either 'X' or 'O'). The winner is the person who is the first to form a horizontal, vertical, or diagonal line of three of your symbols.

Why is it interesting?
It´s one of the most known games and it´s quite simple to play. The instructions for the code could serve a fundamental exercise in programming, helping me to understand basic concepts. While the game itself is simple, implementing a playable version involves handling user interactions, checking for win conditions, and ensuring a smooth flow of gameplay.

Algorithm:

    Initialize the Game:
        Create a 3x3 surface
        ask the users who is going to start first (X or O)

    Game Loop:
        Repeat the following steps until the game is over:
            Show all the moves taken from both players on the surface
            Ask the current player for his move 
            The field needs to be empty
            Show the players symbol on the 3x3 surface
            Switch to the other player.

    The winner is:
        who has three x´s or o´s in a row (rows, columns, and diagonals)

    Draw Condition:
        If the entire surface is filled and no player has won, the game ends in a draw.

    Display Result:
        Display winner or if it´s a draw


### Instrucciones

Descargar el arvhivo y correr en terminal con:

    python pisa.py

o abrir en Thonny y dar boton de play.

Responder a las preguntas que aparecen, el programa tiene instrucciones y no usa bibliotecas no standard. 
