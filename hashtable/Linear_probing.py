r"""
==================================================
Linear Probing (লিনিয়ার প্রোবিং) Notes - Bilingual DSA Reference (10/10)
==================================================

What is Linear Probing? (Linear Probing কী?)
--------------------------------------------------
- Linear Probing is a collision-handling technique for hash tables. (Linear Probing হলো Hash Table-এ Collision সামলানোর একটি পদ্ধতি।)
- It belongs to the OPEN ADDRESSING family. (এটি Open Addressing পরিবারের অন্তর্ভুক্ত।)
- When a slot is already taken, it simply checks the NEXT slot, and keeps going until an empty one is found. (কোনো ঘর দখল হয়ে থাকলে এটি পরের ঘর দেখে, এভাবে খালি ঘর না পাওয়া পর্যন্ত এগোতে থাকে।)
- Everything is stored INSIDE the array itself - no extra lists. (সব ডেটা Array-এর ভিতরেই থাকে, বাইরে আলাদা কোনো List লাগে না।)

The formula: (সূত্র:)
    index = (index + 1) % size

- The % makes the search wrap around to the start of the table. (% ব্যবহারের ফলে খোঁজা টেবিলের শুরুতে ফিরে আসতে পারে।)

--------------------------------------------------
The Problem It Solves (কোন সমস্যার সমাধান করে)
--------------------------------------------------
Without collision handling, the second key overwrites the first. (Collision না সামলালে দ্বিতীয় Key প্রথমটিকে মুছে দেয়।)

"name" -> 20     "mean" -> 20    (same index! একই Index!)

Simple table:  data[20] = "mean value"   <- "name value" is LOST (হারিয়ে গেল)

Linear probing: (Linear Probing দিয়ে:)
  data[20] = ["name", "Sabbir"]
  data[21] = ["mean", "Another"]         <- moved to the next free slot

- No data is lost. (কোনো ডেটা হারায় না।)

--------------------------------------------------
How Insertion Works (Insert কীভাবে কাজ করে)
--------------------------------------------------
Insert "mean" when index 20 is already occupied by "name".

index 20: [name | Sabbir]   <-- occupied, and key != "mean" (দখল করা)
             |
             v  probe +1 (পরের ঘরে যাও)
index 21: [ empty ]         <-- free! store here (খালি! এখানেই বসাও)

+------+---------------+
|  20  | name | Sabbir |
+------+---------------+
|  21  | mean | Another|   <- placed by probing
+------+---------------+
|  22  |    empty      |
+------+---------------+

- We store BOTH the key and the value, not just the value. (আমরা Key এবং Value দুটোই রাখি, শুধু Value নয়।)
- Without storing the key, we could never tell whose value it is. (Key না রাখলে বোঝাই যেত না মানটি কার।)
- If the key already exists, we UPDATE it instead of inserting again. (Key আগে থেকে থাকলে নতুন করে না বসিয়ে আপডেট করা হয়।)

--------------------------------------------------
How Search Works (Search কীভাবে কাজ করে)
--------------------------------------------------
Search "mean":

Step 1: index = hash("mean") = 20
Step 2: data[20] key is "name" != "mean" -> probe forward (পরের ঘরে যাও)
Step 3: data[21] key is "mean" -> FOUND (পাওয়া গেছে)

Stop conditions: (থামার নিয়ম:)
- Key matched -> return the value. (Key মিলে গেলে মান ফেরত দাও।)
- Empty slot found -> the key does not exist. (খালি ঘর পেলে বুঝতে হবে Key নেই।)

* An empty slot means "stop searching", because probing never skips slots. (খালি ঘর মানেই "খোঁজা বন্ধ", কারণ Probing কখনো ঘর লাফিয়ে যায় না।)

--------------------------------------------------
Primary Clustering - The Big Weakness (মূল দুর্বলতা)
--------------------------------------------------
Occupied slots tend to stick together and form long blocks. (দখল করা ঘরগুলো একসাথে জমে লম্বা ব্লক তৈরি করে।)

+---+---+---+---+---+---+---+---+
| X | X | X | X | X |   |   | X |
+---+---+---+---+---+---+---+---+
  \___________________/
      cluster (গুচ্ছ)

- Any key that hashes anywhere into the cluster must walk the WHOLE cluster. (এই গুচ্ছের যেকোনো জায়গায় পড়া Key-কে পুরো গুচ্ছ হেঁটে পার হতে হয়।)
- Clusters grow bigger over time, making everything slower. (সময়ের সাথে গুচ্ছ বড় হয় এবং সবকিছু ধীর হয়ে যায়।)
- This is called PRIMARY CLUSTERING. (একে বলা হয় Primary Clustering।)
- Fixes: quadratic probing (+1, +4, +9...) or double hashing. (সমাধান: Quadratic Probing অথবা Double Hashing।)

--------------------------------------------------
The Deletion Trap - Tombstones (ডিলিটের ফাঁদ)
--------------------------------------------------
Suppose "name"(20) and "mean"(21) exist, and we delete "name" by setting data[20] = None.

+------+----------+
|  20  |   None   |  <- deleted (মুছে ফেলা হলো)
+------+----------+
|  21  |   mean   |  <- still here (এখনো আছে)
+------+----------+

Now search "mean": hash gives 20 -> data[20] is empty -> "not found"! (এখন "mean" খুঁজলে ২০ নম্বর ঘর খালি দেখে বলবে "নেই"!)

- The probing chain is BROKEN. (Probing-এর চেইন ভেঙে গেছে।)
- Real implementations put a TOMBSTONE (a "deleted" marker) instead of None. (আসল বাস্তবায়নে None-এর বদলে একটি Tombstone বা "মুছে ফেলা হয়েছে" চিহ্ন বসানো হয়।)
- Search treats a tombstone as "keep going"; insert treats it as "reusable". (Search Tombstone দেখলে এগিয়ে যায়; Insert একে পুনরায় ব্যবহারযোগ্য ধরে।)
- The __delitem__ in this file uses the SIMPLIFIED version and has exactly this bug. (এই ফাইলের __delitem__ সরল ভার্সন, তাই এই সমস্যাটি এখানে আছে।)

--------------------------------------------------
Linear Probing vs Chaining (দুই পদ্ধতির তুলনা)
--------------------------------------------------
| Feature            | Linear Probing      | Chaining            |
|--------------------|---------------------|---------------------|
| Storage            | Inside the array    | List in each bucket |
| Extra memory       | None per item       | Pointer/list per item |
| Cache friendly     | Yes (sequential)    | No (scattered)      |
| Clustering         | Yes (primary)       | No                  |
| Load factor limit  | Must stay < 1       | Can exceed 1        |
| Deletion           | Hard (tombstones)   | Easy (remove item)  |
| Table full         | Possible -> resize  | Never full          |

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
Open addressing / linear probing is used in:
- Python's own dict (a probing variant, not chaining)
- CPU caches and low-level lookup tables
- Compiler symbol tables
- Memory-constrained systems (no extra allocations)
- High-performance in-memory databases

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. The probe formula: index = (index + 1) % size.
2. Why you MUST store the key alongside the value.
3. Why an empty slot ends a search.
4. What primary clustering is and why it degrades performance.
5. Why deletion needs tombstones (the broken-chain problem).
6. Why the load factor must stay below 1, and ideally under ~0.7.
7. Alternatives: quadratic probing and double hashing.

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Storing only the value in a slot.
✔ Store [key, value]; otherwise you cannot verify whose value it is.

❌ Forgetting the % size wrap-around.
✔ Without it, probing runs off the end of the array.

❌ Deleting by setting the slot to None.
✔ That breaks the probe chain; use a tombstone marker.

❌ Letting the table fill up completely.
✔ At load factor 1 the insert loop never terminates; resize before that.

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation | Average | Worst | Why?                                |
|-----------|---------|-------|-------------------------------------|
| Insert    | O(1)    | O(n)  | Usually 1 probe; worst = full walk  |
| Search    | O(1)    | O(n)  | Usually 1 probe; worst = full walk  |
| Delete    | O(1)    | O(n)  | Must probe to find the key first    |
| Rehash    | O(n)    | O(n)  | Every key is hashed again           |
| Space     | O(n)    | O(n)  | Single array, no extra structures   |

==================================================
"""


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
