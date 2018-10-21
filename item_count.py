def my_len(sentence):
    count = 0
    for letter in sentence:
       count = count + 1


def num_times(word, letter):
    count = 0
    for w in word:
        if w == letter:
            count = count + 1




    return count


def count_numbers(number, target) :
    number = str(number)   # 75 --> '75'
    target = str(target)
    count = 0


    for n in number :
        if n == target :
            count = count + 1


    print(count)


# # # #  # #  # # # #  # # # # # #  # 3
count_numbers (1234567890321765098, 8)




