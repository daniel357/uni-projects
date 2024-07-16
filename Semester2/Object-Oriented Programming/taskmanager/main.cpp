#include <QApplication>
#include <QPushButton>
#include "Repository.h"
#include "Service.h"
#include "gui.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    Service service;
    vector<gui*> windows;
    for(auto &item: service.get_programmers())
    {
        windows.push_back(new gui(service, item));
    }
    return QApplication::exec();
}
