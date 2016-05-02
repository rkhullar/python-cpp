#include <cstddef>
#include <iostream>
#include <string>

using namespace std;

#ifndef LIST_H
#define LIST_H

template <class T>
class ListNode
{
public:
	T data;
	ListNode<T> *prev, *next;
    ListNode(T data);
};

template <class T>
class List
{
public:
	List();
	List(T data);
	void reset();
	void reset(T data);
	bool empty();
	void print();
	void add(T data);
	bool set(int x, T data);
	T    get(int x);
	~List();

private:
	ListNode<T> *head, *tail, *cursor;
	int size, pos;
	bool seek(int x);
};

template <class T>
ListNode<T>::ListNode(T data)
{
    this->data = data;
	prev = NULL;
	next = NULL;
}

template <class T>
List<T>::List(){reset();}

template <class T>
List<T>::List(T data){reset(data);}

template <class T>
void List<T>::reset()
{
	head = NULL; tail = NULL; cursor = NULL;
	size = 0; pos = -1;
}

template <class T>
void List<T>::reset(T data)
{
	head = new ListNode<T>(data); tail = head; cursor = tail;
	size = 1; pos = 0;
}

template <class T>
bool List<T>::empty()
{
	return head == NULL && tail == NULL;
}

template <class T>
void List<T>::print()
{
	cout << "[";
	cursor = head; pos = 0;
	while(cursor && pos < size-1)
	{
		cout << cursor->data << ", ";
		cursor = cursor->next; pos += 1;
	}
	cout << cursor->data << "]" << endl;
}

template <class T>
void List<T>::add(T data)
{
	if(empty()){reset(data);return;}
	ListNode<T> *node = new ListNode<T>(data);
	node->prev = tail;
    tail->next = node;
    tail = tail->next;
	cursor = tail;
    pos = size++;
}

template <class T>
bool List<T>::seek(int x)
{
	cursor = head; pos = 0;
	while(cursor->next && pos < x)
	{
		cursor = cursor->next; pos += 1;
	}
	return pos == x;
}

template <class T>
bool List<T>::set(int x, T data)
{
	if(!seek(x))
		return false;
	cursor->data = data;
	return true;
}

template <class T>
T List<T>::get(int x)
{
	if(seek(x))
		return cursor->data;
	return NULL;
}

template <class T>
List<T>::~List()
{
	while(head->next)
	{
		head = head->next;
		delete head->prev;
	}
	delete head;
}

#endif
