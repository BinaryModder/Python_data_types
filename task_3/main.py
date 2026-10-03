def main():

    list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    list2 = [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]

    all_words = dict()

    for el in list1:
        if el.get('name') not in all_words:
            all_words[el.get('name')] = False

    for el in list2:
        if el.get('name') not in all_words:
            all_words[el.get('name')] = False

    for element_1 in list1:
        for element_2 in list2:
            if element_1.get('name') == element_2.get('name'):
                all_words[element_1.get('name')] = True

    appearing = [key for key, value in all_words.items() if value == True]
    not_appearing = [key for key, value in all_words.items() if value == False]

    print(f'Appearing in both dicts : {appearing}')
    print(f'Not appearing in both dicts {not_appearing}')


if __name__ == "__main__":
    main()
