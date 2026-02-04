# Counds words
def get_words(book_text):
    spl = book_text.split()
    return len(spl)

# Counts each character and returns a dict
def get_characters(book_text):
    result = {}
    for char in book_text:
        lowered = char.lower()
        if lowered not in result:
            result[lowered] = 1
        else:
            result[lowered] += 1
    return result

# Helper function to grab num from the dictionary
def sort_on(dictionary):
    return dictionary["num"]

# Sorts the dictionary into a list of dict pairs in descending order
def sort_characters(characters_dict):
    new_list = []
    for k in characters_dict:
        if k.isalpha():
            new_list.append({"char": k, "num": characters_dict[k]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

# Prints character count in the sorted list in descending order
def print_characters(sorted_list):
    for pair in sorted_list:
        print(f"{pair["char"]}: {pair["num"]}")
    

