
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

class BoxValueError(Exception):
    pass

class Box:
    def __init__(self, dim1,dim2):
        """
        A 2-dimensional box, where dim1 is the length of the first dimension of the box and box.dim2 is the length of the second dimension. You can interpret this loosly as the width and height of the box, but we use the boxes without regard to orientation. 
        
        >>> b = Box(3,4)
        >>> print(b)
        (3,4)
        >>> b.dim1
        3
        >>> b.dim2
        4
        >>> b = Box(-1,-2)
        Traceback (most recent call last):
            ...
        matryoshka_boxes.BoxValueError: Tried to create a box with negative dimensions
        """
        if (dim1 <0 or dim2 < 0):
            raise(BoxValueError("Tried to create a box with negative dimensions")) 
        self.dim1 = dim1
        self.dim2 = dim2
        
    def __str__(self):
        return "({},{})".format(self.dim1, self.dim2)
        
    def __repr__(self):
        return "({},{})".format(self.dim1, self.dim2)    
        
    def __lt__(self, b):
        """
        Returns true or false, depending upon if box self will fit into box b or not. Note that if the boxes are the same size, this will return false as one does not fit INTO another. 
        Note when we compare boxes, we do not care about their orientation, we only care about whether or not self fits inside of b (ie if we can rotate the box in any way such that the width of self is less than the width of b and the height of self is less than the height of b)
        """
        return (min(self.dim1, self.dim2) < min(b.dim1,b.dim2) ) and (max(self.dim1,self.dim2) < max(b.dim1,b.dim2))

        
                
