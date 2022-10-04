//
// Created by User on 5/25/2022.
//

#include "Task.h"

Task::Task(string c, string n, vector<string> s) {
    category= c;
    name=n;
    symptoms=s;
}

Task::~Task() {
}

string Task::get_category() {
    return this->category;
}

string Task::get_name() {
    return this->name;
}

vector<string> Task::get_symptoms() {
    return this->symptoms;
}

string Task::to_str() {
    return "Category-> "+ this->category +" Name-> "+ this->name;
}

vector<string> tokenizer(const string& str, char delimiter)
{
    vector<string >result;
    stringstream ss(str);
    string token;
    while (getline(ss, token, delimiter))
        result.push_back(token);
    return result;
}

std::istream &operator>>(istream &inputStream, Task &item) {
    string line;
    getline(inputStream, line);
    vector<string > tokens;
    if(line.empty())
        return inputStream;
    tokens = tokenizer(line, '|');
    item.category=tokens[0];
    item.name= tokens[1];
    vector<string > s;
    s= tokenizer(tokens[2], ',');
    item.symptoms=s;
    return inputStream;
}

Task::Task() {

}
