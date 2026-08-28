"""Lesson: a closure remembers values from its enclosing function.

Objective: create a small stateful callable and identify where its state lives.
Mental model: the returned function carries a backpack of captured values.
"""

def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))
print(triple(5))

# Active recall: why can multiply still read factor after make_multiplier ends?