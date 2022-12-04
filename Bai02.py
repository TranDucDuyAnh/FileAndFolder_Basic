def main():
    # 2.1
    f = open("D:/data/test.txt", "r")
    # 2.2
    f = open("D:/data/test.txt", "w")
    # 2.3
    f = open("D:/data/test.txt", "w+b")
    # 2.4
    f = open("D:/data/test.txt", mode='r', encoding='utf-8')
    # 2.5
    f.close()
    # 2.6
    try:
        f = open("D:/data/test.txt", encoding='utf-8')
    finally:
        f.close()
    # 2.7 - 2.8
    with open("D:/data/test.txt", mode='w', encoding='utf-8') as f:
        f.write("hello\n")
        f.write("this is\n")
        f.write("a text\n")
    # 2.9
    f = open("D:/data/test.txt", "r")
    f.seek(0)
    print(f.read())
    f.close()
    # 2.10
    im = open("D:/data/apple.jpg", "r+b")
    im.seek(0)
    print(im.read())
    im.close()


if __name__ == "__main__":
    main()
