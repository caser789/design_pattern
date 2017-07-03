class Base(object):

    def __init__(self, name):
        self.name = name
        self.components = list()

    def add(self, component):
        self.components.append(component)

    def remove(self, component):
        self.components.remove(component)

    def kill_virus(self):
        raise NotImplementedError


class Folder(Base):

    def kill_virus(self):
        print 'kill virus in folder {self.name}'.format(self=self)
        for component in self.components:
            component.kill_virus()


class ImageFile(Base):

    def kill_virus(self):
        print 'kill virus to image {self.name}'.format(self=self)


class TextFile(Base):

    def kill_virus(self):
        print 'kill virus to text {self.name}'.format(self=self)


class VideoFile(Base):

    def kill_virus(self):
        print 'kill virus to video {self.name}'.format(self=self)


def main():
    downloads = Folder("Downloads")
    pics = Folder("pics")
    texts = Folder("texts")
    videos = Folder("videos")

    file1 = ImageFile("longnv.jpg")
    file2 = ImageFile("wuji.gif")
    file3 = TextFile("9yin.txt")
    file4 = TextFile("kuihua.doc")
    file5 = VideoFile("jianghu.rmvb")

    pics.add(file1)
    pics.add(file2)
    texts.add(file3)
    texts.add(file4)
    videos.add(file5)
    downloads.add(pics)
    downloads.add(texts)
    downloads.add(videos)

    downloads.kill_virus()

if __name__ == "__main__":
    main()
