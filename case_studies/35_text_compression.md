# Case 35: Text Compression Using Character Runs

**Data note:** Sample values are illustrative; they are not real-time or official records.

## Problem statement
Encode a string by grouping consecutive repeated characters and compare original and encoded lengths, including cases where encoding is not beneficial.

## Objectives
Run-length encode consecutive groups and retain the original if encoded text is not shorter.

## Assumptions
- Inputs are non-empty strings without newline characters.
- Encoding writes every character followed by its run count, including count 1.
- If encoded text is not shorter, the original is chosen.

## Algorithm
1. Start a run at the first character.
2. Scan subsequent characters, extending or closing the run.
3. Append the final run.
4. Compare lengths and print the selected representation.

## Flowchart

```text
Start → Read text → Set current run → More characters? → Same? increase : append prior run and start next → Append final run → Encoded shorter? choose → End
```

## Pseudocode

```text
FOR each text
    encoded = empty; current = first; count = 1
    FOR each later character
        IF equal current: count += 1
        ELSE: append current and count; reset run
    append final run
    choose shorter of encoded and original
    PRINT lengths and choice
```

## Python source code

```python
texts = ["aaabbc", "abcd", "zzzz"]

for text in texts:
    encoded = ""
    current_character = text[0]
    run_count = 1
    for position in range(1, len(text)):
        if text[position] == current_character:
            run_count = run_count + 1
        else:
            encoded = encoded + current_character + str(run_count)
            current_character = text[position]
            run_count = 1
    encoded = encoded + current_character + str(run_count)
    if len(encoded) < len(text):
        chosen = encoded
    else:
        chosen = text
    print("Original:", text, "length:", len(text))
    print("Encoded:", encoded, "length:", len(encoded))
    print("Chosen:", chosen)
    print()
```

## Test cases and observed output

The following is stdout from executing the program with its embedded sample data. The PNG capture is in `../output_screenshots/35_text_compression.png`.

```text
Original: aaabbc length: 6
Encoded: a3b2c1 length: 6
Chosen: aaabbc

Original: abcd length: 4
Encoded: a1b1c1d1 length: 8
Chosen: abcd

Original: zzzz length: 4
Encoded: z4 length: 2
Chosen: z4
```

## Conclusion
Run-length encoding can expand ordinary text. The program keeps the original whenever encoding does not shorten it.
