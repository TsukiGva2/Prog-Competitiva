programa: main.cpp
	g++ -O2 -std=c++17 -Wshadow -fsanitize=address,undefined -Wall -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wno-unused-but-set-variable main.cpp -o programa

.PHONY: test
test: programa input.txt
	./programa < input.txt

.PHONY: all
all: test
