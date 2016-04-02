/*
 * @author  :  Rajan Khullar
 * @created :  04/02/16
 * @updated :  04/02/16
 */

#include <stdio.h>
#include <stdlib.h>
#include "box.h"

int main(int argc, char *argv[])
{
	class_box* box_kls = class_box_load();

	box* b1 = box_kls->init(1,2,3);
	box_kls->print(b1);

	int v = box_kls->volume(b1);
	printf("Volume: %d\n", v);

	free(b1);
	free(box_kls);
	return 0;
}
