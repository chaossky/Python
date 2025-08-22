from itertools import batched
nums = [1, 2, 3, 4, 5, 6, 7]
chunks = list(batched(nums, 3))
print(chunks)  # [(1, 2, 3), (4, 5, 6), (7,)]

# 🔎 WHAT IT DOES
# ✅ Splits data into fixed-size chunks
# ✅ Handles leftovers gracefully in the last batch
# ✅ Works with any iterable
# 🛠 USAGE
# — Processing data in batches
# — Splitting records for APIs or DB inserts
# — Chunking items for parallel tasks
# 💡 WHY IT MATTERS
# ⟶ Cleaner than writing custom slicing loops
# ⟶ Memory-efficient and Pythonic
# ⟶ Perfect for big data, ETL, and automation scripts
# 📚 TRIVIA
# batched() was introduced in Python 3.12, making chunking a built-in feature—previously developers used loops or more-itertools.