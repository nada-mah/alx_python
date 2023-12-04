def main():    
    add = __import__('add_0')
    print("1 + 2 = {}".format(add.add(1,2)))


if __name__ == '__main__':
    main()