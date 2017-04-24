import sys, re, random, requests, mimetypes, os, pickle
from datetime import datetime
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup

from PyQt5 import QtWidgets,QtCore

import ui_yarc



class Worker(QtCore.QThread):
    """"""

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.howDeep = 1
        self.mimeType = []
        self.mimeTypeSort = []
        self.imgExt = []
        self.filesNum = 0
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        }
        try:
            self.comboHistory = pickle.load(open('hist.p','rb'))
        except:
            self.comboHistory = []
            pickle.dump(self.comboHistory,open('hist.p','wb'))



    def run(self):
        self.howManyTimes = MainWindow.howManyPages.value()
        self.combo_history_dump(MainWindow.comboBox.currentText(),self.comboHistory,'hist.p')
        self.url = ("reddit.com/r/" + MainWindow.comboBox.currentText())
        self.r = requests.get('http://' + self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.r.content, 'lxml')
        if self.soup.find('img', {'class':'interstitial-image'}):
            self.r = requests.post('https://www.reddit.com/over18?dest=https://www.' + self.url ,data={'over18':'yes'},headers=self.headers)
            self.soup = BeautifulSoup(self.r.content, 'lxml')
            self.get_links()
        else:
            self.get_links()


    def combo_history_dump(self,entry,list,file):
        '''
        :param entry: STRING 
        :param list: LIST
        :param file: FILENAME.p
        :return:  PICKLE FILE
        '''
        while len(list) < 5:
            if entry in list:
                pass
            else:
                self.comboHistory.append(entry)
                pickle.dump(list, open(file, 'wb'))


    def get_links(self):

        # Regular expression for links in page source
        self.links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                self.soup.prettify())
        # check image type and append tuple to list
        for link in self.links:
            self.mimeType.append(mimetypes.guess_type(link))
        # extracting information from tuple to list
        for i in self.mimeType:
            if i[0] == 'image/jpeg':
                self.mimeTypeSort.append('JPEG')
            elif i[0] == 'image/png':
                self.mimeTypeSort.append('PNG')
            elif i[0] == 'image/gif':
                self.mimeTypeSort.append('GIF')
            else:
                self.mimeTypeSort.append(i[0])
        # merge lists into dict
        self.linkMimeDict = dict(zip(self.links, self.mimeTypeSort))
        # Get rid of garbage aka None
        self.linkMimeDict = {k: v for k, v in self.linkMimeDict.items() if v}
        self.saveFile()

    def saveFile(self):

        self.today = str(datetime.now())
        if not os.path.exists('img/' + self.today[:10] + '/' + MainWindow.comboBox.currentText()):
            os.makedirs('img/' + self.today[:10] + '/' + MainWindow.comboBox.currentText())

        for link,ext in self.linkMimeDict.items():
            try:
                self.file_numb = random.randint(0000000000, 2494849328)
                self.r = requests.get(link)
                self.image = Image.open(BytesIO(self.r.content), 'r')
                self.fileName = 'img/' + self.today[:10] + '/' + MainWindow.comboBox.currentText()+ '/' + str(
                    self.file_numb) + '.' + ext
                self.image.save(self.fileName)
            except:
                print('Unsupported type.')
                pass

        # go to next page if needed
        if self.howManyTimes > 1:
            while self.howDeep <= self.howManyTimes:
                self.url = self.soup.find('a', {'rel': 'nofollow next'}, href=True)
                self.r = requests.get(self.url['href'], headers=self.headers)
                self.howDeep += 1
                self.soup = BeautifulSoup(self.r.content, 'lxml')
                self.get_links()

class MainWindow(QtWidgets.QMainWindow, ui_yarc.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.myThread = Worker()
        self.cb = QtWidgets.QComboBox
        self.label_wrk.hide()
        self.getBut.clicked.connect(self.myThread.start)
        self.getBut.clicked.connect(self.cb)
        self.stopBut.clicked.connect(self.myThread.terminate)
        self.stopBut.clicked.connect(self.label_wrk.hide)
        self.myThread.started.connect(self.label_wrk.show)
        self.myThread.finished.connect(self.label_wrk.hide)
        self.comboBox.addItems(self.myThread.comboHistory)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    app.exec_()
