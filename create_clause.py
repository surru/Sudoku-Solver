import math
import numpy as np
from copy import copy, deepcopy


def clause(mat,N):
	M=math.sqrt(N)

	mat=np.array(mat)

	pred =[]

	for i in range(0,N):
		for j in range(0,N):
			if mat[i][j]==0:
				for k in range(1,N+1):
					u=i-i%M
					v=j-j%M
					if k not in mat[i,:] and k not in mat[:,j] and k not in mat[u:u+M,v:v+M]:
						pred.append([i+1,j+1,k])


	#for i in range(len(pred)):
	#	print pred[i]

	# Finding ccd

	ccd=[]

	pi=0
	pj=0
	cl=[]
	for i in range(len(pred)):
		if pred[i][0]==pi and pred[i][1]==pj:
			a=pred[i][:]
			a.insert(0,1)
			cl.append(a)
		else:
			if cl != []:
				ccd.append(cl)
			cl=[]
			a=pred[i][:]
			a.insert(0,1)
			cl.append(a)
		pi=pred[i][0]
		pj=pred[i][1]

	ccd.append(cl)


	#print len(ccd)

	# for i in range(len(ccd)):
	# 	print ccd[i]

	# Finding ccu

	ccu=[]


	for i in range(len(ccd)):
		cl=[]
		n=len(ccd[i])
		if n>1:
			for j in range(n):
				for k in range(j+1,n):
					a=ccd[i][j][:]
					b=ccd[i][k][:]
					a[0]=-1
					b[0]=-1
					ccu.append([a,b])

	# print len(ccu)

	# for i in range(len(ccu)):
	# 	print ccu[i]

	#Finding crd

	crd=[]

	cle=[]

	for i in range(N):
		cle.append([])
	pi=0
	cli=deepcopy(cle)

	for i in range(len(pred)):
		if pi==pred[i][0]:
			a=pred[i][:]
			a.insert(0,1)
			cli[a[3]-1].append(a)
		else:
			if cli!=cle:
				for j in range(N):
					if cli[j]!=[]:
						crd.append(cli[j])
			cli=deepcopy(cle)
			a=pred[i][:]
			a.insert(0,1)
			cli[a[3]-1].append(a)

		pi=pred[i][0]

	for j in range(N):
		if cli[j]!=[]:
			crd.append(cli[j])


	# print len(crd)

	# for i in range(len(crd)):
	# 	print crd[i]


	# Finding cru

	cru=[]


	for i in range(len(crd)):
		cl=[]
		n=len(crd[i])
		if n>1:
			for j in range(n):
				for k in range(j+1,n):
					a=crd[i][j][:]
					b=crd[i][k][:]
					a[0]=-1
					b[0]=-1
					cru.append([a,b])

	# print len(cru)

	# for i in range(len(cru)):
	# 	print cru[i]


	# Finding cld

	pred.sort(key=lambda x: x[1])

	# print pred

	cld=[]

	pj=0
	cli=deepcopy(cle)

	for i in range(len(pred)):
		if pj==pred[i][1]:
			a=pred[i][:]
			a.insert(0,1)
			cli[a[3]-1].append(a)
		else:
			if cli!=cle:
				for j in range(N):
					if cli[j]!=[]:
						cld.append(cli[j])
			cli=deepcopy(cle)
			a=pred[i][:]
			a.insert(0,1)
			cli[a[3]-1].append(a)

		pj=pred[i][1]

	for j in range(N):
		if cli[j]!=[]:
			cld.append(cli[j])


	# print len(cld)

	# for i in range(len(cld)):
	# 	print cld[i]



	# Finding clu

	clu=[]


	for i in range(len(cld)):
		cl=[]
		n=len(cld[i])
		if n>1:
			for j in range(n):
				for k in range(j+1,n):
					a=cld[i][j][:]
					b=cld[i][k][:]
					a[0]=-1
					b[0]=-1
					clu.append([a,b])

	# print len(clu)

	# for i in range(len(clu)):
	# 	print clu[i]



	# Finding cbd

	pred.sort(key=lambda x: 0.95*(x[1]-(x[1]-1)%M)+1.05*(x[0]-(x[0]-1)%M))

	# print pred

	cbd=[]

	p=0
	cli=deepcopy(cle)

	for i in range(len(pred)):
		qq=0.95*(pred[i][1]-(pred[i][1]-1)%M)+1.05*(pred[i][0]-(pred[i][0]-1)%M)
		if p==qq:
			a=pred[i][:]
			a.insert(0,1)
			cli[a[3]-1].append(a)
		else:
			if cli!=cle:
				for j in range(N):
					if cli[j]!=[]:
						cbd.append(cli[j])
			cli=deepcopy(cle)
			a=pred[i][:]
			a.insert(0,1)
			cli[a[3]-1].append(a)

		p=0.95*(pred[i][1]-(pred[i][1]-1)%M)+1.05*(pred[i][0]-(pred[i][0]-1)%M)

	for j in range(N):
		if cli[j]!=[]:
			cbd.append(cli[j])


	# print len(cbd)

	# for i in range(len(cbd)):
	# 	print cbd[i]

	# finding cbu 

	cbu=[]

	for i in range(len(cbd)):
		cl=[]
		n=len(cbd[i])
		if n>1:
			for j in range(n):
				for k in range(j+1,n):
					a=cbd[i][j][:]
					b=cbd[i][k][:]
					a[0]=-1
					b[0]=-1
					cbu.append([a,b])

	# print len(cbu)

	# for i in range(len(cbu)):
	# 	print cbu[i]


	clause=[]

	clause=ccd+ccu+crd+cru+cld+clu+cbd+cbu

	return clause