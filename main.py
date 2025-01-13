def main():
    word_count = count_words("frankenstein.txt")
    char_count = count_chars("frankenstein.txt")
    list_of_char_dicts = []

    for key, val in char_count.items():
        letter_obj = {}
        letter_obj["letter"] = key
        letter_obj["occurences"] = val
        list_of_char_dicts.append(letter_obj)

    list_of_char_dicts.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n\n")

    for char in list_of_char_dicts:
        print(f"The '{char["letter"]}' character was found {char["occurences"]} times ")


def count_chars(text):
    char_dict = {}
    with open(f"books/{text}") as f:
        file_contents = f.read()
        for char in file_contents:
            if char.isalpha():
                lowered_char = char.lower()
                if lowered_char in char_dict:
                    char_dict[lowered_char] += 1
                else:
                    char_dict[lowered_char] = 1

    return char_dict


def count_words(text):
    word_count = 0
    with open(f"books/{text}") as f:
        file_contents = f.read()
        lines = file_contents.split()
        for line in lines:
            # print(line)
            words = line.split()
            word_count += len(words)
    return word_count


def sort_on(dict):
    return dict["occurences"]


if __name__ == "__main__":
    main()
