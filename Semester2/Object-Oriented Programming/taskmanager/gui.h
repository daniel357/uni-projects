//
// Created by User on 7/4/2022.
//

#ifndef TASKMANAGER_GUI_H
#define TASKMANAGER_GUI_H

#include <QPushButton>
#include <QLineEdit>
#include <QTableView>
#include <QVBoxLayout>
#include <QGridLayout>
#include <QMessageBox>
#include <QLabel>
#include "QWidget"
#include "Observer.h"
#include "Service.h"
#include "TableModel.h"

class gui: public Observer, public QWidget{
private:
    Service& service;
    Programmer& programmer;

    QPushButton * button_add_task, *button_start, *button_done, *button_remove_task;
    QLineEdit *line_description;

    TableModel *tableModel;
    QTableView *tableView;

    QGridLayout * gridLayout_buttons;
    QVBoxLayout * window_layout;
public:
    void connect_signals_slots();

    gui(Service &s, Programmer &p);

    ~gui() override;

    void initialize_gui();

    void add_task();

    void remove_task();

    void set_progress();

    void set_closed();

    int get_selected_index();

    void notify();

    void update() override;

    void check_unset_button();
};


#endif //TASKMANAGER_GUI_H
