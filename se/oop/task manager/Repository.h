//
// Created by User on 7/4/2022.
//

#ifndef TASKMANAGER_REPOSITORY_H
#define TASKMANAGER_REPOSITORY_H

#include "Task.h"
#include "Programmer.h"
#include "ostream"

class Repository {
private:
    vector<Task> tasks;
    vector<Programmer> programmers;

    void read_programmers_from_file();
    void read_tasks_from_file();

    void save_tasks();
public:
    Repository();
    ~Repository();

    vector<Task>& get_all_tasks();
    vector<Programmer>& get_all_programmers();

    void add_task(Task task);

    void remove_task(int position);

    void change_status_progress(int position);

    void change_status_closed(int position);


};


#endif //TASKMANAGER_REPOSITORY_H
