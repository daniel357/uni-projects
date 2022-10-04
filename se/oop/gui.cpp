//
// Created by User on 5/25/2022.
//

// You may need to build the project (run Qt uic code generator) to get "ui_gui.h" resolved

#include "gui.h"
#include "ui_gui.h"
#include <QDialog>
#include <QMessageBox>


gui::gui(QWidget *parent) :
        QWidget(parent), ui(new Ui::gui) {
    ui->setupUi(this);
    populate_list(serv.sort_name());
    connect_slots_and_shit();
}

gui::~gui() {
    delete ui;
}

void gui::populate_list(vector<Task> sorted_tasks) {
    for(auto &item1: sorted_tasks)
    {
        if(item1.get_symptoms().size() >2)
        {
            auto *item = new QListWidgetItem(QString::fromStdString(item1.to_str()));
            QFont font1;
            font1.setBold(true);
            item->setFont(font1);
            this->ui->listWidget_disorder->addItem(item);
        } else{
            auto *item = new QListWidgetItem(QString::fromStdString(item1.to_str()));
            this->ui->listWidget_disorder->addItem(item);
        }
    }
}
void gui::populate_list_string(vector<string> sorted_tasks) {
    for(auto &item1: sorted_tasks)
    {
        auto *item = new QListWidgetItem(QString::fromStdString(item1));
        this->ui->listWidget_symptoms->addItem(item);
    }
}

void gui::connect_slots_and_shit() {
    QObject::connect(this->ui->lineEdit_search_symptom, &QLineEdit::textChanged, this, &gui::search_symptoms);
    QObject::connect(this->ui->pushButton_symptoms, &QPushButton::clicked, this, &gui::show_symptoms_disorder);
}

void gui::search_symptoms() {
    this->ui->listWidget_disorder->clear();
    string text = this->ui->lineEdit_search_symptom->text().toStdString();
    if(text.empty())
        populate_list(serv.sort_name());
    else
    {
        vector<Task> v= serv.sort_symptom(text);
        this->populate_list(v);
    }
}

void gui::show_symptoms_disorder() {
    string d = this->ui->lineEdit_disorder_input->text().toStdString();
    this->ui->listWidget_symptoms->clear();
    vector<string> v= serv.show_symptoms_disorder(d);
    this->populate_list_string(v);
}
