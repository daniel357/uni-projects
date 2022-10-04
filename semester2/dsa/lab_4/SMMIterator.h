//
// Created by User on 5/18/2022.
//

#ifndef LAB_4_SMMITERATOR_H
#define LAB_4_SMMITERATOR_H
#include "SortedMultiMap.h"


class SMMIterator {
    friend class SortedMultiMap;
private:
    const SortedMultiMap& map;
    SMMIterator(const SortedMultiMap& map);

    //TODO - Representation

    SortedMultiMap::Element* elm;
    int* next_v;
    int current_pos, key_pos, first_pos;

public:
    void first();
    void next();
    bool valid() const;
    TElem getCurrent() const;
};

#endif //LAB_4_SMMITERATOR_H
