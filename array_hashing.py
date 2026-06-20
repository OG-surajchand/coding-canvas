"""
1. Two Sum
Problem Statement: Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Examples:

Input: nums = [2, 7, 11, 15], target = 9

Output: [0, 1] (Because nums[0] + nums[1] == 9)

Input: nums = [3, 2, 4], target = 6

Output: [1, 2]

Constraints:

2 <= nums.length <= 10^4

-10^9 <= nums[i] <= 10^9

-10^9 <= target <= 10^9
"""
def two_sum(nums, target):
    accessed_num = set()

    for i, num in enumerate(nums):
        complement = target - num


        if complement not in accessed_num:
            accessed_num.add(num)
        else:
            return [i, nums.index(complement)]
        
result = two_sum(nums = [3, 2, 4], target = 6)
print(result)

"""
2. Contains Duplicate
Problem Statement: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Examples:

Input: nums = [1, 2, 3, 1]

Output: true

Input: nums = [1, 2, 3, 4]

Output: false

Constraints:

1 <= nums.length <= 10^5

-10^9 <= nums[i] <= 10^9
"""

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return True
    return False

result = contains_duplicate(nums = [1, 2, 3, 1])
print(result)

"""
3. Valid Anagram
Problem Statement: Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Examples:

Input: s = "anagram", t = "nagaram"

Output: true

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 10^4

s and t consist of lowercase English letters.
"""

def is_anagram(source: str, target: str) -> bool:
    if len(source) != len(target):
        return False

    if sorted(source.lower()) == sorted(target.lower()):
        return True
    else:        
        return False

result = is_anagram(source = "rat", target = "car")
print(result)

"""
4. Group Anagrams
Problem Statement: Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Examples:

Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Input: strs = [""]

Output: [[""]]

Constraints:

1 <= strs.length <= 10^4

0 <= strs[i].length <= 100

strs[i] consists of lowercase English letters.
"""
def group_anagrams(input_list: list[str]) -> list[list[str]]:
    anagrams = {}

    for words in input_list:
        key = "".join(sorted(words.lower()))
        if key not in anagrams:
            anagrams[key] = [words]
        else:
            anagrams[key].append(words)
    
    return list(anagrams.values())
result = group_anagrams(input_list = ["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)
"""
1. Two Sum
Problem Statement: Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Examples:

Input: nums = [2, 7, 11, 15], target = 9

Output: [0, 1] (Because nums[0] + nums[1] == 9)

Input: nums = [3, 2, 4], target = 6

Output: [1, 2]

Constraints:

2 <= nums.length <= 10^4

-10^9 <= nums[i] <= 10^9

-10^9 <= target <= 10^9
"""
def two_sum(nums, target):
    accessed_num = set()

    for i, num in enumerate(nums):
        complement = target - num


        if complement not in accessed_num:
            accessed_num.add(num)
        else:
            return [i, nums.index(complement)]
        
result = two_sum(nums = [3, 2, 4], target = 6)
print(result)

"""
2. Contains Duplicate
Problem Statement: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Examples:

Input: nums = [1, 2, 3, 1]

Output: true

Input: nums = [1, 2, 3, 4]

Output: false

Constraints:

1 <= nums.length <= 10^5

-10^9 <= nums[i] <= 10^9
"""

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return True
    return False

result = contains_duplicate(nums = [1, 2, 3, 1])
print(result)

"""
3. Valid Anagram
Problem Statement: Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Examples:

Input: s = "anagram", t = "nagaram"

Output: true

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 10^4

s and t consist of lowercase English letters.
"""

def is_anagram(source: str, target: str) -> bool:
    if len(source) != len(target):
        return False

    if sorted(source.lower()) == sorted(target.lower()):
        return True
    else:        
        return False

result = is_anagram(source = "rat", target = "car")
print(result)

"""
4. Group Anagrams
Problem Statement: Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Examples:

Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Input: strs = [""]

Output: [[""]]

Constraints:

1 <= strs.length <= 10^4

0 <= strs[i].length <= 100

strs[i] consists of lowercase English letters.
"""
def group_anagrams(input_list: list[str]) -> list[list[str]]:
    anagrams = {}

    for word in input_list:
        key = tuple(sorted(word.lower()))
        
        if key not in anagrams:
            anagrams[key] = [word]
        else:
            anagrams[key].append(word)
    
    return anagrams

result = group_anagrams(input_list=["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)

def statistics_calculation(input_data):
    obj = {}

    for item in input_data:
        if item not in obj:
            obj[item] = 1
        else:
            obj[item] += 1

    return obj

result = statistics_calculation([1,2,4,4,4,5,6,7,8,9,1,2,3,4])
print(result)