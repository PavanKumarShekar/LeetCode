class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		#longest = ""
		start = 0
		end = 0
		for i in range (len(s)):
			left,right = self.helper(s,i,i)
			if right-left > end-start:
				start = left
				end = right
			left,right = self.helper(s,i,i+1)
			if right-left > end-start:
				start = left
				end = right
		return s[start: end+1]
			
		
	def helper(self,s,i,j):
		if j >= len(s):
			return(0,0)
		
		start = i
		end = j
		while start>=0 and end < len(s) and s[start] == s[end]:
			start-=1
			end+=1
		return (start+1,end-1)

def main():
    object1 = Solution()
    output = object1.longestPalindrome("babad")
    print (output)


if __name__ == "__main__":
    main()
