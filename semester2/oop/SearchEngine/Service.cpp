//
// Created by User on 5/26/2022.
//

#include "Service.h"
#include "iostream"

Service::Service() {
    this->repository =Repository();
}

Service::~Service() {

}

vector<Domain> Service::sort_by_name() {
    vector<Domain> sorted = this->repository.get_all();
    for(int i=0; i<sorted.size()-1; ++i)
    {
        for(int j=i+1; j< sorted.size(); ++j)
        {
            if(sorted[i].get_name()> sorted[j].get_name())
            {
                swap(sorted[i], sorted[j]);
            }
        }
    }
    return sorted;
}

Repository Service::get_repo() {
    return this->repository;
}

vector<Domain> Service::search_by_text(string text) {
    vector<Domain> searched;
    vector<Domain> list =this->repository.get_all();
    for(auto &item: list)
    {
        if (item.get_name().find(text)!=string::npos)
            searched.push_back(item);
        else
        {
            for(auto &i: item.get_keywords())
            {
                if(i.find(text)!= string::npos)
                    searched.push_back(item);
            }
        }
    }
    return searched;
}

string Service::best_matching(string text) {
    string best;
    double ratio=0;
    vector<Domain> searched= this->search_by_text(text);
    for(auto &item: searched)
    {
        cout<<(double)text.size()/item.get_name().size()<<'\n';
        if((double)text.size()/item.get_name().size() > ratio)
        {
            ratio=(double)text.size()/item.get_name().size();
            best=item.get_name();
            cout<<item.get_name()<<" "<<best<<'\n';
        }
    }
    return best;
}



