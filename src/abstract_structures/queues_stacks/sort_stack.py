def sortStack(s):
    bufs = []
    while s:
        item = s.pop()
        count, i = 0, 0
        while bufs and bufs[-1] > item:
            s.append(bufs.pop())
            count += 1
        bufs.append(item)  
        while i < count:
            bufs.append(s.pop())
            i += 1
    return bufs

def main():
    s = [3, 5, 1, 2, 6, 7, 8]
    print(sortStack(s))

    
if __name__ == '__main__':
    main()
