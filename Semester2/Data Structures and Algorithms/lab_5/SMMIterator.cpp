#include "SMMIterator.h"
#include <iostream>
#include "SortedMultiMap.h"


//O(n)
SMMIterator::SMMIterator(const SortedMultiMap& d) : map(d){
    node = map.bst;
    while(node != nullptr){
        it_stack.push(node);
        node = node->left;
    }
    if(!it_stack.empty()) {
        current_node = it_stack.top();
        this->previous_stack.push(current_node);
    }
    else
        current_node = nullptr;
}
//O(n)
void SMMIterator::first(){
    while(!it_stack.empty())
        it_stack.pop();
    node = map.bst;
    while(node != nullptr){
        it_stack.push(node);
        node = node->left;
    }
    if(!it_stack.empty()) {
        current_node = it_stack.top();
    }
    else
        current_node = nullptr;
}

void SMMIterator::previous() {
    if(this->previous_stack.size()<=1) {
        this->current_node =nullptr;
        throw std::out_of_range("out of range");
    }
    this->previous_stack.pop();
    this->current_node = previous_stack.top();
}
//O(n)
void SMMIterator::next(){
    if(it_stack.empty())
        throw std::out_of_range("out of range");
    BSTNode *node = it_stack.top();
    it_stack.pop();
    if(node->right != nullptr){
        node = node->right;
        while(node != nullptr){
            it_stack.push(node);
            node = node->left;
        }
    }
    if(!it_stack.empty()){
        current_node = it_stack.top();
        this->previous_stack.push(current_node);
    }
    else
        current_node = nullptr;
}



//T(1)
bool SMMIterator::valid() const{
    if(current_node == nullptr)
        return false;
    return true;
}
//T(1)
TElem SMMIterator::getCurrent() const{
    if(valid())
        return current_node->data;
    throw std::out_of_range("out of range");
}


