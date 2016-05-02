rebuild: clean compile

clean:
	rm -rf *~ *.o *.gch target

compile: square.h square.cc list.h main.cc
	g++ -c square.cc
	g++ -c main.cc
	g++ square.o main.o -o target

test: rebuild
	./target
