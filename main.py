def main():
    character_count = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        split_string = file_contents.split()

    for i in range(0, len(split_string)):
        new_str_arr = list(split_string[i].lower())
        for i in range(0, len(new_str_arr)):
            letter = new_str_arr[i]
            if letter in character_count:
                character_count[letter] = character_count[letter] + 1
            else:
                character_count[letter] = 1

    character_count = sorted(character_count.items(), key=lambda x: x[1], reverse=True)
    character_count = dict(character_count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(split_string)} words found in the document\n\n")
    for character, count in character_count.items():
        if character.isalpha():
            print(f"The '{character}' character was found {count} times")
    print("--- End report ---")


main()
