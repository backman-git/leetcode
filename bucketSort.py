




ary = [22,45,12,8,10,6,72,81,33,18,50,14]

def bucketSort(ary):


	#divider can be loose~


	Bucket = [[] for i in range(10)]

	minV = min(ary)
	maxV = max(ary)

	for v in ary:
		#divider =10
		Bucket[v/10].append(v)

	Bucket=map(sorted,Bucket)

	Bucket = reduce(lambda res ,x: res+x ,Bucket,[]   )

	return Bucket


print bucketSort(ary)
