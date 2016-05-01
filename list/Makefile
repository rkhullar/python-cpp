rebuild: clean compile

clean:
	rm -rf target *~

compile: list.cc
	g++ list.cc -o target

test: rebuild
	./target
