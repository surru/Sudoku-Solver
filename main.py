
import os
import sys

f1=sys.argv[1]
f2=sys.argv[2]

import file_read,file_write,create_clause

N=9

fo=open(f1,"r")

lines=fo.readlines()

for i in range(len(lines)):

	mat=file_read.read(lines[i],N)

	clause=create_clause.clause(mat,N)

	file_write.write("ozw.txt",clause,N)

	l='minisat ozw.txt pzw.txt'

	os.system(l)

	# print mat
	mat=file_read.read_SAT("pzw.txt",mat,N)

	file_write.write_output(f2,mat,N,i)

l='rm pzw.txt'
os.system(l)

l='rm ozw.txt'
os.system(l)