LINK TIL LEETCODE https://leetcode.com/

#oppgaver gjort på leetcode med full forståelse
#quest1 arrays (restore finishing order)
#my answer
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends = set(friends)
        result = []
        
        for person in order:
            if person in friends:
                result.append(person)
        return result

#quest2 arrays (shuffle the array)
#my answer
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for i in range(n):
            answer.append(nums[i])
            answer.append(nums[i + n])
        return answer

#quest3 arrays (max consecutive ones)
#my anwer
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        largest_streak_counter = 0
        streak_counter = 0
        
        for num in nums:
            if num == 0:
               streak_counter = 0
            elif num == 1:
                streak_counter = streak_counter + 1
                if streak_counter > largest_streak_counter:
                    largest_streak_counter = streak_counter
        return largest_streak_counter

#quest1 arrays2 (set mismatch)
#my answer
from collections import Counter

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counts = Counter(nums)

        duplicate = -1
        missing = 1

        for i in range(1, n + 1):
            if counts[i] == 2:
                duplicate = i
            elif counts[i] == 0:
                missing = i
        return [duplicate, missing]



HASH

#quest1 hash (restore finishing order)
#my answer
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends = set(friends)
        result = []
        
        for person in order:
            if person in friends:
                result.append(person)
        return result

    
