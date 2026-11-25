import os

ENTRY = "One star. He bought me for 'low maintenance', then watered me with leftover coffee and blamed me for dying loudly."
assert 1 <= len(ENTRY) <= 279, len(ENTRY)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
