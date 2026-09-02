# --------------------------------
# DESCRIPTION
# --------------------------------

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.



# ----------------------------------
# CODE FOR TASK
# ----------------------------------
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len = len(s)
        t_len = len(t)
        count_s = {}
        count_t = {}
        if s_len == t_len:
            for i in range(len(s)):
                count_s[s[i]] = count_s.get(s[i], 0) + 1
                count_t[t[i]] = count_t.get(t[i], 0) + 1 
            return count_s == count_t
        else:
            return False

        



