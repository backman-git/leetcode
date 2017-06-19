





key points:

	dict is good for implementation of tree!






import collections

class Solution(object):
	def killProcess(self, pid, ppid, kill):
		"""
		:type pid: List[int]
		:type ppid: List[int]
		:type kill: int
		:rtype: List[int]
		"""


		tree = collections.defaultdict(list)



		for p ,pp in zip(pid,ppid):
			tree[pp].append(p)

		
		res=[]
	
		queue=[kill]

		while len(queue)!=0:
			p=queue.pop(0)
			res.append(p)
			queue+=tree[p]




		return res





sol =Solution()

pid=[1,3,10,5]
ppid=[3,0,5,3]
kill=5
print sol.killProcess(pid,ppid,kill)