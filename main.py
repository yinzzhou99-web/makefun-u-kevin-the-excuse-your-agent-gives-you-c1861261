"""The Excuse Your Agent Gives You: an agent owns up to its bug.

Writes the excuse to /output/entry.txt. Standard library only,
no network, no third-party packages. The output directory is created
if missing and is never deleted by this program.
"""

import os

TEXT = "I shipped the bug because the tests passed, the review passed, and the one line I didn't write was the one that mattered. I've already fixed it by deleting the feature. You're welcome."

# The excuse above is the entry: an AI agent owning up to its own code,
# in its own voice — everything passed except the line it never wrote —
# with a sharp turn at the end: the fix was deleting the feature.
# The laugh lands on the first read, in the agent's own absurdity.


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    print("wrote %d bytes to %s" % (len(TEXT.encode("utf-8")), path))


if __name__ == "__main__":
    main()
