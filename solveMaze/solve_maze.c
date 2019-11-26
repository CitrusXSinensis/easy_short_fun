#include "maze.h"
#include <stdbool.h>

// This module is used for solving a simple maze, and prints out the directions
//   of each steps for getting out from given maze

// relative_r(n) return the relative right direction 
//   of n
int relative_r(int n) {
  if (n == DOWN) return LEFT;
  else if (n == RIGHT) return DOWN;
  else if (n == UP) return RIGHT;
  else return UP;
}

// relative_l(n) return the relative left direction 
//   of n
int relative_l(int n) {
  if (n == DOWN) return RIGHT;
  else if (n == RIGHT) return UP;
  else if (n == UP) return LEFT;
  else return DOWN;
}

// relative_back(n) return the relative back direction 
//   of n
int relative_back(int n) {
  if (n == DOWN) return UP;
  else if (n == RIGHT) return LEFT;
  else if (n == UP) return DOWN;
  else return RIGHT;
}

// main() prints out the path to get out from a maze
//   that has been read as input
int main(void) {
  struct maze *m = read_maze();
  int dic = DOWN;
  while (1) {
    if (!(is_wall(m, relative_r(dic)))) {
      move(m, relative_r(dic));
      dic = relative_r(dic);
    } else if (!(is_wall(m, dic))) {
      move(m, dic);
    } else if (!(is_wall(m, relative_l(dic)))) {
      move(m, relative_l(dic));
      dic = relative_l(dic);
    } else {
      move(m, relative_back(dic));
      dic = relative_back(dic);
    }
  }
}
