# ----------------------------------------------------------
# HashTable Implementation in Python (Chaining Method)
# ----------------------------------------------------------
# What is a Hash Table?
# ---------------------
# A Hash Table stores key-value pairs and uses a hash function
# to map keys into indexes of an underlying array (buckets).
#
# Collision Handling (Chaining):
# ------------------------------
# - When two keys hash to the same index, we store them in a
#   list (bucket) at that index.
# - Example: "name" and "mean" may hash to the same index,
#   both values will live inside the same bucket.
#
# Pros of Chaining:
# -----------------
# Handles collisions gracefully (multiple keys per slot).
# Easy to implement.
# No clustering problem like linear probing.
#
# Cons of Chaining:
# -----------------
# Buckets can grow large → performance may degrade.
# Requires extra memory for linked lists/arrays in each bucket.
#
# Big-O Time Complexity (Average Case):
# -------------------------------------
# Insert   → O(1)   (amortized, if distribution is good)
# Search   → O(1)   (amortized)
# Delete   → O(1)   (amortized)
# Worst Case (if all keys go into one bucket) → O(n)
# ----------------------------------------------------------


class HashTable:
    def __init__(self, size=100):
        """
        Initialize HashTable with empty buckets.
        Note: Use list comprehension to create independent lists.
        """
        self.size = size
        self.data = [[] for _ in range(self.size)]  # avoid [[]] * size (shared refs!)

    def get_hash(self, key):
        """
        Simple hash function: sum ASCII values of chars, mod table size.
        :param key: string key
        :return: index in table
        """
        hash_key = 0
        for i in key:
            hash_key += ord(i)
        return hash_key % self.size

    def __setitem__(self, key, value):
        """
        Insert key-value pair into table.
        If key already exists, update its value.
        Otherwise, append new [key, value] to bucket.
        """
        index = self.get_hash(key)
        bucket = self.data[index]

        for i, kv in enumerate(bucket):
            if kv[0] == key:  # update existing key
                bucket[i][1] = value
                return
        bucket.append([key, value])  # insert new key-value pair

    def __getitem__(self, key):
        """
        Retrieve value for given key.
        Search only within its bucket.
        :return: value if found, -1 otherwise
        """
        index = self.get_hash(key)
        bucket = self.data[index]

        for k, v in bucket:
            if k == key:
                return v
        return -1

    def __delitem__(self, key):
        """
        Delete a key-value pair from table.
        Removes entry from bucket.
        """
        index = self.get_hash(key)
        bucket = self.data[index]

        for i, kv in enumerate(bucket):
            if kv[0] == key:
                del bucket[i]
                return


# ----------------------------------------------------------
# Example Usage
# ----------------------------------------------------------
if __name__ == "__main__":
    ht = HashTable()

    # Insert values
    ht["name"] = "Sabbir Mahmud"
    ht["mean"] = "Another key with same hash"  # Both may hash to same index

    # Retrieve values
    print(ht["name"])  # Sabbir Mahmud
    print(ht["mean"])  # Another key with same hash
