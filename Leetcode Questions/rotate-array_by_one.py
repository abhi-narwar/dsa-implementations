class Solution:
    def rotate(self, arr):
        
        self.reverse(arr,0,len(arr)-1)
        self.reverse(arr,1,len(arr)-1)
    
        
        
    def reverse(self,arr,i,j):
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        
        
        
    
