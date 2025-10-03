#  Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them. 
class Vector:
    def __init__(self, components):
        self.components = components   # list ya tuple

    def __add__(self, other):
        # element-wise addition
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        # dot product
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product")
        result = sum(a * b for a, b in zip(self.components, other.components))
        return result

    def __str__(self):
        return f"Vector({self.components})"


# Example usage
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("v1 + v2 =", v1 + v2)       # Vector([5, 7, 9])
print("v1 · v2 =", v1 * v2)       # 32
