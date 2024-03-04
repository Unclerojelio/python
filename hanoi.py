def hanoi(size, start, finish, spare):
    if size == 1:
        print(start, " -> ", finish)
    else:
        hanoi(size-1, start, spare, finish)
        print(start, " -> ", finish)
        hanoi(size-1, spare, finish, start)
    
hanoi(4, 1, 2, 3)