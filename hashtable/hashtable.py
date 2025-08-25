# ----------------------------------------------------------
# HashTable Implementation in Python (Simple Version)
# ----------------------------------------------------------
# What is a Hash Table?
# ---------------------
# A Hash Table is a data structure that stores key-value pairs.
# It uses a "hash function" to convert the key into an array index,
# making data access very fast (near O(1) time).
#
# Why use Hash Tables?
# --------------------
# - Extremely fast lookups, insertions, and deletions (on average O(1)).
# - Widely used in real-world applications like:
#     * Databases (indexes)
#     * Caching (fast key-value access)
#     * Language dictionaries/maps
#     * Symbol tables in compilers
#
# Pros of Hash Tables:
# --------------------
# Very fast average-case operations (Insert/Search/Delete ~ O(1))
# Flexible key types (strings, numbers, etc.)
# Direct access without scanning entire data (unlike lists/arrays)
#
# Cons of Hash Tables:
# --------------------
# Collisions may occur when two keys hash to the same index
# Worst-case time complexity can degrade to O(n) if collisions are not handled
# Needs good hash functions & resizing strategies
#
# Big-O Time Complexity (without handling collisions):
# ----------------------------------------------------
# Insert   → O(1) average
# Search   → O(1) average
# Delete   → O(1) average
# Worst Case (with collisions, no handling) → O(n)
# ----------------------------------------------------------


class HashTable:
    def __init__(self, size=100):
        """
        Initialize a HashTable with a fixed size.
        :param size: Number of slots in the underlying array.
        """
        self.size = size
        self.data = [None] * self.size  # storage array

    def get_hash(self, key):
        """
        Hash function: converts a string key into an index.
        Here, we simply sum up ASCII values of characters and take modulo.
        :param key: The key to hash (string)
        :return: index (int)
        """
        hash_key = 0
        for i in key:
            hash_key += ord(i)  # ord() gives ASCII value of char
        return hash_key % self.size

    def __setitem__(self, key, value):
        """
        Insert/Update key-value pair in the hash table.
        Does not handle collisions in this version.
        :param key: The key to store
        :param value: The value to store
        """
        index = self.get_hash(key)
        self.data[index] = value

    def __getitem__(self, key):
        """
        Retrieve a value by key.
        :param key: The key to search for
        :return: The value if exists, else None
        """
        index = self.get_hash(key)
        return self.data[index]

    def __delitem__(self, key):
        """
        Delete a key-value pair.
        :param key: The key to delete
        """
        index = self.get_hash(key)
        self.data[index] = None


# ----------------------------------------------------------
# Example Usage
# ----------------------------------------------------------
if __name__ == "__main__":
    ht = HashTable()

    # Inserting key-value pairs
    ht["name"] = "Sabbir Mahmud"
    ht["mean"] = "Another key with same hash"  # This overwrites if collision occurs

    # Retrieving values
    print(ht["name"])  # Might print "Another key..." if collision occurs
