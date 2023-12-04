def main():
    a=1
    b=2    
    add = __import__('add_0')
    print("1 + 2 = {}".format(add.add(a,b)))


if __name__ == '__main__':
    main()