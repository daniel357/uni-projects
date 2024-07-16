//
// Created by User on 5/18/2022.
//

#ifndef LAB_5_SMMITERATOR_H
#define LAB_5_SMMITERATOR_H
#include "SortedMultiMap.h"
#include <stack>
#pragma once

#include <stack>

//creates an iterator over the values associated to key k.  If k is not in the SortedMultiMap the iterator is invalid after creation, otherwise, the current element is the first value associated to the key

//Create the ValueIterator class with the same operations as the regular SortedMultiMapIterator, except that the constructor of the ValueIterator receives as parameter the SortedMultiMap and the key and the getCurrent operation returns a TValue.


class SMMIterator{
    friend class SortedMultiMap;
private:
    //DO NOT CHANGE THIS PART
    const SortedMultiMap& map;
    SMMIterator(const SortedMultiMap& map);
    BSTNode *node;
    stack<BSTNode*> it_stack;
    stack<BSTNode*> previous_stack;
    BSTNode *current_node;

public:
    void previous();
    void first();
    void next();
    bool valid() const;
    TElem getCurrent() const;
};



#endif //LAB_5_SMMITERATOR_H
