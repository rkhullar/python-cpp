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

void m5()
{
	cout << 1 << endl;
	cout << "a" << endl;
	cout << 0 << " " << 1 << " " << 2 << " " << 3 << " " << 4 << " " << 5 << " " << 6 << " " << 7 << " " << 8 << " " << 9 << endl;
	cout << "this" << " " << "is" << " " << "a" << " " << "string" << " " << "list" << endl;
	int a = 5;
	string b = "hello world";
	cout << a << " " << b << endl;
	List<int> *d = new List<int>();
	List<string> *e = new List<string>();
	d->add(5);
	e->add("six");
	d->add(7);
	e->set(0, "beta");
	d->print();
	e->print();
	delete d;
	delete e;
}

int main()
{
   m5();
   return 0;
}
