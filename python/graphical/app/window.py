#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from prime_factors import prime_factors
import time

class window(QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(800, 535)
        self.row_counter = 0

        # menu bar
        self.menu_bar = QMenuBar(self)
        self.file_menu = QMenu('file')
        self.menu_bar.addMenu(self.file_menu)

        # quit
        self.quit_action = QAction(QIcon('exit.png'), 'exit', self)
        self.quit_action.setShortcut('Ctrl+w')
        self.file_menu.addAction(self.quit_action)
        self.menu_bar.show()

        # layouts
        self.main_layout = QVBoxLayout(self)
        self.footer_layout = QHBoxLayout()
        self.input_layout = QHBoxLayout()
        self.results_layout = QHBoxLayout()

        # widgets
        self.title_label = QLabel("prime decomposition calculator")
        self.title_font = QFont("Helvetica",40)
        self.title_label.setFont(self.title_font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.exit_button = QPushButton("exit")
        self.upload_button = QPushButton("upload integer list")
        self.input_line_edit = QLineEdit()
        self.input_label = QLabel("enter the number ")
        self.input_line_edit.setAlignment(Qt.AlignCenter)
        self.input_button = QPushButton("decompose!")
        self.results_table = QTableWidget()
        self.results_table.setFixedSize(600, 300)
        self.results_table.setColumnCount(2)
        self.results_table.setRowCount(1000000)
        self.results_table.setHorizontalHeaderLabels(["input", "factorization"])
        self.header = self.results_table.horizontalHeader()
        self.header.setStretchLastSection(True)
        self.results_table.setColumnWidth(0, 150)
        self.result_time_label = QLabel("time to run: ")
        self.result_time_label.setAlignment(Qt.AlignCenter)

        # adding widgets to layouts
        self.footer_layout.addStretch(0);
        self.footer_layout.addWidget(self.upload_button);
        self.footer_layout.addWidget(self.exit_button);
        self.footer_layout.addStretch(0);
        self.input_layout.addStretch(0);
        self.input_layout.addWidget(self.input_label);
        self.input_layout.addWidget(self.input_line_edit);
        self.input_layout.addWidget(self.input_button);
        self.input_layout.addStretch(0);
        self.results_layout.addStretch(0);
        self.results_layout.addWidget(self.results_table);
        self.results_layout.addStretch(0);

        # adding layouts to main layout
        self.main_layout.addWidget(self.title_label);
        self.main_layout.addSpacing(15);
        self.main_layout.addLayout(self.input_layout);
        self.main_layout.addLayout(self.results_layout);
        self.main_layout.addSpacing(10);
        self.main_layout.addWidget(self.result_time_label);
        self.main_layout.addStretch(0);
        self.main_layout.addLayout(self.footer_layout);

        # actions
        self.quit_action.triggered.connect(self.exit_app)
        self.exit_button.clicked.connect(self.exit_app)
        self.input_button.clicked.connect(self.decompose)
        self.upload_button.clicked.connect(self.upload)

    def exit_app(self):
        self.close()

    def decompose(self):
        user_input = self.input_line_edit.text()
        self.results_table.setItem(self.row_counter, 0, QTableWidgetItem(user_input))
        prime_handler = prime_factors()
        prime_handler.decompose(int(user_input))
        factor_string = ''
        for i in range(len(prime_handler.factors)):
            factor_string += str(prime_handler.factors[i])
            factor_string += ", "
        factor_string = factor_string[:len(factor_string)-2]
        self.results_table.setItem(self.row_counter, 1, QTableWidgetItem(factor_string))
        self.row_counter+=1

    def decompose_argument(self, n):
        self.results_table.setItem(self.row_counter, 0, QTableWidgetItem(str(n)))
        prime_handler = prime_factors()
        prime_handler.decompose(n)
        factor_string = ''
        for i in range(len(prime_handler.factors)):
            factor_string += str(prime_handler.factors[i])
            factor_string += ", "
        factor_string = factor_string[:len(factor_string)-2]
        self.results_table.setItem(self.row_counter, 1, QTableWidgetItem(factor_string))
        self.row_counter+=1

    def upload(self):
        file_name = QFileDialog.getOpenFileName()
        start_time = time.clock()
        line_counter = 0
        with open(file_name[0], 'r') as READ_FILE:
            for line in READ_FILE:
                line_counter += 1
                self.decompose_argument(int(line))
        READ_FILE.close()
        end_time = time.clock()
        self.result_time_label.setText("run time: " + str((end_time-start_time) *1000))
        with open("results_python.txt", "a") as APPEND_FILE:
            APPEND_FILE.write(str(line_counter) + "," + str((end_time-start_time) *1000) + "\n")

    def upload_argument(self, file_name):
        start_time = time.clock()
        with open(file_name, 'r') as READ_FILE:
            for line in READ_FILE:
                self.decompose_argument(int(line))
        READ_FILE.close()
        end_time = time.clock()
        self.result_time_label.setText("run time: " + str((end_time-start_time) *1000))
        return(end_time-start_time)
