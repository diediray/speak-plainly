"""Apply reviewed, exact-span edits to saved response drafts."""

import argparse
import json
from pathlib import Path


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def apply_edits(cases, edit_records):
    ids = [case["id"] for case in cases]
    edit_ids = [record["id"] for record in edit_records]
    if len(ids) != len(set(ids)) or len(edit_ids) != len(set(edit_ids)):
        raise ValueError("Duplicate case IDs")
    if set(ids) != set(edit_ids):
        raise ValueError("Edit IDs must match input case IDs")
    edits_by_id = {record["id"]: record["edits"] for record in edit_records}
    output = []
    for case in cases:
        answer = case["draft"]
        for edit in edits_by_id[case["id"]]:
            before, after = edit["before"], edit["after"]
            if not isinstance(before, str) or not isinstance(after, str):
                raise ValueError(f"Non-text edit in {case['id']}")
            if not before or answer.count(before) != 1:
                raise ValueError(f"Edit does not match one unique span in {case['id']}")
            answer = answer.replace(before, after, 1)
        if not answer.strip():
            raise ValueError(f"Empty answer for {case['id']}")
        output.append({"id": case["id"], "answer": answer.strip()})
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", required=True)
    parser.add_argument("--edits", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = apply_edits(read_json(args.cases), read_json(args.edits))
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Applied edits to {len(result)} answers.")
