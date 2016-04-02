/*
 * @author  :  Rajan Khullar
 * @created :  04/02/16
 * @updated :  04/02/16
 */

#ifndef BOX_H
#define BOX_H

typedef struct box box;
typedef struct class_box class_box;

struct box
{
	int width, height, length;
};

struct class_box
{
    box* (*init)(int w, int h, int l);
	int  (*volume)(box *self);
    void (*print)(box *self);
};

extern class_box* class_box_load();

static box* box_init(int w, int h, int l);
static int box_volume(box *o);
static void box_print(box *o);

#endif
