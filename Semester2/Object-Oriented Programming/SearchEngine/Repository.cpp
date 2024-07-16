//
// Created by User on 5/26/2022.
//

#include "Repository.h"

Repository::Repository() {
    read_from_file();
}

Repository::~Repository() {

}

void Repository::read_from_file() {
    string file_name = R"(C:\Users\User\Desktop\2sem\oop\search_engine\file.txt)";
    if(!file_name.empty())
    {
        ifstream in(file_name);
        Domain item;
        while (in>>item)
        {
            this->list.push_back(item);
        }
    }
}

vector<Domain> Repository::get_all() {
    return this->list;
}
