#include <iostream>
#include <string>
#include "list.h"
//#include "lib.h"

using namespace std;

void m1()
{
	cout << "hello world" << endl;
}

/*
void m2()
{
	square o = square(2);
    cout << "suare size is " << o.get_size() << endl;
}
*/

void m3()
{
	ListNode<int> item = ListNode<int>(6);
    cout << item.get_data() << endl;
}

int main()
{
   m3();
   return 0;
}
