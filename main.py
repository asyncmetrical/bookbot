def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        all_lower = file_contents.lower()
        # book_words = file_contents.split()


        letter_count = {}
        for x in range(ord("a"), ord("z") + 1):
            letter_count[chr(x)] = 0
        # print(letter_count)

        for letter in all_lower:
            if letter not in letter_count:
                pass
            else:
                letter_count[letter] += 1
        # print(letter_count)
    
        def report(ordered_count):
            for i in ordered_count:
                print(f"The '{i}' character was found {ordered_count[i]} times")
        report(letter_count)
main()
