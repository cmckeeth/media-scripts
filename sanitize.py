import glob, os, sys


def finder(_dir):
    for file in os.listdir(_dir):
        print(file)

def removeTails(_dir):
    for file in os.listdir(_dir):
        newName = file.replace(".", " ")
        file = newName


if __name__ == '__main__':
    finder(sys.argv[1])
    removeTails(sys.argv[1])





    # title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    # os.rename(pathAndFilename,
    #           os.path.join(dir, titlePattern % title + ext))