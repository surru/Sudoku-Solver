

clause=[[[1, 1, 2, 1], [1, 2, 2, 1]],
[[1, 1, 1, 2], [-1, 2, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2]],
[[1, 2, 1, 3]]]


def write(file,clause,N):
	fo=open(file,"w")
	nv=N**3
	nv=str(nv)
	nc=len(clause)
	nc=str(nc)

	s="p cnf "+nv+" "+nc+'\n'
	fo.write(s)

	for i in range(len(clause)):
		s=""
		for j in range(len(clause[i])):
			cc=clause[i][j][:]
			a=(cc[1]-1)*(N*N)+(cc[2]-1)*N+cc[3]
			a*=cc[0]
			a=str(a)
			a+=' '
			s+=a

		s+="0 \n"
		fo.write(s)

# write("o.txt",clause,4)

def write_output(file,mat,N,ind):
	if ind==0:
		fo=open(file,"w")
	else:
		fo=open(file,"a")
	s=""
	for i in range(N):
		for j in range(N):
			a=str(mat[i][j])
			s+=a

	s+="\n"
	fo.write(s)