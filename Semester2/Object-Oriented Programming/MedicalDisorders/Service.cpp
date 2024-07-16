//
// Created by User on 5/25/2022.
//

#include <fstream>
#include "Service.h"

Service::Service() {
    this->read_from_file();
}

Service::~Service() {

}

void Service::read_from_file() {
    string file_name = (R"(C:\Users\User\Desktop\2sem\oop\MedicalDisorders\input.txt)");
    if(!file_name.empty())
    {
        ifstream in(file_name);
        Task t;
        while (in>>t)
        {
            this->list.push_back(t);
        }
    }
}

vector<Task> Service::sort_name() {
    vector<Task> v = this->list;
    for(int i=0; i< this->list.size()-1; ++i)
    {
        for(int j=i+1; j< this->list.size(); j++)
        {
            if(v[i].get_name() > v[j].get_name())
            {
                swap(v[i], v[j]);
            }
        }
    }
    return v;
}

vector<Task> Service::sort_symptom(string s) {
    vector<Task> v;
    for(auto &item: this->list)
    {
        for(auto &i: item.get_symptoms())
        {
            if(i.find(s)!=string::npos)
            {
                v.push_back(item);
                break;
            }
        }
    }
    return v;
}

vector<string> Service::show_symptoms_disorder(string d) {
    vector<string> v;
    for(auto &item: this->list)
    {
        if(item.get_name() == d)
        {
            return item.get_symptoms();
        }
    }
    return v;
}




