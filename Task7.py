# import this

def preprocess_text(string):
    string_lowercase = string.lower()
    text = string_lowercase.replace("it\'s", "it is").replace("you\'re", "you are").replace(
        "aren\'t", "are not").replace(
        "let\'s", "let us").replace(",", "").replace(".", "").replace("*", "").replace(
        "-", "").replace("!", "")
    return text

# d)Now create a “vocabulary_list” for the whole text consisting alphabetically ordered words without duplicates
# e.g. Converting “I have a dog, dog have me” into: vocabulary = [“a”, “dog”, “have”, “I”, “me”]


def create_vocabulary_list(text):
    vocabulary_list = []
    for word in text.split():
        if word not in vocabulary_list:
            vocabulary_list.append(word)
    vocabulary_list.sort()
    return vocabulary_list


# e)      Next > create a count of each word in the whole text (you can use imported Counter or just an additional list with numbers):
# e.g. vocabulary_count = {“a”:1, “dog”:2, “have”:2, “i”:1, “me”:1} (or just a list vocab_list = [1,2,2,1,1])


def word_counter(text):
    word_counter_dict = {}
    words = text.split()
    words.sort()
    for word in words:
        if word in word_counter_dict:
            word_counter_dict[word] += 1
        else:
            word_counter_dict[word] = 1
    return word_counter_dict


def main():
    zen_of_python = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren\'t special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one - -obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than * right * now. If the implementation is hard to explain, it\'s a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"

    text = preprocess_text(zen_of_python)
    print(text)
    vocabulary_list = create_vocabulary_list(text)
    print(vocabulary_list)
    word_counts = word_counter(text)
    print(word_counts)


if __name__ == '__main__':
    main()
