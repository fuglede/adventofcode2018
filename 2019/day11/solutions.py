from collections import defaultdict
import os
from vm import VM


with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
    ns = list(map(int, f.read().split(',')))


def get_colors(initial):
    vm = VM([], ns)
    d = -1j
    loc = 0
    colors = defaultdict(int)
    colors[0] = initial
    try:
        while True:
            vm.add_input(colors[loc])
            colors[loc] = next(vm)
            d *= 1j if next(vm) else -1j
            loc += d
    except StopIteration:
        return colors


# Part one
print(len(get_colors(0)))

# Part two
c = get_colors(1)
reals = set(int(z.real) for z in c)
imags = set(int(z.imag) for z in c)
print('\n'.join(
        ''.join('#' if c[x+y*1j] else ' '
                for x in range(min(reals), max(reals)+1))
      for y in range(min(imags), max(imags)+1)))