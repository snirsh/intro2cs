def create_list():
    ls = []
    while True:
        counter = 0
        ls.append(input())
        if ls[counter-1] is None:
            return ls
            break
        else:
            counter += 1
            True


print(create_list())
