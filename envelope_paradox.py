#This is a simulation to solve the two envolope paradox
from random import choice

def return_double_or_half(orig_value):
    return choice([.5, 2]) * orig_value

def expectation_value_test():
    a = 10
    n_steps = 10000
    keep_env_value = 0
    change_env_value = 0
    for n in xrange(n_steps):
        keep_env_value += a
        change_env_value += return_double_or_half(a)
    print change_env_value/keep_env_value

if __name__ == '__main__':
    expectation_value_test()
