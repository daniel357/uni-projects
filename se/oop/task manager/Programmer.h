//
// Created by User on 7/4/2022.
//

#ifndef TASKMANAGER_PROGRAMMER_H
#define TASKMANAGER_PROGRAMMER_H

#include "string"
#include "iostream"
#include "vector"
#include "sstream"
#include "fstream"

using namespace std;

class Programmer {
private:
    string name;
    int id;
public:
    Programmer();
    ~Programmer();
    Programmer(int id, string name);

    string get_name();
    int get_id();
    friend istream &operator>>(istream &stream, Programmer &programmer);

    string to_str();
};


#endif //TASKMANAGER_PROGRAMMER_H
