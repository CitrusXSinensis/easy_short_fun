#include <limits.h>
#include <stdio.h>
#include <assert.h>

// min(a, b) return the smaller value of a and b
int min(int a, int b) {
  if (a > b) return b;
  return a;
}

// reverse_add_count(n) read in input and print them out in the reverse 
//   order with each integer subtructed by the smallest integer in the
//   input using only recursion
// requires: input are all integer
// effects: read input and print output
int reverse_add_count(int n) {
  int input;
  if (scanf("%d", &input) > 0) {
    int count = reverse_add_count(min(n, input));
    printf("%d\n", input - count);
    return count;
  } 
  return n;
}


int main(void) {
  reverse_add_count(INT_MAX);
}
