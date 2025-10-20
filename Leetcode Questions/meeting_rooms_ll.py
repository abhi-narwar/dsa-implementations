class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        n=len(start)
        rooms=0
        max_rooms=0
        i,j=0,0
        
        while i<n and j<n:
            if start[i]<end[j]:
                rooms+=1
                i+=1
                max_rooms=max(rooms,max_rooms)
            else:
                rooms-=1
                j+=1
        return max_rooms
        
        
