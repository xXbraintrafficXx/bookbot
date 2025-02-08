#read frankensten
def main() :
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")

    book_text = get_book_text(book_path)
    #print(book_text)
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document\n")
    character_count = count_characters(book_text)
    print(character_count)
    print("--- End report ---")
    
def get_book_text(path) :
    with open(path) as f:
        return f.read()

def count_words(text) :
    words = text.split()
    return len(words)

def count_characters(text) :
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    chars_appear = {}
    for i in text:
        if i.lower() not in chars_appear:
            chars_appear[i.lower()] = 1
        else:
            chars_appear[i.lower()] += 1 

    char_list = []
    #sort and filter dictionary
    for char, count in chars_appear.items():
        if char in chars: #add only alpha chars
            char_list.append({'letter': char, 'num': count})
    def sort_on(dict):
        return dict["num"]
   
    char_list.sort(reverse=True, key=sort_on)
    char_report = []
    for char_dict in char_list:
        charval = char_dict["letter"]
        numval = char_dict["num"]
        char_report.append(f"The '{charval}' character was found {numval} times")


    return "\n".join(char_report)


    


main()