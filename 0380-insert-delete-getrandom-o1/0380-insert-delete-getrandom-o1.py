class RandomizedSet(object):

    def __init__(self):
        self.vals = []
        self.val_to_index = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_index:
            return False
        # Append to the end of array and record its index in the map
        self.val_to_index[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_index:
            return False

        # Get index of the element to remove and the last element
        idx_to_remove = self.val_to_index[val]
        last_val = self.vals[-1]

        # Move the last element to the slot of the element to remove
        self.vals[idx_to_remove] = last_val
        self.val_to_index[last_val] = idx_to_remove

        # Remove the last element from array and target from map
        self.vals.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()