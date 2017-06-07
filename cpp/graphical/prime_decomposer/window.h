#ifndef WINDOW_H
#define WINDOW_H

#include <QWidget>
#include <QPushButton>
#include <QMenuBar>
#include <QMenu>
#include <QAction>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QFont>
#include <QLineEdit>
#include <QTableWidget>

class window : public QWidget{Q_OBJECT
    public:
        explicit window(QWidget *parent = 0);
    private:
        int row_counter;
        QPushButton *exit_button;
        QMenuBar *menu_bar;
        QMenu *file_menu;
        QAction *quit_action;
        QVBoxLayout *main_layout;
        QHBoxLayout *footer_layout;
        QLabel *title_label;
        QFont title_font;
        QLineEdit *input_line_edit;
        QHBoxLayout *input_layout;
        QLabel *input_label;
        QPushButton *input_button;
        QTableWidget *results_table;
        QHBoxLayout *results_layout;
        QPushButton *upload_button;
        QLabel *result_time_label;
    private slots:
        void exit_clicked();
        void decompose();
        int upload();
        void decompose_argument(long n);
};

#endif // WINDOW_H
