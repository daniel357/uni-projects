//
// Created by User on 7/4/2022.
//

#include "Task.h"

Task::Task() {

}

Task::~Task() {

}

Task::Task(string description, string status, int id) {
    this->description=description;
    this->status=status;
    this->id=id;
}

string Task::get_description() {
    return this->description;
}

string Task::get_status() {
    return this->status;
}

int Task::get_id() {
    return this->id;
}

void Task::set_description(string desc) {
    this->description=desc;
}

void Task::set_status(string stat) {
    this->status=stat;
}

void Task::set_id(int id) {
    this->id=id;
}

static vector<string> tokenize(string line, char delimiter)
{
    vector<string> data;
    stringstream ss(line);
    string token;
    while (getline(ss, token, delimiter))
    {
        data.push_back(token);
    }
    return data;
}


istream &operator>>(istream &stream, Task &task) {
    string line;
    getline(stream, line);
    vector<string> data =tokenize(line, ';');
    if(data.size()!=3)
        return stream;
    task.id= stoi(data[2]);
    task.description=data[0];
    task.status=data[1];
    return stream;
}

string Task::to_str() {
    return this->description+";"+ this->status+";"+ to_string(this->id);
}
