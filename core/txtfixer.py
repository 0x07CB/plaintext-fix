#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

from plaintext_fix.plaintext_fix import plaintext_fix


def parse_args():
    parser = argparse.ArgumentParser(
        description="Fix plaintext files by removing unwanted characters."
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input file to be fixed.",
    )
    parser.add_argument(
        "output_file",
        type=str,
        help="Path to the output file where the fixed content will be saved.",
    )
    return parser.parse_args()

def main():
    args = parse_args()

    TextFixer = plaintext_fix()

    # Read the input file
    with open(args.input_file, "r", encoding="utf-8") as f:
        content_lines = f.readlines()
    print(f"Read {len(content_lines)} lines from {args.input_file}")


    print("Fixing content in progress...")
    # Fix the content
    fixed_content_lines = []
    for line in content_lines:
        fixed_line = ""
        for line_chunk in TextFixer.fix(f"{line}"):
            fixed_line = fixed_line + line_chunk
        fixed_content_lines.append(fixed_line)
    fixed_content = "\n".join(fixed_content_lines)
    print("Content fixing completed.")

    # Write the fixed content to the output file
    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(fixed_content)
    print(f"Fixed content written to {args.output_file}")


if __name__ == "__main__":
    main()
