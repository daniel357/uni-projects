//
// Created by User on 5/26/2022.
//

#include "Domain.h"

string Domain::to_str() {

    string k;
    for(auto &item: this->keywords)
    {
        k.append(" "+ item +" ");
    }
    return this->name+k;
}

vector<string> tokenize(const string& str, char delimiter) {
    vector<string> result;
    stringstream ss(str);
    string token;
    while (getline(ss, token, delimiter))
        result.push_back(token);
    return result;
}

std::istream &operator>>(istream &inputStream, Domain &item) {
    string line;
    getline(inputStream, line);
    vector<string> tokens;
    if(line.empty())
        return inputStream;
    tokens = tokenize(line, '|');
    item.name=tokens[0];
    item.content=tokens[2];
    vector<string >k_tok;
    k_tok= tokenize(tokens[1], ',');
    item.keywords=k_tok;
    return inputStream;
}

Domain::Domain() {

}

Domain::~Domain() {

}

string Domain::get_name() {
    return this->name;
}

string Domain::get_content() {
    return this->content;
}

vector<string> Domain::get_keywords() {
    return this->keywords;
}
