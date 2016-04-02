# @author	:  Rajan Khullar
# @created	:  04/02/16
# @updated	:  04/02/16

rebuild: clean compile

clean:
	@rm -rf *.o *~ *.h.gch target

compile: box.c box.h target.c
	gcc -c box.c -o box.o
	gcc -c target.c -o target.o
	gcc box.o target.o -o target

test: rebuild
	./target
