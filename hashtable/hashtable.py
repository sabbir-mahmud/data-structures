"""
==================================================
Hash Table (হ্যাশ টেবিল) Notes - Bilingual DSA Reference (10/10)
==================================================

What is a Hash Table? (Hash Table কী?)
--------------------------------------------------
- A Hash Table stores data as key-value pairs. (Hash Table ডেটাকে Key-Value জোড়া হিসেবে সংরক্ষণ করে।)
- It uses a HASH FUNCTION to convert a key into an array index. (এটি একটি Hash Function ব্যবহার করে Key-কে Array-এর Index-এ রূপান্তর করে।)
- Because it jumps straight to an index, access is nearly O(1). (সরাসরি Index-এ চলে যায় বলে ডেটা পেতে প্রায় O(1) সময় লাগে।)
- Python's dict is a highly optimized hash table. (Python-এর dict হলো একটি অত্যন্ত উন্নত Hash Table।)

--------------------------------------------------
The Core Idea (মূল ধারণা)
--------------------------------------------------
Key -> Hash Function -> Index -> Store value at that index

    "name"  --> get_hash("name") --> 17 --> data[17] = "Sabbir"

- No searching is needed; the key TELLS us where to look. (খুঁজতে হয় না; Key নিজেই বলে দেয় কোথায় যেতে হবে।)
- This is the whole magic of hashing. (Hashing-এর পুরো জাদুটাই এটি।)

--------------------------------------------------
How the Hash Function Works (Hash Function কীভাবে কাজ করে)
--------------------------------------------------
Here we sum the ASCII values of every character, then take modulo size. (এখানে প্রতিটি অক্ষরের ASCII মান যোগ করে, তারপর Size দিয়ে ভাগশেষ নেওয়া হয়।)

Key = "cat", size = 100

  'c' -> 99
  'a' -> 97
  't' -> 116
  ------------
  sum  = 312

  index = 312 % 100 = 12

+----+----+ ... +-----+ ... +----+
| 0  | 1  |     | 12  |     | 99 |
+----+----+ ... +-----+ ... +----+
                  ^
                value stored here

- The modulo (%) keeps the index inside the array bounds. (মডুলাস (%) Index-কে Array-এর সীমার ভিতরে রাখে।)

--------------------------------------------------
Properties of a Good Hash Function (ভালো Hash Function-এর গুণ)
--------------------------------------------------
1. Deterministic - the same key must always give the same index. (একই Key সবসময় একই Index দেবে।)
2. Uniform - it should spread keys evenly across the table. (Key গুলো টেবিল জুড়ে সমানভাবে ছড়াবে।)
3. Fast - it must be cheap to compute. (দ্রুত হিসাব করা যাবে।)

Bad distribution (clustering):     Good distribution:
+---+---+---+---+---+              +---+---+---+---+---+
| 4 | 0 | 0 | 0 | 1 |              | 1 | 1 | 1 | 1 | 1 |
+---+---+---+---+---+              +---+---+---+---+---+

- Our ASCII-sum function is simple but WEAK. (আমাদের ASCII যোগ করা Function সহজ, কিন্তু দুর্বল।)
- "name", "mean" and "amen" all sum to the same value! (এই তিনটি শব্দের যোগফল একই!)

--------------------------------------------------
The Collision Problem (Collision বা সংঘর্ষের সমস্যা)
--------------------------------------------------
A collision happens when two different keys produce the SAME index. (দুটি ভিন্ন Key একই Index তৈরি করলে তাকে Collision বলে।)

"name" --> index 20
"mean" --> index 20   <-- same index! (একই Index!)

Without handling: (Collision সামলানো না হলে:)

+------+
| 20   | "Sabbir Mahmud"        <- first value (প্রথম মান)
+------+
   |
   v  overwritten! (মুছে গেল!)
+------+
| 20   | "Another key..."       <- second value replaces it
+------+

- Data is silently LOST. (ডেটা নীরবে হারিয়ে যায়।)
- This simple version does NOT handle collisions - see chaining_method.py and Linear_probing.py. (এই সহজ ভার্সনটি Collision সামলায় না - chaining_method.py এবং Linear_probing.py দেখো।)

--------------------------------------------------
Load Factor (লোড ফ্যাক্টর)
--------------------------------------------------
Load Factor = Number of items / Table size

    items = 75, size = 100  ->  load factor = 0.75

- The higher the load factor, the more collisions happen. (Load Factor যত বেশি, Collision তত বেশি।)
- Real hash tables RESIZE (usually double) when the load factor crosses ~0.7. (আসল Hash Table, Load Factor ০.৭ পার হলে সাইজ দ্বিগুণ করে।)
- Resizing requires REHASHING every key into the new table -> O(n). (Resize করলে সব Key নতুন করে Hash করতে হয় - O(n)।)

--------------------------------------------------
Hash Table vs Array vs Linked List (পার্থক্য)
--------------------------------------------------
| Feature           | Array      | Linked List | Hash Table   |
|-------------------|------------|-------------|--------------|
| Access by index   | O(1)       | O(n)        | N/A          |
| Access by key     | O(n)       | O(n)        | O(1) average |
| Insert            | O(n)       | O(1)        | O(1) average |
| Delete            | O(n)       | O(1)        | O(1) average |
| Search by value   | O(n)       | O(n)        | O(n)         |
| Ordered           | Yes        | Yes         | No*          |
| Extra memory      | Low        | Medium      | High (empty slots) |

* Python 3.7+ dicts preserve insertion order, but that is a Python detail, not a hash table property. (Python 3.7+ এ dict ঢোকানোর ক্রম মনে রাখে, কিন্তু এটি Hash Table-এর নিজস্ব বৈশিষ্ট্য নয়।)

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
Hash Tables are used in:
- Python dict and set (internally)
- Database indexing
- Caching systems (Redis, Memcached)
- Symbol tables in compilers
- Password storage (with cryptographic hashes)
- Counting frequency of items
- Removing duplicates in O(n)
- Two-sum style interview problems

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. Why lookup is O(1) average (The key computes its own index).
2. Why the worst case is O(n) (All keys collide into one slot).
3. What a collision is and the two ways to fix it (Chaining, Open Addressing).
4. What a load factor is and why resizing/rehashing is needed.
5. Why keys must be immutable and hashable (A mutable key would change its hash).
6. That hash tables have NO ordering guarantee by design.

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Thinking hash table operations are ALWAYS O(1).
✔ It is O(1) on AVERAGE; the worst case is O(n).

❌ Thinking a good hash function prevents all collisions.
✔ Collisions are unavoidable (pigeonhole principle); we only reduce and manage them.

❌ Ignoring collisions in an implementation.
✔ Without handling, data gets silently overwritten (this file demonstrates that bug).

❌ Using a mutable object (like a list) as a key.
✔ Keys must be immutable so their hash never changes.

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation | Average | Worst | Why?                              |
|-----------|---------|-------|-----------------------------------|
| Insert    | O(1)    | O(n)  | Direct index; worst = all collide |
| Search    | O(1)    | O(n)  | Direct index; worst = all collide |
| Delete    | O(1)    | O(n)  | Direct index; worst = all collide |
| Rehash    | O(n)    | O(n)  | Every key is hashed again         |
| Space     | O(n)    | O(n)  | Table plus unused empty slots     |

==================================================
"""


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
