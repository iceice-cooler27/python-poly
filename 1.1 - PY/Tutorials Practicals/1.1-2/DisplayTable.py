import math

#Header
print("{:6} {:6} {:11} {:7}" \
      .format("Number", "Square", "Square Root", "English"))

#Content
print("{:6d} {:6.0f} {:11.2f} {:>7}" \
      .format(1, math.pow(1,2), math.sqrt(1), "One"))
print("{:6d} {:6.0f} {:11.2f} {:>7}" \
      .format(2, math.pow(2,2), math.sqrt(2), "Two"))
print("{:6d} {:6.0f} {:11.2f} {:>7}" \
      .format(3, math.pow(3,2), math.sqrt(3), "Three"))
print("{:6d} {:6.0f} {:11.2f} {:>7}" \
      .format(4, math.pow(4,2), math.sqrt(4), "Four"))
print("{:6d} {:6.0f} {:11.2f} {:>7}" \
      .format(5, math.pow(5,2), math.sqrt(5), "Five"))
