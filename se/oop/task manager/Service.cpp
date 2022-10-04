//
// Created by User on 7/4/2022.
//

#include "Service.h"

Service::Service() {
    this->repository=Repository();
}

Service::~Service() {

}

vector<Task> &Service::get_tasks() {
    return this->repository.get_all_tasks();
}

vector<Programmer> &Service::get_programmers() {
    return this->repository.get_all_programmers();
}

vector<Task> Service::get_tasks_sorted_status() {
    vector<Task> t = this->repository.get_all_tasks();
    for (int i = 0; i < t.size(); ++i) {
        for (int j = 0; j < t.size(); ++j) {
            if(t[i].get_status()>t[j].get_status())
                swap(t[i], t[j]);
        }
    }
    return t;
}

void Service::add_task(string description, int id) {
    bool found = false;
    for(auto &item: this->repository.get_all_tasks())
        if (item.get_description() == description)
            found= true;
    if (found== true)
    {
        throw exception();
        return;
    }
    Task task = Task(description, "open", id);
    this->repository.add_task(task);
    this->notify();
}

void Service::remove_task(string description) {
    int pos_at;
    for (int i = 0; i < this->get_tasks().size(); ++i) {
        if(this->get_tasks()[i].get_description() == description)
        {
            pos_at=i;
        }
    }
    this->repository.remove_task(pos_at);
    this->notify();
}

void Service::status_to_progress(string description) {
    int pos_at;
    for (int i = 0; i < this->get_tasks().size(); ++i) {
        if(this->get_tasks()[i].get_description() == description)
        {
            pos_at=i;
        }
    }
    this->repository.change_status_progress(pos_at);
    this->notify();
}

void Service::status_to_closed(string description) {
    int pos_at;
    for (int i = 0; i < this->get_tasks().size(); ++i) {
        if(this->get_tasks()[i].get_description() == description)
        {
            pos_at=i;
        }
    }    this->repository.change_status_closed(pos_at);
    this->notify();
}
