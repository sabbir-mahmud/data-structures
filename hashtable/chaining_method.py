r"""
==================================================
Chaining Method (চেইনিং পদ্ধতি) Notes - Bilingual DSA Reference (10/10)
==================================================

What is Chaining? (Chaining কী?)
--------------------------------------------------
- Chaining is a collision-handling technique for hash tables. (Chaining হলো Hash Table-এ Collision সামলানোর একটি পদ্ধতি।)
- Each array slot holds a BUCKET (a list) instead of a single value. (প্রতিটি ঘরে একটি মান না রেখে একটি Bucket বা List রাখা হয়।)
- When two keys collide, both simply live inside the same bucket. (দুটি Key-এর Index এক হলে দুটোই একই Bucket-এর ভিতরে থাকে।)
- It is also called SEPARATE CHAINING or Closed Addressing. (একে Separate Chaining বা Closed Addressing-ও বলা হয়।)

--------------------------------------------------
The Problem It Solves (কোন সমস্যার সমাধান করে)
--------------------------------------------------
"name" -> 20     "mean" -> 20    (same index! একই Index!)

Simple table:  data[20] = "mean value"   <- "name value" is LOST (হারিয়ে গেল)

With chaining: (Chaining দিয়ে:)
  data[20] = [ ["name", "Sabbir"], ["mean", "Another"] ]

- Both keys live peacefully in the same slot. (দুটি Key-ই একই ঘরে শান্তিতে থাকে।)
- Nothing is ever overwritten by mistake. (ভুল করে কোনো ডেটা মুছে যায় না।)

--------------------------------------------------
How Chaining Looks (Chaining দেখতে কেমন)
--------------------------------------------------

  Index      Bucket (list of [key, value] pairs)
+-------+   +--------------------------------------+
|   0   |-->| []                                   |   empty (খালি)
+-------+   +--------------------------------------+
|   1   |-->| [ ["cat", 5] ]                       |   1 item
+-------+   +--------------------------------------+
|  ...  |   |                                      |
+-------+   +--------------------------------------+
|  20   |-->| [ ["name", "Sabbir"], ["mean", "X"] ]|   collision! (সংঘর্ষ!)
+-------+   +--------------------------------------+
|  99   |-->| []                                   |
+-------+   +--------------------------------------+

- The array itself never "fills up". (Array কখনোই "ভরে" যায় না।)
- A bucket can hold any number of items. (একটি Bucket-এ যত খুশি আইটেম রাখা যায়।)

--------------------------------------------------
How Insert / Search / Delete Work (তিনটি কাজ কীভাবে হয়)
--------------------------------------------------
Insert: (বসানো)
  1. index = get_hash(key)                  (Index বের করো।)
  2. Scan the bucket; if the key exists, UPDATE it. (Bucket ঘুরে দেখো, Key থাকলে আপডেট করো।)
  3. Otherwise append [key, value].         (নাহলে শেষে যোগ করো।)

Search: (খোঁজা)
  1. index = get_hash(key)
  2. Scan only THAT bucket for a matching key. (শুধু ঐ Bucket-এর ভিতরেই খোঁজো।)

Delete: (মোছা)
  1. index = get_hash(key)
  2. Find the pair in the bucket and remove it. (Bucket থেকে জোড়াটি খুঁজে মুছে দাও।)

- We only ever scan ONE bucket, never the whole table. (আমরা শুধু একটি Bucket ঘুরি, পুরো টেবিল নয়।)
- Deletion is trivially simple here - no tombstones needed. (এখানে ডিলিট করা খুব সহজ, কোনো Tombstone লাগে না।)

--------------------------------------------------
Why Average is O(1) but Worst is O(n) (গড়ে O(1), সবচেয়ে খারাপে O(n))
--------------------------------------------------
Good hash function - keys spread evenly: (ভালো Hash Function - সমানভাবে ছড়ানো:)
+---+---+---+---+---+
| 1 | 1 | 1 | 1 | 1 |   bucket size ~ 1  ->  O(1)
+---+---+---+---+---+

Bad hash function - everything in one bucket: (খারাপ Hash Function - সব এক ঘরে:)
+---+---+---+---+---+
| 5 | 0 | 0 | 0 | 0 |   bucket size = n  ->  O(n)
+---+---+---+---+---+
  |
  v
[k1] -> [k2] -> [k3] -> [k4] -> [k5]   this is just a linked list! (এটি তো একটি Linked List!)

- In the worst case, a hash table degrades into a linear search. (সবচেয়ে খারাপ অবস্থায় Hash Table একটি Linear Search-এ পরিণত হয়।)
- Average bucket length = load factor = n / size. (গড় Bucket দৈর্ঘ্য = Load Factor = n / size।)
- Java 8+ converts very long buckets into balanced trees to get O(log n). (Java 8+ খুব লম্বা Bucket-কে Balanced Tree বানিয়ে O(log n) করে ফেলে।)

--------------------------------------------------
Why [[] for _ in range(size)] and not [[]] * size (একটি জরুরি Python ফাঁদ)
--------------------------------------------------
WRONG:  self.data = [[]] * self.size     (ভুল)

+---+---+---+
| * | * | * |    all three point to the SAME list! (তিনটিই একই List-কে দেখায়!)
+---+---+---+
  \   |   /
   \  |  /
    [ same list ]

Appending to bucket 0 also changes buckets 1 and 2. (০ নম্বরে কিছু যোগ করলে ১ আর ২ নম্বরেও যোগ হয়ে যায়।)

RIGHT:  self.data = [[] for _ in range(self.size)]   (সঠিক)

+---+---+---+
| * | * | * |    three INDEPENDENT lists (তিনটি আলাদা স্বাধীন List)
+---+---+---+
  |   |   |
 [ ] [ ] [ ]

- This is one of the most common Python bugs in hash table code. (Hash Table লেখার সময় এটি Python-এর সবচেয়ে পরিচিত ভুলগুলোর একটি।)

--------------------------------------------------
Chaining vs Linear Probing (দুই পদ্ধতির তুলনা)
--------------------------------------------------
| Feature            | Chaining              | Linear Probing        |
|--------------------|-----------------------|-----------------------|
| Storage            | List in each bucket   | Inside the array      |
| Extra memory       | Yes (list per bucket) | None per item         |
| Cache friendly     | No (scattered)        | Yes (sequential)      |
| Clustering         | No                    | Yes (primary)         |
| Load factor limit  | Can exceed 1          | Must stay < 1         |
| Deletion           | Easy (just remove)    | Hard (tombstones)     |
| Table full         | Never                 | Possible -> resize    |
| Implementation     | Easier                | Trickier              |

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
Chaining is used in:
- Java's HashMap (chaining, with tree-ification for long chains)
- C++ std::unordered_map
- Database index buckets
- Caching layers where deletion is frequent
- Any workload with an unpredictable or high load factor

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. That each slot is a bucket holding [key, value] pairs.
2. Why the average case is O(1) and the worst case is O(n).
3. Why load factor = n / size equals the average bucket length.
4. Why chaining never "fills up" but probing can.
5. Why deletion is easy here but needs tombstones in probing.
6. The [[]] * size aliasing bug in Python.
7. When to prefer chaining (frequent deletes, high load) vs probing (cache speed, tight memory).

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Using [[]] * size to create buckets.
✔ All buckets would share one list; use a list comprehension.

❌ Storing only the value inside the bucket.
✔ Store [key, value] so you can tell colliding keys apart.

❌ Appending a key that already exists.
✔ Scan the bucket first and UPDATE if the key is present.

❌ Thinking chaining makes everything O(1) forever.
✔ If buckets grow long, it degrades to O(n); resizing still matters.

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation | Average | Worst | Why?                                 |
|-----------|---------|-------|--------------------------------------|
| Insert    | O(1)    | O(n)  | Scan one short bucket; worst = all   |
| Search    | O(1)    | O(n)  | Scan one short bucket; worst = all   |
| Delete    | O(1)    | O(n)  | Find inside the bucket, then remove  |
| Rehash    | O(n)    | O(n)  | Every key is hashed again            |
| Space     | O(n)    | O(n)  | Table plus a list for every bucket   |

==================================================
"""


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
