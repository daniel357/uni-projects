#include <QApplication>
#include <QPushButton>
#include "gui.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    gui ui;
    ui.show();
    return QApplication::exec();
}
