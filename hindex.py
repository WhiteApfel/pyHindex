def h_index(publications):
    publications = sorted(publications)
    N = len(publications)
    if N > 1:
        maxrange = min([N, max(publications)]) + 1
        for h in range(1, maxrange)[::-1]:
            if publications[-h:][0] >= h >= publications[:N - h][-1]:
                return h
        return 1
    else:
        return 1


if __name__ == "__main__":
    print("Enter the number of citations for each publication, separated by spaces.\n\n")
    while True:
        print(f'H-index: \033[93m{h_index(list(map(int, input(">>> ").split())))}\033[0m\n')
