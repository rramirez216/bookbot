def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        split_string = file_contents.split()
        print(len(split_string))

    print(split_string[2])


main()
