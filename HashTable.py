# Jimmy Nguyen
# Student ID: 000579757


# a chaining hash table for when you want the key to be another property
class ChainingHashTable:

    # creates a new chaining hash table with a size of 40
    def __init__(self, initial_cap=40):
        self.table = [];
        for i in range(initial_cap):
            self.table.append([])

    # inserts the key after getting a bucket
    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        self.table[bucket].append(value)

    # returns the key by using a get
    def get(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        matching_list = self.table[bucket]

        # returns the whole matching list
        return matching_list


# a directly mapped hash table
# this works best for ID when it does not collide
class DirectHashTable:

    # creates an initial table of size 40
    def __init__(self, initial_cap=40):
        self.length = 0;
        self.package_list = [];
        for i in range(initial_cap):
            self.package_list.append(None)

    # maps the id directly to key, increases if the key is greater than length
    def put(self, idx, package):
        if idx > self.package_list.__len__():
            self.package_list = self.package_list[:idx]
        self.package_list[idx-1] = package
        self.length += 1

    # returns the package with the specific key
    def get(self, idx):
        return self.package_list[idx - 1]

    # removes the package itself
    def remove(self, idx):
        self.package_list[idx-1] = None;
        self.length -= 1;
