#!/bin/bash


#python3 solve01.py level
#./level
#input
for ((i=0 ; ; ))

do
	gunzip < drop > file
	tar -xvf file
	chmod +x level

	python3 solvedup.py level | cat > out
	python3 read.py

	python3 read.py | ./level
done

