# Longest Substring Without Repeating Characters
# Given a string s, find the length of the *longest* substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

from turtle import left


def lengthOfLongestSubstring(str):

    charSet = set()

    leftPointer = 0
    resLength = 0

    for r in range(len(str)):

        while (str[r] in charSet):
            leftPointer += 1
            charSet.remove(str[leftPointer])

        charSet.add(str[r])
        resLength = max(resLength, r - leftPointer + 1)

    print(charSet)
    return resLength


# print(lengthOfLongestSubstring('abcabcbb'))

# ----------------------------------------------------------------


def lengthOfLongestSubstring2(s):
    substring = ''  # the substring being checked
    longest = 0  # length of the longest substring
    for char in s:
        substring += char  # append char in substring
        if substring.count(char) > 1:  # check repeat
            # if char is repeating,
            # substring = substring starts with an index without the FIRST encountered repeated character
            # example:
            # s = 'asjrgapa'
            # when substring = 'asjrga' ---> substring = 'sjrga' on the next substring = 'sjrgap' ...
            substring = substring[substring.index(char)+1:]
        longest = len(substring) if longest < len(
            substring) else longest  # check len is longest

    print(substring)
    return longest


# print(lengthOfLongestSubstring2('abcabcbb'))

# ----------------------------------------------------------------


def lengthOfLongestSubstring3(s):
    n = len(s)
    dict1 = set()
    left = 0
    right = 0
    res = 0
    save = set()

    while right < n:

        if s[right] not in dict1:
            dict1.add(s[right])
            res = max(res, right-left+1)
            right += 1
        else:
            if (len(save) < len(dict1)):
                save = dict1.copy()
            dict1.remove(s[left])
            left += 1

    print("save", save)
    return res


print(lengthOfLongestSubstring3('abcabcbb'))
