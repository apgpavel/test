#pass test 12 minutes

from itertools import accumulate

class MovingTotal:
    def __init__(self, *args, **kwargs):
        self.box = list(args)
        self._cache = 0

    def append(self, numbers):
        for item in numbers:
            self.box.append(item)
            self._cache = set(accumulate(self.box))
            self._last = sum(self.box)
        self.box.pop(0)

    def contains(self, total):
        return total in self._cache

movingtotal = MovingTotal()
movingtotal.append([1, 2, 3])
print(movingtotal.contains(6))
print(movingtotal.contains(9))
movingtotal.append([4])
print(movingtotal.contains(9))
