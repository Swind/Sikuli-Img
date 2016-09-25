class Finder:
    def next(self):
        raise NotImplementedError("Subclasses should implement this!")

    def __iter__(self):
        return self

    def __next__(self):
        item = self.next()

        if item is None:
            raise StopIteration
        else:
            return item
