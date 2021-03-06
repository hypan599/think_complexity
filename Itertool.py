"""this file defines an itertool 
that can generate infinite letter-num 
sequences like a1,b1,c1...zi,a2,b2..."""


class AllTrue:

    def __next__(self):
        return True

    def __iter__(self):
        return self


def alphabet_num_cycle(n):
    i = 0
    total = 1
    while True:
        if total >= n:
            break
        i += 1
        for letter in "abcdefghijklmnopqrstuvwxyz".lower():
            total += 1
            yield letter + str(i)


def main():
    k = 0
    print(list(zip("abc", AllTrue())))
    for letter in alphabet_num_cycle():
        print(letter)
        # these lines used to test programme
        k += 1
        if k > 10:
            break


if __name__ == '__main__':
    main()
