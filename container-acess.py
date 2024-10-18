class MyContainer:

    def __init__(self):
        self._mylist = [1, 2, 3, 4, 5]
        self._mydict = {'a': 1, 'b': 2, 'c': 3}
        self._myset = {1, 2, 3, 4, 5}

    def get_set(self):
        return self._myset

    def get_list(self):
        return self._mylist
    def __getitem__(self, index):
        return self._mylist[index]
    def get_dict(self):
        return self._mydict

    def get_set(self):
        return self._myset
    def add_to_list(self, value):
        self._mylist.append(value)

    def remove_from_list(self, value):
        self._mylist.remove(value)

    def add_to_dict(self, key, value):
        self._mydict[key] = value

    def remove_from_dict(self, key):
        del self._mydict[key]

    def add_to_set(self, value):
        self._myset.add(value)

    def remove_from_set(self, value):
        self._myset.remove(value)

    def get_set(self):
        return self._myset

    def get_list(self):
        return self._mylist

    def get_dict(self):
        return self._mydict

    def get_set(self):
        return self._myset
    
c1 = MyContainer()
print(c1[0])