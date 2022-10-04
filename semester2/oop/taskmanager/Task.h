//
// Created by User on 7/4/2022.
//

#ifndef TASKMANAGER_TASK_H
#define TASKMANAGER_TASK_H
#include "string"
#include "iostream"
#include "vector"
#include "sstream"
#include "fstream"
using namespace std;

class Task {
private:
    string description, status;
    int id;
public:
    Task();
    ~Task();
    Task(string description, string status, int id);

    string get_description();
    string get_status();
    int get_id();

    void set_description(string desc);
    void set_status(string stat);
    void set_id(int id);

    friend istream &operator>>(istream &stream, Task &task);

    string to_str();

};


#endif //TASKMANAGER_TASK_H
