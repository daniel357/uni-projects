//
// Created by User on 5/25/2022.
//

#ifndef MEDICALDISORDERS_GUI_H
#define MEDICALDISORDERS_GUI_H

#include <QWidget>
#include "Service.h"


QT_BEGIN_NAMESPACE
namespace Ui { class gui; }
QT_END_NAMESPACE

class gui : public QWidget {
Q_OBJECT

public:
    explicit gui(QWidget *parent = nullptr);

    ~gui() override;

private:
    Ui::gui *ui;
    Service serv;

    void populate_list(vector<Task> sorted_tasks);
    void connect_slots_and_shit();
    void search_symptoms();
    void show_symptoms_disorder();
    void populate_list_string(vector<string> sorted_tasks);
};


#endif //MEDICALDISORDERS_GUI_H
