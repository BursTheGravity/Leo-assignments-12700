#include <iostream>
#include <string>
using std::cout;
using std::endl;
using std::string;

std::string piglatinify ( string s ) {
	string ans = "";
	string x;
	x = s.at(0);
	string vowels = "aeiou";
	if ( vowels.find(x) != string::npos ) { ans = s + "ay"; }
	else { ans = s.substr(1) + x + "ay"; }
	return ans;
}

int main() {
	std::cout << "piglatinify('hello'): " << piglatinify("hello") << std::endl;
	std::cout << "piglatinify('ello'): " << piglatinify("ello") << std:: endl;
}