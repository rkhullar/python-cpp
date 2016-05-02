#include <iostream>
#include <string>
#include "square.h"

using namespace std;

square::square(int size)
{
    this->size = size;
}

int square::get_size(void)
{
    return this->size;
}
