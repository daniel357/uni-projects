//
// Created by User on 7/4/2022.
//

#ifndef TASKMANAGER_SERVICE_H
#define TASKMANAGER_SERVICE_H

#include "Repository.h"
#include "Observer.h"


class Service: public Observable{
private:
    Repository repository;
public:
    Service();
    ~Service();

    vector<Task> & get_tasks();
    vector<Programmer> &get_programmers();

    vector<Task> get_tasks_sorted_status();

    void add_task(string description, int id);

    void remove_task(string d);

    void status_to_progress(string d);

    void status_to_closed(string d);

};


#endif //TASKMANAGER_SERVICE_H
