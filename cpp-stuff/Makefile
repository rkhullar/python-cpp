rebuild: clean compile

clean:
	rm -rf *~ *.o *.gch target

compile: lib.h lib.cc list.h list.hxx main.cc
	g++ -c lib.cc
	g++ -c list.h
	g++ -c main.cc
	g++ lib.o list.o main.o -o target

test: rebuild
	./target
