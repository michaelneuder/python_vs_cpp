#ifndef WINDOW_H
#define WINDOW_H

#include <QWidget>

namespace Ui {
class window;
}

class window : public QWidget
{
    Q_OBJECT

public:
    explicit window(QWidget *parent = 0);
    ~window();

private:
    Ui::window *ui;
};

#endif // WINDOW_H
