# required python and PyQt5 modules
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))    # add prefered search engine url here
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # create navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # back button
        back_btn = QAction('<--', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # forward button
        forward_btn = QAction('-->', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.nav_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.url_update)

        # reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

    def nav_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def url_update(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("Browser")
window = MainWindow()
app.exec()
