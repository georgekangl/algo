# Makefile
CXX = clang++
DEBUG = -g
CFLAGS = -c -Wall
LFLAGS = -Wall
INCLUDES = -I .
OBJECTS = sorting.o
.PHONY: all clean

all: sort

sort: $(OBJECTS)
	@echo "Building..."
	$(CXX) $(LFLAGS) $(INCLUDES) $(OBJECTS) -o sort

sorting.o: sorting.cpp
	$(CXX) $(CFLAGS) $(INCLUDES) sorting.cpp

clean:
	@echo "Cleaning up ... "
	-rm sort
	-rm $(OBJECTS)
