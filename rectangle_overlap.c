struct point {
  int x;
  int y;
};

// rectangles are axis-aligned
struct rectangle {
  struct point ll;              // lower-left corner
  struct point ur;              // upper-right corner
};

const struct rectangle NO_OVERLAP = {{0, 0}, {0, 0}};
///////////////////////////////////


bool valid_rectangle(struct rectangle r) {
  if (r.ll.x < r.ur.x && r.ll.y < r.ur.y) return true;
  return false;
}


bool equal_rectangles(struct rectangle r1, struct rectangle r2) {
  if ((r1.ll.x == r2.ll.x) && (r1.ll.y == r2.ll.y)) {
    if ((r1.ur.x == r2.ur.x) && (r1.ur.y == r2.ur.y)) return true;
  }
  return false;
}

int min(int a, int b) {
  if (a < b) return a;
  return b;
}

int max(int a, int b) {
  if (a > b) return a;
  return b;
}

struct rectangle overlap(struct rectangle r1, struct rectangle r2) {
  if ((r1.ur.x <= r2.ll.x) || (r1.ur.y <= r2.ll.y)) return NO_OVERLAP;
  if ((r2.ur.x <= r1.ll.x) || (r2.ur.y <= r1.ll.y)) return NO_OVERLAP;
  int ur_x = min(r1.ur.x,r2.ur.x);
  int ur_y = min(r1.ur.y,r2.ur.y);
  int ll_x = max(r1.ll.x,r2.ll.x);
  int ll_y = max(r1.ll.y,r2.ll.y);
  struct rectangle r3 = {{ll_x, ll_y}, {ur_x, ur_y}};
  return r3;
}


struct rectangle rotate_right(struct rectangle r) {
  int ur_x = max(r.ll.y, r.ur.y);
  int ur_y = max(r.ll.x * -1, r.ur.x * -1);
  int ll_x = min(r.ll.y, r.ur.y);
  int ll_y = min(r.ll.x * -1, r.ur.x * -1);
  struct rectangle r1 = {{ll_x, ll_y}, {ur_x, ur_y}};
  return r1;
}


int main(void) {

  struct rectangle a = {{0, 0}, {1, 1}};
  struct rectangle b = {{0, -1}, {1, 0}};
  struct rectangle c = {{2, 4}, {3, 10}};

  assert(valid_rectangle(a));
  assert(valid_rectangle(b));
  assert(valid_rectangle(c));
  assert(equal_rectangles(a, a));
  assert(equal_rectangles(a, b) == 0);
  assert(equal_rectangles(a, overlap(a, a)));
  assert(equal_rectangles(NO_OVERLAP, overlap(a, b)));
  assert(equal_rectangles(b, rotate_right(a)));
  assert(equal_rectangles(a, rotate_right(rotate_right(
    rotate_right(rotate_right(a))))));
  assert(equal_rectangles(overlap(a, c), NO_OVERLAP));
}
