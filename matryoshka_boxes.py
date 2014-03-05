from box import Box

def largest_box_subset(baby_boxes, mama_box, memo = None):
    """ 
    Given a tuple of 2-D boxes stored in baby_boxes (see box class for details
    on boxes), use dynamic programming (with memoization) to find the size of
    the largest subset of these boxes that will fit inside of the mama_box
    such that box_1 fits inside of box_0, box_2 fits inside of box_1, ...
    box_n fits inside of box_n-1 and box_n fits in mama_box. Note you never
    have more than one box in each box (even if more than one box could fit).
    It is like you are finding the largest possible subset of boxes that form
    a matryoshka-doll-like set of boxes
    (http://en.wikipedia.org/wiki/Matryoshka_doll)! (this is why we refer to
    them as mama and baby boxes --- the outermost box is the mama box and each
    of the boxes layered inside are the babies)
    
     Note a box does not fit into another box that is the same size, so a box
    with width 1 and height 1 would not fit into another box with width 1 and
    height 1. Similarly, a box of width 1 and height 1 doesn't fit into a box
    with width 1 and height 5. Also note that we do not care about the
    orientation of a box --- so a box with a width of 1 and height of 2 is the
    same as a box with a width of 2 and height of 1. Both of these boxes can
    fit into a box with a width of 3 and a height of 2.
    
     We can think of this problem recursively. If no baby_boxes fit in the
    mama_box, the answer is 1. Otherwise, for each baby box that fits in
    mama_box, recursively find the largest box subset that starts at that baby
    box and add 1 (for the enclosing mama box). More explicitly, the
    recurrence for this function is:
    
    largest_box_subset(baby_boxes, mama_box) =:
        1 if no box fits in mama_box
        or
        1 + max(largest_box_subset(baby_boxes, child)) over all child boxes that possibly fit in mama_box
        
    memo is a dictionary that you can use to make your solution use
    memoization.
        
    >>> b = (Box(1,3), Box(4,2), Box(1,5), Box(6,2), Box(7,4),Box(2,6))
    >>> largest_box_subset(b,Box(8,8))
    4
    >>> b = (Box(0,0), Box(1,1), Box(2,2))
    >>> largest_box_subset(b,Box(3, 3))
    4
    >>> largest_box_subset(b,Box(0,0))
    1
    >>> b = (Box(0,0), Box(0,1), Box(0,2))
    >>> largest_box_subset(b,Box(3,3))
    2
    >>> largest_box_subset((Box(2,2), Box(1,1), Box(0,0)), Box(3, 3))
    4
    """
    # fill in your definition of largest_box_subset here. Feel free to write
    # any auxillary functions you feel will help you/make your code cleaner.
    # Remember, these doctests are not exhaustive. Additionally, docstrings are
    # not usually enough: you will likely want to include inline comments to
    # help explain what your code is doing. REMEMBER: your solution must use
    # dynamic programming and memoization.
    
    #memo is a dictionary that you can use to make your solution use memoization
    if not memo:
        memo = {}

    pass
