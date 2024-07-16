//
// Created by User on 5/25/2022.
//

#ifndef MEDICALDISORDERS_TASK_H
#define MEDICALDISORDERS_TASK_H

#include "vector"
#include "string"
#include "sstream"
using namespace std;

class Task{
private:
    string category, name;
    vector<string> symptoms;
public:
    Task();
    Task(string c, string n, vector<string> s);
    ~Task();

    string get_category();
    string get_name();
    vector<string> get_symptoms();

    friend std::istream& operator>>(std::istream& inputStream, Task& item);
    string to_str();
};

#endif //MEDICALDISORDERS_TASK_H
