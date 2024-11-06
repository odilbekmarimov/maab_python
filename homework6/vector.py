from __future__ import annotations
from math import sqrt

class Vector:
    def __init__(self, *components: float):
        self.components = list(components)
    
    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"
    
    def __bool__(self):
        return any(component != 0 for component in self.components)
    
    def __add__(self, vector2: Vector):
        if len(self.components) == len(vector2.components):
            return Vector(*(a + b for a, b in zip(self.components, vector2.components)))
        else:
            raise ValueError("Vector lengths do not match")
        
    def __sub__(self, vector2: Vector):
        if len(self.components) == len(vector2.components):
            return Vector(*(a - b for a, b in zip(self.components, vector2.components)))
        else:
            raise ValueError("Vector lengths do not match")
    
    def __mul__(self, other):
        if isinstance(other, Vector) and len(self.components) == len(other.components): 
            return Vector(*(a * b for a, b in zip(self.components, other.components)))
        elif isinstance(other, (int, float)):
            return Vector(*(component * other for component in self.components))
        else:
            raise ValueError("Vector lengths do not match")
        
    def __eq__(self, vector2: Vector):
        if len(self.components) != len(vector2.components):
            raise ValueError("Vectors must be of the same length.")
        return all(a == b for a, b in zip(self.components, vector2.components))
    
    def __getitem__(self, index):
        return self.components[index]
    
    def __setitem__(self, index, value):
        self.components[index] = value
        
    def __len__(self):
        return len(self.components)
    
    def __neg__(self):
        return Vector(*(-component for component in self.components))
    
    def __abs__(self):
        return sqrt(sum(component ** 2 for component in self.components))
    
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(*(a / scalar for a in self.components))
        else:
            return NotImplemented



#############################
# Instantiation
v1 = Vector(1, 4, 6)
print(v1)              # Expected Output: Vector(1, 4, 6)

# Boolean Evaluation
print(bool(v1))        # Expected Output: True
print(bool(Vector(0, 0)))  # Expected Output: False

# Length
print(len(v1))         # Expected Output: 3

# Indexing and Slicing
print(v1[1])           # Expected Output: 4
v1[1] = 10
print(v1)              # Expected Output: Vector(1, 10, 6)

# Vector Arithmetic
v2 = Vector(3, 7, 2)
print(v1 + v2)         # Expected Output: Vector(4, 17, 8)
print(v1 - v2)         # Expected Output: Vector(-2, 3, 4)
print(v1 * v2)         # Expected Output: Vector(3, 70, 12)

# Scalar Multiplication and Division
print(v1 * 3)          # Expected Output: Vector(3, 30, 18)
print(v1 / 2)          # Expected Output: Vector(0.5, 5, 3)

# Absolute Value (Norm)
print(abs(v1))         # Expected Output: √(1^2 + 10^2 + 6^2) = 11.66...

# Equality Comparison
print(v1 == Vector(1, 10, 6))  # Expected Output: True

# Negation
print(-v1)             # Expected Output: Vector(-1, -10, -6)
