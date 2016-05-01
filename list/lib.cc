#include <iostream>
#include <string>
#include "lib.h"

using namespace std;

void test()
{
	cout << "this is a string" << endl;
}

square::square(int size)
{
    this->size = size;
}

int square::get_size(void)
{
    return this->size;
}
