import os
print("\033[1;32m Banana is sorting your files,no need to wait...")
print()
print()
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

if __name__ == "__main__":
    files = os.listdir()

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Videos')
    createIfNotExist('Others')
    createIfNotExist('Audio')


    imgExts = [".png", ".jpg",".svg", ".jpeg",".GIF", ".TIFF", ".BMP"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

    docExts = [".txt", ".docx", "doc", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    vidExts = [".mp4", ".mkv", ".flv","webm", ".MPG", ".MP2", ".MPEG", ".MPE", ".MPV"]
    videos = [file for file in files if os.path.splitext(file)[1].lower() in vidExts]

    audExts = [".wav", ".mp3", ".aac", ".wma"]
    audios = [file for file in files if os.path.splitext(file)[1].lower() in audExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in vidExts) and (ext not in audExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)

    move("Images", images)
    move("Docs", docs)
    move("Videos", videos)
    move("Others", others)
    move("Audio", audios)
    print("\033[1;36m Everything sorted Sir \n Thanks for using this tool - Kushal")
    print("\033[1;33m https://www.github.com/k1ushal")
