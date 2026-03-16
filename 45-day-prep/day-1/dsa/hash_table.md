# Hash Table — Interview Notes

---

**What is a Hash Table?**
> Data structure storing key-value pairs. Hash function converts key to index. O(1) average for insert, search, delete.

---

**What is a Collision?**
> Two different keys hash to the same index.

---

**Collision Resolution**
> - **Chaining** — list at each bucket. Used in Java HashMap.
> - **Open Addressing** — probe for next empty slot. Used in Python dict.
> - **Linear** → `(h+i) % size` | **Quadratic** → `(h+i²) % size` | **Double Hashing** → `(h1 + i*h2) % size`

---

**Load Factor**
> `α = keys / buckets` → crosses 0.67 → rehash (double size + re-insert all)

---

**Chaining Logic**
> Same key → **update**. Different key, same index → **chain**. We check by comparing the actual key with `==`, not the index.

---

**Why immutable keys in Python?**
> Mutable key changes → hash changes → value can never be found again.

---

**Why O(n) worst case?**
> All keys collide into one bucket → linear search through entire chain.

---

**Chaining vs Open Addressing?**
> Chaining → simpler, works at high load factor. Open Addressing → better cache performance, load factor must stay below 1.

---

**Python dict internally**
> Hash table. Default size 8. Doubles on resize. Open addressing with pseudo-random probing.