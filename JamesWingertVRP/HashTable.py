#James Wingert #001424955
class HashTableEntry:

    def __init__(self, key, item):
        self.key = key
        self.item = item


class HashTable:

    # Constructor
    # Space-time complexity is O(1)
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    # private getter to create a hash key and assign the bucket position
    # Space-time complexity is O(1)
    def _get_hash_pos(self, key):
        bucket = int(key) % len(self.map)
        return bucket

    # Delete a value from the hash table
    # runtime is O(N)
    def delete(self, key):
        hash_key = self._get_hash_pos(key)

        if self.map[hash_key] is None:
            return False
        for i in range(0, len(self.map[hash_key])):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key].pop(i)
                return True
        return False

    # Insert a new package value into the hash table
    # Space-time complexity is O(N)
    def insert(self, key, value):
        hash_key = self._get_hash_pos(key)
        key_value = [key, value]

        if self.map[hash_key] is None:
            self.map[hash_key] = list([key_value])
            return True
        else:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[hash_key].append(key_value)
            return True

    # Space-time complexity is O(N)
    def update(self, key, value):
        hash_key = self._get_hash_pos(key)
        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print(key + 'can not be updated')

    # Retrieve value from table
    # Space-time complexity is O(N)
    def get(self, key):
        hash_key = self._get_hash_pos(key)
        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    return pair[1]
        return None


