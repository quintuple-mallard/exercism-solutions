class CustomSet:
    def __init__(self, elements = None):
        self._elems = []
        if elements is None:
            elements = []
        for item in elements:
            if item not in self._elems:
                self._elems.append(item)

    def isempty(self):
        return not len(self._elems)

    def __contains__(self, element):
        return element in self._elems

    def issubset(self, other):
        return all(item in other for item in self._elems)

    def isdisjoint(self, other):
        return not any(item in other for item in self._elems)

    def __eq__(self, other):
        return self.issubset(other) and len(self._elems) == len(other._elems)

    def add(self, element):
        if element not in self._elems:
            self._elems.append(element)
            self._elems = sorted(self._elems)

    def intersection(self, other):
        return CustomSet(item for item in self._elems if item in other._elems)

    def __sub__(self, other):
        return CustomSet(item for item in self._elems if item not in other._elems)

    def __add__(self, other):
        return CustomSet(self._elems + other._elems)
