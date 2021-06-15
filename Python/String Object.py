def main():
    print('Hello, World.'.capitalize())
    print('Hello, World.'.lower())
    print('Hello, World.'.title())
    print('Hello, World.'.count(' '))
    print('Hello, World.'.swapcase())
    s='This is a string'
    print(s.split())
    s2=s.split('i')
    print(s2)
    s3='?'.join(s2)
    print(s3)

if __name__=="__main__":
    main()    