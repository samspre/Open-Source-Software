all: static_block dynamic_block

static_block: program.o staticLib.a
	cc program.o staticLib.a -o static_block

dynamic_block: program.o sharedLib.so
	cc program.o sharedLib.so -o dynamic_block -Wl,-rpath='$$ORIGIN'

program.o: program.c
	cc -c program.c

block.o: source/block.c
	cc -c source/block.c

staticLib.a: block.o
	ar qc staticLib.a block.o

sharedLib.so: block.o
	cc -shared -o sharedLib.so block.o
