#pragma once
//DO NOT INCLUDE SMMITERATOR

//DO NOT CHANGE THIS PART
#include <vector>
#include <utility>
typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
typedef TValue(*Transformer)(TKey, TValue);
#define NULL_TVALUE -111111
#define NULL_TELEM pair<TKey, TValue>(-111111, -111111);
using namespace std;
class SMMIterator;
class ValueIterator;
typedef bool(*Relation)(TKey, TKey);


struct BSTNode{
    TElem data = NULL_TELEM;
    BSTNode *left = nullptr, *right = nullptr;
};

class SortedMultiMap {
    friend class ValueIterator;
    friend class SMMIterator;
private:
    BSTNode *bst;
    Relation r;
    int length;
    BSTNode *create_node(TKey c, TValue v);
    void insert_rec(BSTNode *bst, TKey c, TValue v);
public:

    // constructor
    SortedMultiMap(Relation r);

    //adds a new key value pair to the sorted multi map
    void add(TKey c, TValue v);

    //returns the values belonging to a given key
    vector<TValue> search(TKey c) const;

    //removes a key value pair from the sorted multimap
    //returns true if the pair was removed (it was part of the multimap), false if nothing is removed
    bool remove(TKey c, TValue v);

    //returns the number of key-value pairs from the sorted multimap
    int size() const;

    //verifies if the sorted multi map is empty
    bool isEmpty() const;

    // returns an iterator for the sorted multimap. The iterator will returns the pairs as required by the relation (given to the constructor)	
    SMMIterator iterator() const;


    // destructor
    ~SortedMultiMap();


    void replaceInOrderRecursive(BSTNode *startNode, Transformer t);

    //replaces the value of every key, with the result given by a function invoked on the pair.
    void replaceAll(Transformer  t);
};