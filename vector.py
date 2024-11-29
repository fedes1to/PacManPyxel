# Demasiado cansado de que los vectores sean listas de 2 elementos, decidi hacer una clase que represente un vector de dos dimensiones.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, vector):
        return self.x == vector.x and self.y == vector.y

    def __ne__(self, vector):
        return self.x != vector.x or self.y != vector.y

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        return Vector(int(self.x // scalar), int(self.y // scalar))

    def __mod__(self, scalar):
        return Vector(self.x % scalar, self.y % scalar)

    def __pow__(self, scalar):
        return Vector(self.x ** scalar, self.y ** scalar)

    def __abs__(self):
        return Vector(abs(self.x), abs(self.y))

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __pos__(self):
        return Vector(+self.x, +self.y)

    def __iadd__(self, vector):
        self.x += vector.x
        self.y += vector.y
        return self

    def __isub__(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        return self

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    def __itruediv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        return self

    def __ifloordiv__(self, scalar):
        self.x = int(self.x // scalar)
        self.y = int(self.x // scalar)
        return self

    def rounded(self):
        return Vector(int(round(self.x)), int(round(self.y)))
    
    def floored(self):
        return Vector(int(self.x // 1), int(self.y // 1))
    
    def normalized(self):
        return self / abs(self.magnitude())
    
    def distance_to(self, vector):
        return abs(self - vector)
    
    def dot(self, vector):
        return self.x * vector.x + self.y * vector.y
    
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __le__(self, other):
        return self.magnitude() <= other.magnitude()

    def __gt__(self, other):
        return self.magnitude() > other.magnitude()

    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __hash__(self):
        return hash((self.x, self.y))