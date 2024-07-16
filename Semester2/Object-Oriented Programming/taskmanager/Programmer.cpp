//
// Created by User on 7/4/2022.
//

#include "Programmer.h"

Programmer::Programmer() {

}

Programmer::~Programmer() {

}

Programmer::Programmer(int id, string name) {
    this->id=id;
    this->name=name;
}

string Programmer::get_name() {
    return this->name;
}

int Programmer::get_id() {
    return this->id;
}

static vector<string> tokenize(string line, char delimiter)
{
    vector<string> data;
    stringstream ss(line);
    string token;
    while (getline(ss, token, delimiter))
    {
        data.push_back(token);
    }
    return data;
}

istream &operator>>(istream &stream, Programmer &programmer) {
    string line;
    getline(stream, line);
    vector<string> data =tokenize(line, ';');
    if(data.size()!=2)
        return stream;
    programmer.id= stoi(data[0]);
    programmer.name=data[1];
    return stream;

}

string Programmer::to_str() {
    return to_string(this->id) +";"+ this->name;
}
