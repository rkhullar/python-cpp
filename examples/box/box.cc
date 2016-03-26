#include <iostream>
#include <string>

using namespace std;

class box
{
    public:
      box(double w, double h, double l)
	: width(w), height(h), length(l) 
        {}

        double width; 
	double height; 
	double length;
  
        double volume(){return width * height * length;}
        string output(){return "this is a box";}
};

int main()
{
    box b = box(1, 2, 3);
    cout << b.output() << endl;
    cout << b.volume() << endl;
    return 0;
}
