#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sys

# get sigma from command line
if len(sys.argv) != 3:
    print('Usage: python3 plot-dynamic.py sigma output-file')
    sys.exit(1)

sigma = float(sys.argv[1])

# generate data with given sigma
x = np.linspace(0, 1, 100)
y = np.exp(sigma * x)

# plot data
plt.plot(x, y, 'r-', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = exp(' + str(sigma) + 'x)')

# save plot to file
plt.savefig('figs/dynamic_sigma=' + str(sigma) + '.pdf', bbox_inches='tight', format='pdf')
