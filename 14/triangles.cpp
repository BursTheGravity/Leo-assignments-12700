#include <iostream>
#include <string>
using std::cout;
using std::endl;
using std::string;

string a = "*";

std::string line(int l, std::string c){
  string ans;
  for (int i = 0; i < l; i++) {
    ans += c;
  }
  return ans;
}

std::string rect(int w, int h) {
  string ans;
  for (int h1 = 0; h1 < h; h1++) {
    ans += line (w, a) + "\n";
  }
  return ans;
}

/*
 *
 **
 ***
 ****
 */
std::string tri1(int h) {
  string ans;
  for (int h1 = 1; h1 <= h; h1++) {
    ans += line (h1, a) + "\n";
  }
  return ans;
}


/*
   *
  ***
 *****
 */
std::string tri2(int h) {
  string ans;
  for (int i = 1; i <= h; i++) {
    int spaces = h - i;
    for (int sp = 1; sp <= spaces; sp++) {
      ans += " ";
    }
    ans += line (i*2-1, a) + "\n";
  }
  return ans;
}

/*
  *
 **
***
 */
std::string tri3(int h) {
  string ans;
  for (int i = 1; i <= h; i++) {
    int spaces = h - i;
    for (int sp = 0; sp < spaces; sp++) {
      ans += " ";
    }
    ans += line (i, a) + "\n";
  }
  return ans;
}
int main(){
  cout << "line(5, '*'): " << endl;
  cout << line(5, a) << endl;
  cout << endl;
  cout << "rect(4, 6): " << endl;
  cout << rect(4, 6) << endl;
  cout << "tri(5): " << endl;
  cout << tri1(5) << endl;
  cout << "tri2(5): " << endl;
  cout << tri2(5) << endl;
  cout << "tri3(5): " << endl;
  cout << tri3(5) << endl;
}

	