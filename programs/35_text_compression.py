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
