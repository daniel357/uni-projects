//
// Created by User on 7/4/2022.
//

#include "Repository.h"

void Repository::read_programmers_from_file() {
    string file = R"(C:\Users\User\Desktop\2sem\oop\taskmanager\programmers.txt)";
    if(!file.empty())
    {
        ifstream in(file);
        Programmer programmer;
        while (in>>programmer)
        {
            cout<<programmer.get_name()<<'\n';
            this->programmers.push_back(programmer);
        }
    }
}

void Repository::read_tasks_from_file() {
    string file = R"(C:\Users\User\Desktop\2sem\oop\taskmanager\tasks.txt)";
    if(!file.empty())
    {
        ifstream in(file);
        Task task;
        while (in>>task)
        {
            cout<<task.get_description()<<'\n';
            this->tasks.push_back(task);
        }
    }
}

Repository::Repository() {
    this->read_programmers_from_file();
    this->read_tasks_from_file();
}

Repository::~Repository() {

}

vector<Task>& Repository::get_all_tasks() {
    return this->tasks;
}

vector<Programmer>& Repository::get_all_programmers() {
    return this->programmers;
}

void Repository::add_task(Task task) {
    this->tasks.push_back(task);
    this->save_tasks();
}

void Repository::remove_task(int position) {
    this->tasks.erase(this->tasks.begin()+position);
    this->save_tasks();
}

void Repository::change_status_progress(int position) {
    this->tasks[position].set_status("in progress");
    this->save_tasks();
}

void Repository::change_status_closed(int position) {
    this->tasks[position].set_status("closed");
    this->save_tasks();
}

void Repository::save_tasks() {
    string file_name = R"(C:\Users\User\Desktop\2sem\oop\taskmanager\tasks.txt)";
    ofstream out(file_name);
    for(auto &item: this->tasks)
    {
        out<<item.to_str()<<'\n';
    }

}

