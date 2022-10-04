#include "ShortTest.h"
#include "ExtendedTest.h"
#include "iostream"

int main(){
    testAll();
    testAllExtended();

    std::cout<<"Finished SMM Tests!"<<std::endl;
    system("pause");
}
