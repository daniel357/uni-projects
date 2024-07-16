#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
#include <vector>
#include <exception>
using namespace std;


//T(1)
BSTNode *SortedMultiMap::create_node(TKey c, TValue v){
    BSTNode *new_node;
    new_node =  new BSTNode;
    new_node->data = make_pair(c, v);
    return new_node;
}

//O(n)
void SortedMultiMap::insert_rec(BSTNode *node, TKey c, TValue v){
    if(!r(node->data.first, c)){
        if(node->left == nullptr){
            node->left = create_node(c, v);
            return;
        }
        insert_rec(node->left, c, v);
    }
    else{
        if(node->right == nullptr){
            node->right = create_node(c, v);
            return;
        }
        insert_rec(node->right, c, v);
    }
}

//T(1)
SortedMultiMap::SortedMultiMap(Relation r) {
    this->r = r;
    length = 0;
    bst = nullptr;
}

//O(n)
void SortedMultiMap::add(TKey c, TValue v) {
    length++;

    if(bst == nullptr){ // we don t have a root
        bst = create_node(c, v);
    }
    else{ // we have a root
        insert_rec(bst, c, v);
    }
}

//O(n)
vector<TValue> SortedMultiMap::search(TKey c) const {
    if(bst == nullptr)
        return vector<TValue>();
    vector<TValue> values;
    BSTNode *current_node;

    current_node = bst;
    while(current_node != nullptr){
        if(current_node->data.first == c){
            values.push_back(current_node->data.second);
        }
        if(!r(current_node->data.first, c))
            current_node = current_node->left;
        else
            current_node = current_node->right;
    }
    return values;
}

//O(n)
bool SortedMultiMap::remove(TKey c, TValue v) {
    BSTNode* current_node = bst;
    auto pair = make_pair(c, v);
    BSTNode* prev;
    bool right = false, root = false;
    while(current_node != nullptr){
        if(current_node->data == pair)
            break;
        prev = current_node;
        if(!r(current_node->data.first, c)){
            current_node = current_node->left;
            right = false;
        }
        else{
            current_node = current_node->right;
            right = true;
        }
    }
    if(current_node == bst)
        root = true;
    if(current_node == nullptr)
        return false;
    if(current_node->left == nullptr && current_node->right == nullptr){
        length--;/// the node to be deleted is a leaf
        if(root){
            delete bst;
            bst = nullptr;
            return true;
        }
        delete current_node;
        current_node = nullptr;
        if(right)
            prev->right = nullptr;
        else
            prev->left = nullptr;
        return true;
    }
    if(current_node->left == nullptr && current_node->right != nullptr){
        length--;//if the node has only one child we link the previous one to it's child
        if(root){
            bst = current_node->right;
            delete current_node;
            current_node = nullptr;
            return true;
        }
        if(right)
            prev->right = current_node->right;
        else
            prev->left = current_node->right;
        delete current_node;
        current_node = nullptr;
        return true;
    }
    if(current_node->left != nullptr && current_node->right == nullptr){
        length--;
        if(root){
            bst = current_node->left;
            delete current_node;
            current_node = nullptr;
            return true;
        }
        if(right)
            prev->right = current_node->left;
        else
            prev->left = current_node->left;
        delete current_node;
        current_node = nullptr;
        return true;
    }
    if(current_node->left != nullptr && current_node->right != nullptr){
        if(root)//if the node has 2 children and it is root
        {
            length--;
            BSTNode* left_node, *right_node;

            left_node = bst->left;
            right_node = bst->right;
            prev = current_node;
            current_node = bst->right;
            while(current_node->left != nullptr){
                prev = current_node;
                current_node = current_node->left;
            }
            if(current_node == bst->right){
                bst->data = current_node->data;
                bst->left = left_node;
                bst->right = current_node->right;
            }
            else{
                bst->data = current_node->data;
                prev->left = nullptr;
                bst->left = left_node;
                bst->right = right_node;
            }
            delete current_node;
            current_node = nullptr;
            return true;
        }
        else{//the node has 2 children and is not the root
            length--;
            BSTNode* left_node, *right_node, *keep_right_node, *c_node, *p_node;
            p_node = current_node;
            keep_right_node = current_node;
            c_node = current_node->right;
            left_node = current_node->left;
            right_node = current_node->right;
            while(c_node->right != nullptr){
                prev = c_node;
                c_node = c_node->left;
            }
            if(c_node == current_node->right){
                current_node->data = c_node->data;
                current_node->left = left_node;
                current_node->right = c_node->right;
            }
            else{
                current_node->data = c_node->data;
                prev->left = nullptr;
                current_node->left = left_node;
                current_node->right = right_node;
            }
            delete c_node;
            current_node = nullptr;
            return true;
        }
    }
}

//T(1)
int SortedMultiMap::size() const {
    return length;
}

//T(1)
bool SortedMultiMap::isEmpty() const {
    return length == 0;
}

SMMIterator SortedMultiMap::iterator() const {
    return SMMIterator(*this);
}

SortedMultiMap::~SortedMultiMap() {
}

void SortedMultiMap::replaceInOrderRecursive(BSTNode *startNode, Transformer t) {
    if (startNode != nullptr) {
        this->replaceInOrderRecursive(startNode->left, t);
        TValue value = t(startNode->data.first, startNode->data.second);
        startNode->data.second = value;
        this->replaceInOrderRecursive(startNode->right, t);
    }
}
//Theta(n)

void SortedMultiMap::replaceAll(Transformer  t) {
    BSTNode* startNode = this->bst;
    this->replaceInOrderRecursive(startNode, t);
}