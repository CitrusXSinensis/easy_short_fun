#include <limits.h>
#include <assert.h>


// can_mult(a, b) determine if the sum of a and b causes 
//   integer overflow
int can_add(int a, int b) {
  int up = INT_MAX;
  int low = -INT_MIN;
  if ((a % 2 == 0) && (b % 2 == 0)) {
    return (low / 2 <= (a / 2 + b / 2) && (a / 2 + b / 2) < up / 2 + 1);
  } else if (a % 2 != 0 && b % 2 != 0) {
    return (low / 2 < (a / 2 + b / 2) && (a / 2 + b / 2) < up / 2);
  } else {
    return (low / 2 + 1 <= (a / 2 + b / 2) && (a / 2 + b / 2) < up / 2 + 1);
  }
}

// can_mult(a, b) determine if the product of a and b causes 
//   integer overflow
int can_mult(int a, int b) {
  int product = 0;
  while (b != 0) {
    if ((b > 0) && (can_add(product, a))) {
      product += a;
      --b;
    } else if ((b > 0) && (can_add(product, a))) {
      product -= a;
      ++b;
    } else {
      return 0;
    }
  }
  return 1;
}

// average3(a, b, c) return the average of a, b, and c without
//   the occurance of integer overflow
int average3(int a, int b, int c) {
  assert(a >= 0);
  assert(b >= 0);
  assert(c >= 0);
  return a / 3 + b / 3 + c / 3 + (a % 3 + b % 3 + c % 3) / 3;
}

int main(void) {
  assert(can_add(1,2));
  assert(can_add(2147483647,1) == 0);
  assert(can_add(2147483646,2) == 0);
  assert(can_add(2147483643,5) == 0);
  assert(can_add(-2147483645,-5) == 0);
  assert(can_mult(3,4));
  assert(can_mult(12323213,32232) == 0);
  assert(can_mult(-13000,222232) == 0);
  assert(average3(5, 6, 6) == 5);
  assert(average3(6, 6, 6) == 6);
  assert(average3(7, 8, 6) == 7);
  assert(average3(7, 7, 7) == 7);
  assert(average3(10, 6, 6) == 7);
  assert(average3(0, 0, 6) == 2);
  assert(average3(13, 5, 2) == 6);
  assert(average3(3, 0, 3) == 2);
  trace_int(average3(1, 2, 2147483645));
  assert(average3(2147483647, 2147483646, 2147483645) == 2147483646);
  assert(can_add(INT_MIN, INT_MAX));
  assert(!(can_mult(-1,INT_MIN)));
}  
