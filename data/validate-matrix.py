#!/usr/bin/env python3
"""PreToolUse guard: validate adaptation-matrix.json structure before edits.

Called by hook with $CLAUDE_TOOL_FILE_PATH as argument.
Exit 0 = allow edit, Exit 1 = block edit with error message.
"""
import sys, os, json

MATRIX_NAME = "adaptation-matrix.json"
EXPECTED_PHASES = ["qualifier", "comprendre", "strategiser", "specifier",
                   "designer", "architecturer", "planifier", "valider"]
EXPECTED_SIZES = ["S", "M", "L", "XL"]


def main():
    if len(sys.argv) < 2:
        sys.exit(0)  # No file path, skip

    file_path = os.path.normpath(sys.argv[1])
    if not file_path.endswith(MATRIX_NAME):
        sys.exit(0)  # Not the matrix file, skip

    if not os.path.isfile(file_path):
        sys.exit(0)  # File doesn't exist yet, skip

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            matrix = json.load(f)
    except json.JSONDecodeError as e:
        print("[validate-matrix] BLOCKED: Invalid JSON — %s" % e)
        sys.exit(1)

    errors = []

    # Check phases key exists
    if "phases" not in matrix:
        errors.append("Missing 'phases' key")
    else:
        # Check all 8 phases present
        for p in EXPECTED_PHASES:
            if p not in matrix["phases"]:
                errors.append("Missing phase: %s" % p)
            else:
                phase = matrix["phases"][p]
                if "items" not in phase:
                    errors.append("Phase '%s' missing 'items'" % p)
                else:
                    # Check S/M/L/XL sizes exist
                    for s in EXPECTED_SIZES:
                        if s not in phase["items"]:
                            errors.append("Phase '%s' missing size '%s'" % (p, s))

                    # Check monotonic: len(S) <= len(M) <= len(L) <= len(XL)
                    counts = []
                    for s in EXPECTED_SIZES:
                        if s in phase["items"]:
                            counts.append(len(phase["items"][s]))
                    if counts != sorted(counts):
                        errors.append("Phase '%s' not monotonic: %s" % (p, dict(zip(EXPECTED_SIZES, counts))))

    # Check phase_order
    if "phase_order" not in matrix:
        errors.append("Missing 'phase_order' key")
    elif matrix["phase_order"] != EXPECTED_PHASES:
        errors.append("phase_order mismatch: expected %s" % EXPECTED_PHASES)

    if errors:
        print("[validate-matrix] BLOCKED: %d issue(s):" % len(errors))
        for e in errors:
            print("  - %s" % e)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
