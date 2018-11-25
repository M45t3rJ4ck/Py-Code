def string_num_appear(string):
    my_dict = {}
    for word in string:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict = 1
    return my_dict


string_num_appear()


def most_common(occur):
    values = occur.values()
    best = max(values)
    words = []
    for k in occur:
        if occur[k] == best:
            words.append(k)
    return words, best


def often_happen(occur, min_times):
    result = []
    done = False
    while not done:
        temp = most_common(occur)
        if temp[1] >= min_times:
            result.append(temp)
            for w in temp[0]:
                del(occur[0])
            else:
                done = True
    return result


print(often_happen())
