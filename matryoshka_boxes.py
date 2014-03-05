from box import Box

def largest_box_subset(boxes):
    """
    Given a list of 2-D boxes (see box class for details on boxes), use dynamic programming (with memoization) to find the size of the largest subset of these boxes such that box_1 fits inside of box_0, box_2 fits inside of box_1, ... box_n fits inside of box_n-1. Note you never have more than one box in each box (even if more than one box could fit). It is like you are finding the largest possible subset of boxes that form a matryoshka-doll-like set of boxes (http://en.wikipedia.org/wiki/Matryoshka_doll)! 
    
    Note a box does not fit into another box that is the same size, so a box with width 1 and height 1 would not fit into another box with width 1 and height 1. Similarly, a box of width 1 and height 1 doesn't fit into a box with width 1 and height 5 because their widths are the same. Also note that we do not care about the orientation of a box --- so a box with a width of 1 and height of 2 is the same as a box with a width of 2 and height of 1. Both of these boxes can fit into a box with a width of 3 and a height of 2. 
    
    >>> b = [Box(1,3), Box(4,2), Box(1,5), Box(6,2), Box(7,4),Box(2,6)]
    >>> largest_box_subset(b)
    3
    >>> b = [Box(0,0), Box(1,1), Box(2,2)]
    >>> largest_box_subset(b)
    3
    >>> b = [Box(0,0), Box(0,1), Box(0,2)]
    >>> largest_box_subset(b)
    1
    
    """
    #fill in your definition of largest_box_subset here. Feel free to write any auxillary functions you feel will help you/make your code cleaner. Remember, these doctests are not exhaustive. Additionally, docstrings are not usually enough: you will likely want to include inline comments to help explain what your code is doing. REMEMBER: your solution must use dynamic programming and memoization.

    pass


        
                
