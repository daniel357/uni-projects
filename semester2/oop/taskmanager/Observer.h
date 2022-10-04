//
// Created by User on 7/4/2022.
//

#ifndef TASKMANAGER_OBSERVER_H
#define TASKMANAGER_OBSERVER_H

#include <vector>
#include <algorithm>
#include "iostream"
using namespace std;

class Observer {
public:
    virtual void update() = 0;
    virtual ~Observer() {}
};


class Observable {
private:
    vector<Observer*> observers;

public:
    void addObserver(Observer *obs) {
        this->observers.push_back(obs);

    }

    void removeObserver(Observer* obs) {
        auto it = std::find(this->observers.begin(), this->observers.end(), obs);
        if (it != this->observers.end())
            this->observers.erase(it);
    }

    void notify () {
        for (auto obs : this->observers) {
            cout<<obs<<'\n';
            obs->update();
        }
    }
};

#endif //TASKMANAGER_OBSERVER_H
