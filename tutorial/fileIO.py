with open("kaziNazrul.txt", mode="r") as k_file:
    words_all = []
    for line in k_file.readlines():
        stripped_string = line.strip()
        words = stripped_string.split(" ")
        words_all += words

    unique_words = set(words_all)
    print(len(words_all))
    print(words_all)
    print(len(unique_words))

    with open("unique_words.txt", mode="w") as write_file:
        for item in sorted(unique_words):
            write_file.write(item)
            write_file.write("\n")


print("Finished")