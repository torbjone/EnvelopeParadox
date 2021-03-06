#This is a simulation to solve the two envolope paradox
from random import choice, randint, shuffle
import pylab
import numpy as np

def return_double_or_half(orig_value):
    return choice([.5, 2.]) * orig_value

def choise_test():
    n_steps = 10000
    keep_env_value = 0
    change_env_value = 0
    num_first_val_greater_than_second = 0
    v0_vals = []
    v1_vals = []
    for n in xrange(n_steps):
        start_value = randint(1,1000)
        values = [start_value, return_double_or_half(start_value)]
        if values[0] >values[1]:
            num_first_val_greater_than_second += 1
        # The following is the critical line. If it is commented
        # out, you choud change envelope. If not it doesn't matter!
        #shuffle(values) 
        keep_env_value += values[0]
        change_env_value += values[1]

        v0_vals.append(values[0])
        v1_vals.append(values[1])
    print change_env_value/keep_env_value
    print 'Prop value[0] > value[1]', float(num_first_val_greater_than_second) / n_steps

    f = pylab.figure()
    ax = f.add_subplot(111)
    bins = np.linspace(0,2000,num=20)
    ax.hist(v0_vals, bins=bins, alpha=0.4, label='Dist of V[0]')
    ax.hist(v1_vals, bins=bins, alpha=0.4, label='Dist of V[1]')
    ax.legend()
    pylab.show()

if __name__ == '__main__':
    choise_test()
