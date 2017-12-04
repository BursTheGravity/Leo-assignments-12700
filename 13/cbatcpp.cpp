#include <iostream>

bool cigar_party (int cigars, bool is_weekend) {
	if (cigars >= 40) {
		if (is_weekend) { return true; }
		else if (cigars <= 60) { return true; }
	}
	return false;
}

int caught_speeding (int speed, bool is_birthday) {
	if (is_birthday) { speed -= 5; }
	if (speed <= 60) { return 0; }
	else if (speed > 60 && speed <= 80) { return 1; }
	else if (speed > 80) { return 2; }
}

int lone_sum (int a, int b, int c) {
	int ans = 0;
	if (a != b && a != c) { ans += a; }
	if (b != a && b != c) { ans += b; }
	if (c != a && c != b) { ans += c; }
	return ans;
}

int main () {
	std::cout << std::boolalpha; //print bools as true or false
	std::cout << "cigar_party(30, false) : " << cigar_party(30, false) << std::endl; //→ False
	std::cout << "cigar_party(50, false) : " << cigar_party(50, false) << std::endl; //→ True
	std::cout << "cigar_party(70, true) : " << cigar_party(70, true) << std::endl; //→ True
	std::cout << "caught_speeding(60, false) : " << caught_speeding(60, false) << std::endl; //→ 0
	std::cout << "caught_speeding(65, false) : " << caught_speeding(65, false) << std::endl; //→ 1
	std::cout << "caught_speeding(65, true) : " << caught_speeding(65, true) << std::endl; //→ 0
	std::cout << "lone_sum(1, 2, 3) : " << lone_sum(1, 2, 3) << std::endl; //→ 6
	std::cout << "lone_sum(3, 2, 3) : " << lone_sum(3, 2, 3) << std::endl; //→ 2
	std::cout << "lone_sum(3, 3, 3) : " << lone_sum(3, 3, 3) << std::endl; //→ 0
}