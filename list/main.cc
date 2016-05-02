#include <iostream>
#include <string>
#include "list.h"
#include "square.h"

using namespace std;

void m1()
{
	cout << "hello world" << endl;
}

void m2()
{
	square * o = new square(2);
    cout << "suare size is " << o->get_size() << endl;
	delete o;
}

void m3()
{
	ListNode<int> * a = new ListNode<int>(6);
    cout << a->data << endl;
	delete a;
}

void m4()
{
	List<string> * b = new List<string>();
	b->add("A");
	b->add("B");
	b->add("C");
	b->add("D");
	b->print();
	cout << b->get(3) << endl;
	b->set(0,"X");
	b->set(3,"Y");
	b->print();
	delete b;
}

int main()
{
   m4();
   return 0;
}
