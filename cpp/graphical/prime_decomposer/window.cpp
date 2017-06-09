#include "window.h"
#include <QPushButton>
#include <QMenuBar>
#include <QMenu>
#include <QAction>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QFont>
#include <QLineEdit>
#include <iostream>
#include <prime_factors.h>
#include <QTableWidget>
#include <QString>
#include <QHeaderView>
#include <QTableWidgetItem>
#include <QFileDialog>
#include <fstream>
#include <ctime>
#include <QFile>
#include <QDebug>
#include <QTextStream>
using namespace std;

window::window(QWidget *parent) : QWidget(parent){
    setFixedSize(800,535);
    row_counter = 0;

    // menu bar and menu declaration
    menu_bar = new QMenuBar(this);
    file_menu = new QMenu("file");
    menu_bar->addMenu(file_menu);

    // menu actions
    quit_action = new QAction("quit",this);
    quit_action->setShortcut(Qt::Key_W | Qt::CTRL);
    file_menu->addAction(quit_action);
    menu_bar->show();

    // layouts
    main_layout = new QVBoxLayout(this);
    footer_layout = new QHBoxLayout();
    input_layout = new QHBoxLayout();
    results_layout = new QHBoxLayout();

    // widgets
    title_label = new QLabel("prime decomposition calculator");
    title_font = QFont("Helvetica",40);
    title_label->setFont(title_font);
    title_label->setAlignment(Qt::AlignCenter);
    exit_button = new QPushButton("exit");
    upload_button = new QPushButton("upload integer list");
    input_line_edit = new QLineEdit();
    input_label = new QLabel("enter the number ");
    input_line_edit->setAlignment(Qt::AlignCenter);
    input_button = new QPushButton("decompose!");
    results_table = new QTableWidget();
    results_table->setFixedSize(600, 300);
    results_table->setColumnCount(2);
    results_table->setRowCount(1000000);
    results_table->setHorizontalHeaderLabels(QString("input; factorization").split(";"));
    QHeaderView* header = results_table->horizontalHeader();
    header->setStretchLastSection(true);
    results_table->setColumnWidth(0, 150);
    result_time_label = new QLabel("time to run: ");
    result_time_label->setAlignment(Qt::AlignCenter);

    // adding widgets to layouts
    footer_layout->addStretch(0);
    footer_layout->addWidget(upload_button);
    footer_layout->addWidget(exit_button);
    footer_layout->addStretch(0);
    input_layout->addStretch(0);
    input_layout->addWidget(input_label);
    input_layout->addWidget(input_line_edit);
    input_layout->addWidget(input_button);
    input_layout->addStretch(0);
    results_layout->addStretch(0);
    results_layout->addWidget(results_table);
    results_layout->addStretch(0);

    // adding layouts to main layout
    main_layout->addWidget(title_label);
    main_layout->addSpacing(15);
    main_layout->addLayout(input_layout);
    main_layout->addLayout(results_layout);
    main_layout->addSpacing(10);
    main_layout->addWidget(result_time_label);
    main_layout->addStretch(0);
    main_layout->addLayout(footer_layout);

    // connections
    connect(exit_button, SIGNAL (clicked()), this, SLOT (exit_clicked()));
    connect(quit_action, SIGNAL (triggered()), this, SLOT (exit_clicked()));
    connect(input_button, SIGNAL (clicked()), this, SLOT (decompose()));
    connect(upload_button, SIGNAL (clicked()), this, SLOT (upload()));
}

void window::exit_clicked(){
    this->close();
}

void window::decompose(){
    string input = input_line_edit->text().toUtf8().constData();
    long int_input = std::stol(input);
    results_table->setItem(row_counter, 0, new QTableWidgetItem(input_line_edit->text()));
    prime_factors prime_handler;
    prime_handler.decompose(int_input);
    vector<int> factors = prime_handler.get_factors();
    QString factor_string;
    for(vector<int>::const_iterator i=factors.begin(); i!= factors.end(); ++i){
        QString temp = QString::number(*i);
        factor_string += temp;
        factor_string += ", ";
    }
    factor_string.chop(2);
    results_table->setItem(row_counter, 1, new QTableWidgetItem(factor_string));
    row_counter++;
    input_line_edit->clear();
}

void window::decompose_argument(long n){
    QString input_qstring = QString::fromStdString(to_string(n));
    results_table->setItem(row_counter, 0, new QTableWidgetItem(input_qstring));
    prime_factors prime_handler;
    prime_handler.decompose(n);
    vector<int> factors = prime_handler.get_factors();
    QString factor_string;
    for(vector<int>::const_iterator i=factors.begin(); i!= factors.end(); ++i){
        QString temp = QString::number(*i);
        factor_string += temp;
        factor_string += ", ";
    }
    factor_string.chop(2);
    results_table->setItem(row_counter, 1, new QTableWidgetItem(factor_string));
    row_counter++;
}

int window::upload(){
    QString file_name = QFileDialog::getOpenFileName();
    clock_t start = clock();
    string file_name_ = file_name.toUtf8().constData();
    string line;
    int num_lines = 0;
    ifstream input_file (file_name_);
    if(input_file.is_open()){
        while(getline(input_file, line)){
            num_lines++;
            long n = stol(line);
            decompose_argument(n);
        }
        input_file.close();
    }
    else cout << "file could not be opened." << endl;
    clock_t end = clock();
    double time = double (end-start)/ CLOCKS_PER_SEC*1000;
    result_time_label->setText(QString::fromStdString("run time: "+ to_string(time)));
    QString output_file_name = "results_c++.txt";
    QFile output_file(output_file_name);
    output_file.open(QIODevice::Append);
    if(!output_file.isOpen()){
        cout << "- Error, unable to open\n";
        return 1;
    }
    QTextStream out_stream(&output_file);
    out_stream << QString::fromStdString(to_string(num_lines) + ", " + to_string(time) + "\n");
    output_file.close();
    return 0;
}
