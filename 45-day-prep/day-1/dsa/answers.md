# Day 1 - DSA Final Notes
## Arrays & Hash Tables — Big-O, Time & Space Complexity

---

## 📌 What is Big-O?
Big-O describes **how an algorithm's time/space grows** as input size (n) increases.

| Notation | Name | Meaning |
|----------|------|---------|
| **O(1)** | Constant | Same speed regardless of n |
| **O(log n)** | Logarithmic | Grows slowly (e.g. binary search) |
| **O(n)** | Linear | Grows proportionally with n |

---

## 🗂️ Arrays — Time Complexity

| Operation | Complexity | Why |
|-----------|-----------|-----|
| Access by index | **O(1)** | Direct memory: `base + index × size` |
| Search (unsorted) | **O(n)** | Must scan every element |
| Search (sorted) | **O(log n)** | Binary search possible |
| Insert at end | **O(1)** amortized | Just append |
| Insert at middle/start | **O(n)** | Must shift all elements after |
| Delete at end | **O(1)** | Remove last |
| Delete at middle/start | **O(n)** | Must shift elements to fill gap |

> **Key insight:** Arrays are O(1) access because memory is contiguous —
> address = `base + (index × element_size)`. One formula, no searching.

---

## 🗃️ Hash Tables — Time Complexity

| Operation | Average | Worst | Why |
|-----------|---------|-------|-----|
| Lookup | **O(1)** | O(n) | Collision → linear scan |
| Insert | **O(1)** | O(n) | Collision handling |
| Delete | **O(1)** | O(n) | Collision handling |
| Search | **O(1)** | O(n) | Same as lookup |

> **Why O(1) average?** Key → hash function → index → jump directly to bucket. No iteration.
>
> **Why O(n) worst case?** All keys collide into the same bucket → becomes a linked list → full linear scan.
> This is rare with a good hash function but can be triggered by adversarial inputs.

---

## 📦 Space Complexity Trade-offs

| Structure | Space | Note |
|-----------|-------|------|
| Array (fixed) | **O(n)** | Allocates exactly n elements |
| Array (dynamic) | **O(n)** | May over-allocate (e.g. 2× resize buffer) |
| Hash Table | **O(n)** | Stores n key-value pairs + extra bucket overhead |

| Situation | Choose | Reason |
|-----------|--------|--------|
| Fast lookup, memory available | **Hash Table** | O(1) lookup at cost of extra space |
| Memory tight, order matters | **Array** | Leaner, but O(n) search |
| Caching / memoization | **Hash Table** | O(1) repeated lookups |

> **Core Rule:** More space → faster time. Hash tables spend memory to buy speed.

---

## ⚖️ Arrays vs Hash Tables — When to Use?

| Need | Use |
|------|-----|
| Fast access by position | **Array** |
| Fast lookup by key | **Hash Table** |
| Ordered / sorted data | **Array** |
| Frequency counting / caching | **Hash Table** |
| Memory efficiency | **Array** (less overhead) |

---

## 🧠 Memory Aids

```
Array:      index → value   (positional, ordered, contiguous memory)
Hash Table: key   → value   (associative, unordered, hash-indexed)

Hash Map Lookup = O(1) average, O(n) worst case (due to collisions)
Both offer O(1) access — but for very different reasons.
```

---

## 🔑 5 Golden Rules to Remember

1. **Array access is O(1)** — contiguous memory, one formula finds any element.
2. **Hash lookup is O(1) average** — hash function jumps directly to the bucket.
3. **Hash worst case is O(n)** — all keys collide, rare with good hash functions.
4. **Array insert/delete is O(n)** — shifting elements is expensive, except at the end.
5. **More space = faster time** — hash tables trade memory overhead for speed.