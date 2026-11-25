import os

ENTRY = "One star. My owner waters me on a schedule set by an app that also reminds him to drink water, and somehow I am the only one of us still thirsty."
assert 1 <= len(ENTRY) <= 279, len(ENTRY)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
