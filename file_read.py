
def read(str,N):
	# fo =open(file,"r")
	# str =fo.read(N*N)

	mat = [[0 for x in range(N)] for x in range(N)]

	k=0
	for i in range(N):
		for j in range(N):
			if str[k]!='.':
				mat[i][j]=int(str[k])
			k+=1

	return mat

# f=read("i.txt",4)

# print f

def read_SAT(file,mat,N):
	fo=open("pzw.txt","r")

	line=fo.readlines()

	#print line
	m=N*N
	for s in line[1].split():
		a=int(s)
		if a>0:
			x=a%N
			y=1+(a-1)%m/N
			z=1+(a-1)/m
			if x==0:
				x=N
			mat[z-1][y-1]=x

	return mat





