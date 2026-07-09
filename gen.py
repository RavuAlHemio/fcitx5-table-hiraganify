#!/usr/bin/env python3
import argparse
import sys
import unicodedata


HIRAGANA_FIRST = 0x3041
HIRAGANA_LAST = 0x3096
SMALL_PREFIX = "."


def add_code(
    all_code_chars: set[str],
    code_to_char: dict[str, str],
    code_prefix: str,
    char_name_lower: str,
    char: str,
) -> None:
    code = code_prefix + char_name_lower
    all_code_chars.update(code)
    code_to_char[code] = char


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="output_file", nargs="?")
    args = parser.parse_args()
    if args.output_file is None:
        output_file = sys.stdout
    else:
        output_file = open(args.output_file, "w", encoding="utf-8")

    with output_file:
        all_code_chars: set[str] = set()
        code_to_char: dict[str, str] = {}

        for n in range(HIRAGANA_FIRST, HIRAGANA_LAST+1):
            char = chr(n)
            char_name = unicodedata.name(char).removeprefix("HIRAGANA LETTER ")

            code_prefix = ""
            if char_name.startswith("SMALL "):
                char_name = char_name.removeprefix("SMALL ")
                code_prefix = "."

            char_name = char_name.lower()

            add_code(all_code_chars, code_to_char, code_prefix, char_name, char)

            # some sensible aliases
            if char_name == "si":
                add_code(all_code_chars, code_to_char, code_prefix, "shi", char)
            if char_name == "ti":
                add_code(all_code_chars, code_to_char, code_prefix, "chi", char)
            if char_name == "tu":
                add_code(all_code_chars, code_to_char, code_prefix, "tsu", char)
            if char_name == "hu":
                add_code(all_code_chars, code_to_char, code_prefix, "fu", char)
            if len(char_name) == 2 and char_name.startswith("r"):
                # ra/re/ri/ro/ru -> la/le/li/lo/lu
                add_code(all_code_chars, code_to_char, code_prefix, "l" + char_name[1], char)

        key_code = "".join(sorted(all_code_chars))
        max_length = max(len(code) for code in code_to_char.keys())

        print(f"KeyCode={key_code}", file=output_file)
        print(f"Length={max_length}", file=output_file)
        print("[Data]", file=output_file)
        for (code, char) in code_to_char.items():
            print(f"{code} {char}", file=output_file)


if __name__ == "__main__":
    main()
