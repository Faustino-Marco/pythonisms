def annoy(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        normal_return = func(*args, **kwargs)
        annoying = "I know you are but what am I??"
        return annoying

def fight_starter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
    normal_return = func(*args, **kwargs)
    fightfightfight = "You want a knuckle sandwich?"
    return fightfightfight

## followed lecture below for reference
################################
class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection): # [a,b,c] => [a] -> [b] -> [c] -> None
                self.insert(item)


    def __iter__(self):

        def value_generator():

            current = self.head

            while current:

                yield current.value

                current = current.next

        return value_generator()

    def __str__(self):

        out = ""

        for value in self:
            out += f"[ {value} ] -> "

        return out + "None"

    def __len__(self):
        # DANGER: not O(1) - better IRL to track a self.length
        return len(list(iter(self)))

    def __eq__(self, other):
        # consider https://docs.python.org/3/library/functools.html#functools.total_ordering for Data collections
        return list(self) == list(other)

    def __getitem__(self, index):

        # return list(self)[index]

        # IF you have an efficient way to track length then check here
        # if len(self):
        #     raise IndexError

        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError
