#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        dict = {}
        for name in arr:
            dict[name] = 0
        for name in arr:
            dict[name]+=1
        max = 0
        for name in arr:
            if dict[name]>max: max = dict[name]
        res = []
        for name in arr:
            if dict[name] == max:
                res.append(name)
        return sorted(res)[0]
    
sol = Solution()


arr = ["john","johnny","jackie","johnny","john","jackie","jamie","jamie","john","johnny","jamie","johnny","john"]
print(sol.winner(arr,len(arr)))