import sys,re,random,requests,mimetypes
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup

from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton

from ui_yarc import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.getBut.clicked.connect(self.start_url)
        # self.getBut.clicked.connect()
        # self.getBut.clicked.connect()

    def start_url(self):

        self.howDeep = 1
        self.howManyTimes = self.howManyPages.value()

        self.url = ("reddit.com/r/" + self.subField.text())
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        }

        self.r = requests.get('http://' + self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.r.content, 'html.parser')
        self.howDeep += 0
        self.get_doc()

    def get_doc(self):

        #Regular expression for links in page source
        self.links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                self.soup.prettify())
        self.mimeType = []
        self.mimeTypeSort = []

        #chceck image type and append tuple to list
        for link in self.links:
            self.mimeType.append(mimetypes.guess_type(link))

        # extracting information from tuple to list

        for i in self.mimeType:
            self.mimeTypeSort.append(i[0])

        self.linkMimeDict = dict(zip(self.links, self.mimeTypeSort))

        #Get rid of garbage aka None

        self.linkMimeDict = {k: v for k, v in self.linkMimeDict.items() if v}


        #choose image format

        print (self.linkMimeDict)
        for item in self.linkMimeDict.itervalues():
            if item == "image/jpeg":
                self.saveFile('JPEG')
            elif item == "image/png":
                self.saveFile('PNG')
            elif item == "image/gif":
                self.saveFile('GIF')
            else:pass

    def saveFile(self,fileType):
        for link in self.linkMimeDict:
            try:
                self.file_numb = random.randint(0000000000,2494849328)
                self.r = requests.get(link)
                self.i = Image.open(BytesIO(self.r.content),'r')
                self.fileName = 'img/' + str(self.file_numb) + '.jpg'
                self.i.save(self.fileName,fileType)
            except:
                print('error')
                pass


        #go to next page if needed

        if self.howManyTimes > 1:
            while self.howDeep <= self.howManyTimes:

                self.url = self.soup.find('a',{'rel' : 'nofollow next'},href=True)

                # sometimes self.soup.find can't find next button so for now it is bruteforcing it :)
                try:
                    self.r = requests.get(self.url['href'])
                except:
                    while self.url == None:
                        self.url = self.soup.find('a', {'rel': 'nofollow next'}, href=True)

                self.soup = BeautifulSoup(self.r.content, 'html.parser')
                self.howDeep += 1
                self.get_doc()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()