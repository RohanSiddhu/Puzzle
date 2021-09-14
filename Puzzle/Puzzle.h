/*----------------------------------------------------------------------------
                   Puzzle!
                  ---------
______________________________________________________________________________*/

//Coded by: Rohan Siddhu

#pragma once

// Include Headers

#include <iostream>
#include <conio.h>
#include <cstdlib>
#include <Windows.h>


// Global variables

int key;
short i, j;


// Function prototypes

short menu();
void playscreen();
void gameover();
void table();
int getkey();
short ascending(short q[][4]);


// inline functions

 /**
  * gotoxy : Position cursor at (col, row)
  */

inline void gotoxy(short col, short row) {
    HANDLE hStdout = GetStdHandle(STD_OUTPUT_HANDLE);
    COORD position = { col, row };

    SetConsoleCursorPosition(hStdout, position);
}


/**
 * hline : Draw horizontal line of length len
 */

inline void hline(short len) {
    for (j = 0; j < len; j++)
        std::cout << char(196);
}


/**
 * vline : Draw vertical line of length len at (col, row)
 */

inline void vline(short len, short col, short row) {
    for (j = 0; j < len; j++) {
        gotoxy(col, row + j);
        std::cout << char(179);
    }
}


/**
 * rectangle : Draw rectangle between the coordinates (a, b) and (c, d)
 */

inline void rectangle(short a, short b, short c, short d) {
    gotoxy(a, b);
    std::cout << char(218);
    for (i = 0; i < (c - a - 1); i++)
        std::cout << char(196);
    std::cout << char(191);
    for (i = 1; i <= (d - b - 1); i++) {
        gotoxy(c, b + i);
        std::cout << char(179);
    }
    gotoxy(a, b + 1);
    for (i = 1; i <= (d - b - 1); i++) {
        gotoxy(a, b + i);
        std::cout << char(179);
    }
    gotoxy(a, d);
    std::cout << char(192);
    for (i = 0; i < (c - a - 1); i++)
        std::cout << char(196);
    std::cout << char(217);
}
