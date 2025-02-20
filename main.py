def sort_on(dict):
    return dict["count"]
def main():
    char_count = {}
    with open('books/frankenstein.txt') as f:
        file_contents = f.read().lower()
    words = file_contents.split()
    word_count = len(words)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for letter in file_contents:
        if letter.isalpha():
            if letter in char_count:
                char_count[letter] +=1
            else:
                char_count[letter] = 1
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})
    # Sort in descending order (most frequent first)
        char_list.sort(reverse=True, key=sort_on)

# Print each character count
        for char_dict in char_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

print("--- End report ---")
main()