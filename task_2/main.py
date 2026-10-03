def main():

    text = tuple(input().lower().split())
    counting_dict = dict()

    for word in text:
        if word in counting_dict:
            counting_dict[word] += 1
        else:
            counting_dict[word] = 1

    sorted_dict = sorted(counting_dict.items(),
                         key=lambda wrd: wrd[1], reverse=True)

    for x in range(5):
        print(f'{x+1} : {sorted_dict[x]}')


if __name__ == "__main__":
    main()
