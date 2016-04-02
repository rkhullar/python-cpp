/*
 * @author  :  Rajan Khullar
 * @created :  04/02/16
 * @updated :  04/02/16
 */

#include <stdio.h>
#include <stdlib.h>
#include "box.h"

extern class_box* class_box_load()
{
	class_box* kls = (class_box*) malloc(sizeof(class_box));
	if(kls == NULL) exit(1);
	kls->init = &box_init;
	kls->volume = &box_volume;
	kls->print = &box_print;
	return kls;
}

static box* box_init(int w, int h, int l)
{
	box* o = (box*) malloc(sizeof(box));
	if(o == NULL) exit(1);
	o->width = w;
	o->height = h;
	o->length = l;
	return o;
}

static int box_volume(box *o)
{
	return o->width * o->height * o->length;
}

static void box_print(box *o)
{
	printf("This is a box. %d\n", o->width);
}
