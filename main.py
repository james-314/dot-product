# import dataclass to reduce the amount of "stuff" involved in our class.  
from dataclasses import dataclass
import numpy
import time

@dataclass(frozen=True)  # frozen=True makes the class immutable.
class Vector:
    """
    A representation of 3D cartesian vector.
    """

    x: float = 0
    y: float = 0
    z: float = 0

    @staticmethod
    def dot_product(a: 'Vector', b: 'Vector') -> float:
        """
        Calculate the dot (scalar/inner) product, a.b of two vectors.
        """
        return a.x * b.x + a.y * b.y + a.z * b.z


def main_func():
    # Create two test vectors
    a = Vector(1.23, 2.6574, 3.0)
    b = Vector(-4.0, 5.5, -6.9)

    # Prove that the calculation is as expected
    print("The dot product of {0} and {1} is {2}".format(a, b, Vector.dot_product(a, b)))

    # Test for execution time
    start_time = time.time_ns()
    for i in range(0, 1000000):
        Vector.dot_product(a, b)
    end_time = time.time_ns()

    print("Time for 1,000,000 iterations of the calculation {} ms".format((end_time - start_time) / 1000000))

    # Numpy test

    # Create two test vectors
    a = numpy.array([1.23, 2.6574, 3.0], dtype=numpy.float64)
    b = numpy.array([-4.0, 5.5, -6.9], dtype=numpy.float64)

    # Prove that the calculation is as expected
    print("The dot product of {0} and {1} is {2}".format(a, b, numpy.dot(a, b)))

    # Test for execution time
    start_time = time.time_ns()
    for i in range(0, 1000000):
        numpy.dot(a, b)
    end_time = time.time_ns()

    print("Time for 1,000,000 iterations of the numpy calculation {} ms".format((end_time - start_time) / 1000000))

if __name__ == "__main__":
    main_func()
