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
