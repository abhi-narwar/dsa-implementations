class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        def merge_sort(sums):
            if len(sums) <= 1:
                return 0, sums
                
            mid = len(sums) // 2
            count_left, left = merge_sort(sums[:mid])
            count_right, right = merge_sort(sums[mid:])
            count = count_left + count_right

            
            j = k = 0
            for left_val in left:
                while k < len(right) and right[k] - left_val < lower:
                    k += 1
                while j < len(right) and right[j] - left_val <= upper:
                    j += 1
                count += j - k

           
            merged = sorted(left + right)
            return count, merged

     
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        count,_ = merge_sort(prefix)
        return count