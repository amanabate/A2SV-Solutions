# Problem:  Boats to Save People - https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        
        for _ in range(len(people)):
            if left > right:
                break

            if people[left] + people[right] <= limit:
                left += 1
                
            right -= 1
            boats += 1
        
        return boats