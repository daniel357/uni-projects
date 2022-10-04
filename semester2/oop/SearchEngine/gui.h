//
// Created by User on 5/26/2022.
//

#ifndef SEARCH_ENGINE_GUI_H
#define SEARCH_ENGINE_GUI_H

#include <QWidget>
#include "Service.h"
#include "Repository.h"


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
    Service service;
    void populate_list(vector<Domain> arr);
    void connect_signals_slots();
    void filter_by_text();
    void show_best_matching();
};


#endif //SEARCH_ENGINE_GUI_H
