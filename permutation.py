#JST algorithm 




def extend(l,iObj):

	if l==[]:
		return [[1]]

	
	eList=[]
	oList=[]
	out=[]

	if len(l) ==1:
		eList=l[0]
		oList=l[0]
		#generate
		out.append(eList+[iObj])
		out.append([iObj]+oList)


		
	else:
		#even 
		eList=[l[n] for n in range(len(l)) if n %2 ==0   ]

		#odd
		oList=[l[n] for n in range(len(l)) if n %2 ==1   ]

		
		#insert eList
		for lObj in eList:
			for i in range(len(lObj),-1,-1):
				out.append( lObj[:i]+[iObj]+lObj[i:])

		for lObj in oList:
			for i in range(len(lObj)+1):
				out.append(lObj[:i]+[iObj]+lObj[i:])

	return out



def permutation(n):

	out=[]
	for n in range(1,n+1):
		out=extend(out,n)

	return out






for l in permutation(9):
	print l

