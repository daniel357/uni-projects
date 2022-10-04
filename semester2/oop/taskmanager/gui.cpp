//
// Created by User on 7/4/2022.
//

#include "gui.h"


gui::gui(Service &s, Programmer &p):service(s), programmer(p) {
    this->service.addObserver(this);
    this->initialize_gui();
    this->connect_signals_slots();
    this->show();
}

gui::~gui() {
    this->service.removeObserver(this);
}

void gui::initialize_gui() {
    this->setWindowTitle(QString::fromStdString(this->programmer.get_name()));
    this->resize(1000, 700);
    this->tableModel = new TableModel(this->service, this->programmer);
    this->tableView = new QTableView{};
    this->tableView->setModel(this->tableModel);

    this->window_layout =new QVBoxLayout();
    this->window_layout->addWidget(this->tableView);

    this->line_description = new QLineEdit{};
    QLabel* description_label = new QLabel{};
    description_label->setText("description");

    this->button_add_task = new QPushButton("add task");
    this->button_remove_task = new QPushButton("remove task");
    this->button_done = new QPushButton("DONE");
    this->button_start = new QPushButton("START");

    this->gridLayout_buttons = new QGridLayout();
    this->gridLayout_buttons->addWidget(description_label, 0, 0);
    this->gridLayout_buttons->addWidget(this->line_description, 0, 1);
    this->gridLayout_buttons->addWidget(this->button_add_task, 1, 0);
    this->gridLayout_buttons->addWidget(this->button_remove_task, 2, 0);
    this->gridLayout_buttons->addWidget(this->button_start, 3, 0);
    this->gridLayout_buttons->addWidget(this->button_done, 4, 0);

    this->window_layout->addLayout(this->gridLayout_buttons);
    this->tableView->resizeColumnsToContents();

    this->setLayout(this->window_layout);

}

int gui::get_selected_index() {
    QModelIndexList  selected_indexes = this->tableView->selectionModel()->selectedIndexes();
    if(selected_indexes.empty())
        return -1;
    int index_selected = selected_indexes.at(0).row();
    return index_selected;
}

void gui::notify() {
    this->tableModel->refresh_data();
}

void gui::update() {
    this->notify();
}

void gui::connect_signals_slots() {
    QObject::connect(this->button_add_task, &QPushButton::clicked, this, &gui::add_task);
    QObject::connect(this->button_remove_task, &QPushButton::clicked, this, &gui::remove_task);
    QObject::connect(this->button_start, &QPushButton::clicked, this, &gui::set_progress);
    QObject::connect(this->button_done, &QPushButton::clicked, this, &gui::set_closed);
    QObject::connect(this->tableView, &QTableView::clicked, this, &gui::check_unset_button);
}

void gui::add_task() {
    string description = this->line_description->text().toStdString();
    if(description.empty())
    {
        QMessageBox::critical(this, "ERROR", "invalid input");
        return;
    }
    try {
        this->service.add_task(description, this->programmer.get_id());
    }
    catch (exception)
    {
        QMessageBox::critical(this, "ERROR", "invalid input");
        return;
    }
}

void gui::remove_task() {
    int index = this->get_selected_index();
    if(index == -1)
    {
        QMessageBox::critical(this, "ERROR", "no index selected");
        return;
    }
    string description = this->tableModel->index(index, 0).data().toString().toStdString();
    this->service.remove_task(description);

}

void gui::set_progress() {
    int index = this->get_selected_index();
    if(index == -1)
    {
        QMessageBox::critical(this, "ERROR", "no index selected");
        return;
    }
    string status = this->tableModel->index(index, 1).data().toString().toStdString();
    if(status != "open")
    {
        QMessageBox::information(this, "ATTENTION", "task has non open status!");
        return;
    }
    string desc = this->tableModel->index(index, 0).data().toString().toStdString();
    this->service.status_to_progress(desc);

}

void gui::set_closed() {
    int index = this->get_selected_index();
    if(index == -1)
    {
        QMessageBox::critical(this, "ERROR", "no index selected");
        return;
    }
    string desc = this->tableModel->index(index, 0).data().toString().toStdString();
    this->service.status_to_closed(desc);

}

void gui::check_unset_button() {
    int index = this->get_selected_index();
    if(index == -1)
    {
        QMessageBox::critical(this, "ERROR", "no index selected");
        return;
    }
    string status = this->tableModel->index(index, 1).data().toString().toStdString();
    int id = this->tableModel->index(index, 2).data().toInt();
    if(status != "in progress")
    {
        this->button_done->setDisabled(true);
    }
    if(id!= this->programmer.get_id())
        this->button_done->setDisabled(true);
    if(status == "in progress" && id == this->programmer.get_id())
    {
        this->button_done->setDisabled(false);
    }
}





