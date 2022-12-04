# 1.1
import os


def get_cwd():
    cwd = os.getcwd()
    print(cwd)


def main():
    # 1.2
    get_cwd()
    # 1.3
    os.chdir("D:/data")
    get_cwd()
    # 1.4
    os.makedirs("D:/data/nltt")
    # 1.5
    items = os.listdir("C:/Users/Admin/Documents")
    print(items)
    # 1.6
    existence = os.path.exists("D:/data/text.txt")
    print("Is exist:", existence)
    # 1.7
    os.remove("D:/data/text.txt")
    os.rmdir("D:/data/junk")


if __name__ == "__main__":
    main()
