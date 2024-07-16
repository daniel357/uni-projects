//
// Created by User on 5/26/2022.
//

#ifndef SEARCH_ENGINE_SERVICE_H
#define SEARCH_ENGINE_SERVICE_H

#include "Repository.h"
#include "vector"
#include "string"

using namespace std;

class Service{
private:
    Repository repository;
public:
    Service();
    ~Service();
    vector<Domain> sort_by_name();
    Repository get_repo();
    vector<Domain> search_by_text(string text);

    string best_matching(string text);
};


#endif //SEARCH_ENGINE_SERVICE_H
