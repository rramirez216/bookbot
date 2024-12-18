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

    print(character_count)


main()
