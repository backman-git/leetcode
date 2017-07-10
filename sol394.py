class Solution(object):
	
	def decodeString(self, s):
		res=""
		ptr1=0
		while ptr1 <len(s):
			if s[ptr1] =="[":
				nPtr=ptr1-1
				nStr=""
				while nPtr>=0 and s[nPtr].isdigit() :
					nStr=s[nPtr]+nStr
					nPtr-=1
				n=int(nStr)
				content=""
				ptr2=ptr1+1
				cnt=1
				while not(s[ptr2]==']' and cnt==1) :
					if s[ptr2]=='[':
						cnt+=1
					elif s[ptr2]==']':
						cnt-=1
					content+=s[ptr2]
					ptr2+=1	
				res+=self.decodeString(content)*n	
				ptr1=ptr2
			elif s[ptr1].isdigit() is False:
				res+=s[ptr1]
			ptr1+=1
		return res

sol =Solution()

print sol.decodeString("100[leetcode]")