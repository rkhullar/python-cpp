#ifndef LIST_H
#define LIST_H

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

#endif
