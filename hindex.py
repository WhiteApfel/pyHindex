def h_index(publications):
    publications = sorted(publications)
    N = len(publications)
    for h in range(0, N):
        if publications[-h:][0] >= h and publications[:N-h][-1] <= h:
            return h
    return 1

if __name__ == "__main__":
    print(h_index(list(map(int, input().split())))) #"Enter the number of citations for each publication, separated by spaces.\n\n>>> "
