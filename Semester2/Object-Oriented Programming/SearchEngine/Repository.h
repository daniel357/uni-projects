//
// Created by User on 5/26/2022.
//

#ifndef SEARCH_ENGINE_REPOSITORY_H
#define SEARCH_ENGINE_REPOSITORY_H
#include "Domain.h"
#include "string"
#include "vector"
#include "fstream"
#include "sstream"
using namespace std;

class Repository{
private:
    vector<Domain> list;
public:
    Repository();
    ~Repository();
    void read_from_file();
    vector<Domain> get_all();

};
#endif //SEARCH_ENGINE_REPOSITORY_H
