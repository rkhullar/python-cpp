rebuild:	clean, compile

clean:
	rm -rf *~ target.o target

compile:	target.cc
	g++ -std=c++0x -c target.cc -o target.o
	g++ -std=c++0x target.o -o target
