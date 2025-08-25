# ----------------------------------------------------------
# HashTable Implementation with Linear Probing in Python
# ----------------------------------------------------------
# What is a Hash Table?
# ---------------------
# A Hash Table is a data structure that stores key-value pairs.
# It uses a "hash function" to convert the key into an index in an array.
# This makes data insertion, retrieval, and deletion very fast (O(1) average).
#
# Problem: Collisions
# -------------------
# A "collision" occurs when two different keys hash to the same index.
# Example: "name" and "mean" both produce the same hash index.
#
# Solution: Linear Probing (Open Addressing)
# ------------------------------------------
# Linear Probing resolves collisions by checking the *next slot* in the array
# until an empty slot is found. This avoids overwriting data.
#
# Pros of Linear Probing:
# -----------------------
# Simple to implement
# Cache-friendly (sequential memory access)
#
# Cons of Linear Probing:
# -----------------------
# Primary clustering (long chains of occupied slots form, making searches slower)
# Deletion requires care (tombstones are usually used; here we do a simplified version)
#
# Big-O Time Complexity (with linear probing):
# --------------------------------------------
# Insert   → O(1) average, O(n) worst-case
# Search   → O(1) average, O(n) worst-case
# Delete   → O(1) average, O(n) worst-case
# Space    → O(n)
# ----------------------------------------------------------


class HashTable:
    def __init__(self, size=100):
        """
        Initialize the hash table with a fixed size.
        Uses an array (list) to store key-value pairs.
        """
        self.size = size
        self.data = [None] * self.size

    def get_hash(self, key):
        """
        Hash function: converts a string key into an index.
        Here, we simply sum ASCII values of characters and take modulo.
        :param key: The key to hash
        :return: index (int)
        """
        hash_key = 0
        for i in key:
            hash_key += ord(i)
        return hash_key % self.size

    def __setitem__(self, key, value):
        """
        Insert/Update a key-value pair using Linear Probing.
        If the slot is full, move forward until an empty one is found.
        :param key: Key to insert
        :param value: Value to insert
        """
        index = self.get_hash(key)

        # Linear probing: move forward until empty slot is found
        while self.data[index] is not None:
            # If key already exists → update
            if self.data[index][0] == key:
                self.data[index] = [key, value]
                return
            # Move to the next index (wrap around with %)
            index = (index + 1) % self.size

        # Insert new key-value pair
        self.data[index] = [key, value]

    def __getitem__(self, key):
        """
        Retrieve a value by key using Linear Probing.
        Keeps searching forward until it finds the key or an empty slot.
        :param key: Key to search for
        :return: Value if found, -1 otherwise
        """
        index = self.get_hash(key)

        while self.data[index]:
            if self.data[index][0] == key:
                return self.data[index][1]
            index = (index + 1) % self.size

        return -1  # Key not found

    def __delitem__(self, key):
        """
        Delete a key-value pair.
        NOTE: This simplified deletion sets the slot to None directly.
        In real implementations, a "tombstone" marker is used so that probing chains are preserved.
        :param key: Key to delete
        """
        index = self.get_hash(key)
        self.data[index] = None


# ----------------------------------------------------------
# Example Usage
# ----------------------------------------------------------
if __name__ == "__main__":
    ht = HashTable()

    # Insert values
    ht["name"] = "Sabbir Mahmud"
    ht["mean"] = "Another key with same hash"

    # Retrieve values
    print(ht["name"])  # Output: Sabbir Mahmud
    print(ht["mean"])  # Output: Another key with same hash
