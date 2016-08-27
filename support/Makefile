rebuild: clean compile

clean:
	rm -rf *~ *.o *.gch target

compile: list.h main.cc
	g++ -c main.cc
	g++ main.o -o target

test: rebuild
	./target
