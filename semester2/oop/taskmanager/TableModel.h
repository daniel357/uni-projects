//
// Created by User on 7/4/2022.
//

#ifndef TASKMANAGER_TABLEMODEL_H
#define TASKMANAGER_TABLEMODEL_H

#include "Service.h"
#include "QAbstractTableModel"

class TableModel: public QAbstractTableModel{
private:
    Service &service;
    Programmer &programmer;
public:
    TableModel(Service& service1, Programmer& programmer1, QObject*parent = NULL);

    int rowCount(const QModelIndex &parent = QModelIndex{}) const override;

    int columnCount(const QModelIndex &parent =QModelIndex{}) const override;

    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;

//    Qt::ItemFlags flags(const QModelIndex & qModelIndex) const override;

    void refresh_data();

    ~TableModel() override;
};


#endif //TASKMANAGER_TABLEMODEL_H
