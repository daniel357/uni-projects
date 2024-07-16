//
// Created by User on 5/25/2022.
//

#ifndef MEDICALDISORDERS_SERVICE_H
#define MEDICALDISORDERS_SERVICE_H

#include "algorithm"
#include "vector"
#include "Task.h"
#include "string"
#include "sstream"

class Service{
private:
    vector<Task> list;
public:
    Service();
    ~Service();
    void read_from_file();

    vector<Task> sort_name();
    vector<Task> sort_symptom(string s);
    vector<string> show_symptoms_disorder(string d);

};

#endif //MEDICALDISORDERS_SERVICE_H
