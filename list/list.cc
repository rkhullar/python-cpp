/*

*/

#include <iostream>
#include <string>

using namespace std;

template <class T>
class ListNode
{
    public:
        ListNode(T data);
        T get_data(void);

    private:
        T data;

};

template <class T>
ListNode<T>::ListNode(T data)
{
    this->data = data;
}

template <class T>
T ListNode<T>::get_data(void)
{
    return this->data;
}


int main()
{
   cout << "hello world" << endl;
   ListNode<int> item = ListNode<int>(6);
   cout << item.get_data() << endl;
}
