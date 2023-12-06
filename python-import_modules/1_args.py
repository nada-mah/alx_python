from sys import argv
def main():
    i=1
    if len(argv) == 1:
        print("0 arguments.")
    else:
        if (len(argv)-1) == 1:
            print(f"{len(argv)-1} argument:")
        else:
            print(f"{len(argv)-1} arguments:")
        while len(argv) > i:
            print("{}: {}".format(i,argv[i]))
            i+=1
            
if __name__ == '__main__':
    main()