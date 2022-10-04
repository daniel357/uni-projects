//
// Created by User on 5/26/2022.
//

// You may need to build the project (run Qt uic code generator) to get "ui_gui.h" resolved

#include <QListWidgetItem>
#include "gui.h"
#include "ui_gui.h"
#include "iostream"


gui::gui(QWidget *parent) :
        QWidget(parent), ui(new Ui::gui) {
    ui->setupUi(this);
    populate_list(service.sort_by_name());
    connect_signals_slots();
    filter_by_text();
    show_best_matching();
}

gui::~gui() {
    delete ui;
}

void gui::populate_list(vector<Domain> arr) {
    for(auto &i: arr)
    {
        auto *item = new QListWidgetItem(QString::fromStdString(i.to_str()));
        QFont font1;
        font1.setBold(true);
        item->setFont(font1);
        this->ui->listWidget->addItem(item);
    }
}

void gui::connect_signals_slots() {
      QObject::connect(this->ui->pushButton, &QPushButton::clicked, this, &gui::show_best_matching);
      QObject::connect(this->ui->lineEdit_search_text, &QLineEdit::textChanged, this, &gui::filter_by_text);

}

void gui::filter_by_text() {
    string text = this->ui->lineEdit_search_text->text().toStdString();
    if(!text.empty()) {
        this->ui->listWidget->clear();
        vector<Domain> filtered = service.search_by_text(text);
        this->populate_list(filtered);
    }
    else
    {
        this->ui->listWidget->clear();
        this->populate_list(service.sort_by_name());
    }
}

void gui::show_best_matching() {
    string text = this->ui->lineEdit_search_text->text().toStdString();
    cout<<text<<'\n';
    if(!text.empty()) {
        string matched = service.best_matching(text);
        this->ui->lineEdit_output->setText(QString::fromStdString("best match ->"+matched));
    }
}
