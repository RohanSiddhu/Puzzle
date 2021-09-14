/*----------------------------------------------------------------------------
                   Puzzle!
                  ---------
______________________________________________________________________________*/

//Coded by: Rohan Siddhu


#include "Puzzle.h"


/**
 * Main Function : Program's execution starts here.
 */

int main(int argc, const char* argv[]) {
    system("cls");                     // Clearing console window.

    while (1) {
        menu();
        system("cls");

        playscreen();
    }

    return 0;
}


/**
 * menu : Main menu of the game
 */

short menu() {
    short h = 0;
    system("cls");

    gotoxy(38, 11);
    std::cout << "Play";
    rectangle(37, 10, 42, 12);

    gotoxy(38, 14);
    std::cout << "Exit";


    while (1) {
        key = getkey();

        if (key == 80 && h == 0) {                //Select the box over Exit.
            system("cls");
            gotoxy(38, 11);
            std::cout << "Play";
            gotoxy(38, 14);
            std::cout << "Exit";
            rectangle(37, 13, 42, 15);
            h++;
        }

        if (key == 13 && h == 1)                 //Terminates the execution of the program.
            exit(0);

        if (key == 72 && h == 1) {                //Select the box over Play.
            system("cls");
            gotoxy(38, 11);
            std::cout << "Play";
            gotoxy(38, 14);
            std::cout << "Exit";
            rectangle(37, 10, 42, 12);
            h--;
        }

        if (key == 13 && h == 0)
            return 0;
    }
}


/**
 * playscreen : Game Screen
 */

void playscreen() {
    short arr[4][4] = {
        {1,4,15,7},
        {8,10,2,11},
        {14,3,6,13},
        {12,9,5,16}
    };                    //Matrix of the puzzle declairation.
    short x, y, move = 0, change;
    short a = 3, b = 3;

    table();                             //Draw table.

    while (1) {
        for (i = 0, y = 8; i < 4; i++, y += 6) {             //Printing the matrix.
            for (j = 0, x = 24; j < 4; j++, x += 10) {
                gotoxy(x, y);

                if (arr[i][j] == 16)                  //Print blank space at the place of 16.
                    std::cout << "  ";
                else {
                    std::cout.width(2);
                    std::cout << arr[i][j];
                }
            }
        }
        gotoxy(50, 2);
        std::cout << "Moves:";
        gotoxy(58, 2);
        std::cout << move;

        if (ascending(arr) == 0)          //Terminating when the matrix is arranged.
            break;

        key = getkey();                  //Taking controls input.

        if (key == 27) {                   //Contro is passed to homescreen while ESC is pressed.
            menu();
            system("cls");
            table();
        }
        else if (key == 72 && a != 3) {        //Up arrow key.
            change = arr[a][b];
            arr[a][b] = arr[a + 1][b];
            arr[a + 1][b] = change;
            a++;
            move++;
        }
        else if (key == 80 && a != 0) {     //Down arrow key.
            change = arr[a][b];
            arr[a][b] = arr[a - 1][b];
            arr[a - 1][b] = change;
            a--;
            move++;
        }
        else if (key == 75 && b != 3) {     //Left arrow key.
            change = arr[a][b];
            arr[a][b] = arr[a][b + 1];
            arr[a][b + 1] = change;
            b++;
            move++;
        }
        else if (key == 77 && b != 0) {     //Right arrow key.
            change = arr[a][b];
            arr[a][b] = arr[a][b - 1];
            arr[a][b - 1] = change;
            b--;
            move++;
        }
    }
    gameover();
}


/**
 * gameover : Game Over screen.
 */

void gameover() {
    system("cls");
    gotoxy(35, 12);
    std::cout << "Congretulations";
    _getch();
}


/** 
 * table : This function drow a table of 4X4 on the screen.
 */

void table() {
    for (i = 19; i <= 59; i += 10) {
        vline(24, i, 5);
    }
    gotoxy(19, 5);                  //Horizontal Line 1
    std::cout << char(218);
    hline(9);
    for (i = 0; i < 3; i++) {
        std::cout << char(194);
        hline(9);
    }
    std::cout << char(191);

    gotoxy(19, 11);                //Horizontal Line 2
    std::cout << char(195);
    hline(9);
    for (i = 0; i < 3; i++) {
        std::cout << char(197);
        hline(9);
    }
    std::cout << char(180);

    gotoxy(19, 17);               //Horizontal Line 3
    std::cout << char(195);
    hline(9);
    for (i = 0; i < 3; i++) {
        std::cout << char(197);
        hline(9);
    }
    std::cout << char(180);

    gotoxy(19, 23);              //Horizontal Line 4
    std::cout << char(195);
    hline(9);
    for (i = 0; i < 3; i++) {
        std::cout << char(197);
        hline(9);
    }
    std::cout << char(180);

    gotoxy(19, 29);             //Horizontal Line 5
    std::cout << char(192);
    hline(9);
    for (i = 0; i < 3; i++) {
        std::cout << char(193);
        hline(9);
    }
    std::cout << char(217);
}


/**
 * getkey : Retun scancode.
 */

int getkey() {
    int ch;
    ch = _getch();
    if (ch == 0) {
        ch = _getch();
        return ch;
    }
    return ch;
}


/**
 * ascending : This function return 1 when array is not in ascending order and return 0
 *              when array is in ascending order.
 */

short ascending(short q[][4]) {
    short a;
    for (a = 1, i = 0; i < 4; i++)
        for (j = 0; j < 4; j++, a++)
            if (q[i][j] != a)
                return 1;

    return 0;
}
