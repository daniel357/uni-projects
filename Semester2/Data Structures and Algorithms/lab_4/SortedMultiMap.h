//
// Created by User on 5/18/2022.
//

#ifndef LAB_4_SORTEDMULTIMAP_H
#define LAB_4_SORTEDMULTIMAP_H
//DO NOT INCLUDE SMMITERATOR

//DO NOT CHANGE THIS PART
#include <vector>
#include <utility>
typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
#define NULL_TVALUE -111111
#define NULL_TELEM pair<TKey, TValue>(-111111, -111111);
using namespace std;
class SMMIterator;
typedef bool(*Relation)(TKey, TKey);


class SortedMultiMap {
    friend class SMMIterator;
private:
    //TODO - Representation

    // Element has: key elm, size = length of the vector containing values, corresponding to some key , val = dynamic arr of values
    // T = hashtable (dynamic vector containing elements of type: Element)
    // m = head, first_empty = first empty position from the table, head_slla = head for the vector next_slla, length = length of the container, rel = the relationship
    // next = vector pt coalesced Verkettung, next_slla = vector pt ordinea in functie de relatie
    // h(key) = hash function

    struct Element {
        TKey key;
        int size;
        TValue* val;
    };

    Element* T;
    int m, pos, first_empty, head_slla, length;
    int* next, * next_slla;
    Relation rel;


    int h(TKey key) {
        return key % m;
    }


public:

    // constructor
    SortedMultiMap(Relation r);

    void resize_rehash();

    //adds a new key value pair to the sorted multi map
    void add(TKey c, TValue v);

    //returns the values belonging to a given key
    vector<TValue> search(TKey c);

    //removes a key value pair from the sorted multimap
    //returns true if the pair was removed (it was part of the multimap), false if nothing is removed
    bool remove(TKey c, TValue v);

    //returns the number of key-value pairs from the sorted multimap
    int size() const;

    //verifies if the sorted multimap is empty
    bool isEmpty() const;

    // returns an iterator for the sorted multimap. The iterator will return the pairs as required by the relation (given to the constructor)
    SMMIterator iterator() const;

    vector<TValue> valueBag() const;

    // destructor
    ~SortedMultiMap();
};

#endif //LAB_4_SORTEDMULTIMAP_H
