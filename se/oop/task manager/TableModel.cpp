//
// Created by User on 7/4/2022.
//

#include "TableModel.h"

#include <QFont>
#include <QBrush>
#include "TableModel.h"

TableModel::TableModel(Service &service1, Programmer &programmer1, QObject *parent):service{service1}, programmer{programmer1} {

}

int TableModel::rowCount(const QModelIndex &parent) const {
    return this->service.get_tasks().size();
}

int TableModel::columnCount(const QModelIndex &parent) const {
    return 3;
}

QVariant TableModel::data(const QModelIndex &index, int role) const {
    int row = index.row();
    int column = index.column();

    vector<Task> tasks = this->service.get_tasks_sorted_status();
    Task task = tasks[row];
    if(role == Qt::DisplayRole || role == Qt::EditRole)
    {
        if(column == 0)
            return QString::fromStdString(task.get_description());
        else if(column == 1)
            return QString::fromStdString(task.get_status());
        else if(column == 2)
            return QString::fromStdString(to_string(task.get_id()));
    }
    if(role == Qt::FontRole){
        QFont font("Helvetica", 15, 10, true);
        font.setItalic(false);
        return font;
    }
//    if(role == Qt::BackgroundRole)
//    {
//        if(tasks[row].get_id() == this->programmer.get_id())
//        {
//            return QBrush{Qt::blue};
//        }
//    }
    return QVariant{};
}

QVariant TableModel::headerData(int section, Qt::Orientation orientation, int role) const {
    if(role == Qt::DisplayRole && orientation == Qt::Horizontal)
    {
        if(section == 0)
            return QString{"Description"};
        else if(section == 1)
            return QString{"Status"};
        else if(section == 2)
            return QString{"Id"};
    }

    if(role == Qt::FontRole)
    {
        QFont font("Helvetica", 15, 10, true);
        font.setBold(true);
        font.setItalic(false);
        return font;
    }
    return QVariant{};
}
//
//Qt::ItemFlags TableModel::flags(const QModelIndex &qModelIndex) const {
//    return Qt::ItemIsEditable | Qt::ItemIsSelectable | Qt::ItemIsEnabled;
//}

void TableModel::refresh_data() {
    endResetModel();
}

TableModel::~TableModel() {

}