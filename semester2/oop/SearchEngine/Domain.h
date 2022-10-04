//
// Created by User on 5/26/2022.
//

#ifndef SEARCH_ENGINE_DOMAIN_H
#define SEARCH_ENGINE_DOMAIN_H
#include "vector"
#include "sstream"
#include "string"
using namespace std;

class Domain{
private:
    string name;
    vector<string > keywords;
    string content;
public:
    Domain();
    ~Domain();
    string get_name();
    string get_content();
    vector<string> get_keywords();

    string to_str();
    friend std::istream& operator>>(std::istream& inputStream, Domain& item);


};
#endif //SEARCH_ENGINE_DOMAIN_H
