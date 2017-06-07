#!/usr/bin/env python3
from PyQt5.QtWidgets import QApplication
from window import window

class app(object):
    def __init__(self):
        self.app = QApplication([])
        self.main_window = window()
        self.main_window.show()
        self.app.exec_()

def main():
    my_app = app()

if __name__ == '__main__':
    main()
