#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main()
{
	unordered_map<string, int> d1;
	d1["k1"] = 1;
	d1["k2"] = 2;
	d1["k3"] = 3;
	cout << &d1 << endl;
	return 0;
}
