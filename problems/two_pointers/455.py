# problem: assign cookies
# link: https://leetcode.com/problems/assign-cookies/description/
# Difficulty: Easy

# Problem: 
# we have two lists one that holds child's greed size
# and second one that holds the cookies with their sizes.
# if the cookie is same or bigger than childrens greed meter,
# the child can accept it, otherwise it cannot.

# our task is to give every child possible cookies.

# Aproach: 
# doesnt really need that much thinking its obvious and easy, 
# can be done in better time complexity but maybe next time.

# test input
g = [1, 2, 3]
s = [1, 1]

def findContentChildren(g: list[int], s: list[int]) -> int:
    # need to be sorted to use pointers. 
    g.sort()
    s.sort()

    # we define to identical pointers because we need to compare each pair on our way.
    curr_child = 0
    curr_cookie = 0
    # containter to hold valid pairs of cookie and child
    valid = 0
    # until we run out of tries meaning if we exceed the length the program will run
    while curr_child < len(g) and curr_cookie < len(s):
        # if current cookie is same or larger than childs greed.
        if s[curr_cookie] >= g[curr_child]:
            # then we have one good pair 
            valid += 1
            # and we move on simoulteniosly.
            curr_child += 1
            curr_cookie += 1
        else:
            # if childs greed is bigger we only move on to next cookie, 
            # maybe next cookie will be same or bigger than childs greed
            curr_cookie += 1
    # simply return valid pairs
    return valid
# Time complexity: \(O(n \log n + m \log m)\)

