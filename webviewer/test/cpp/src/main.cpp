#include<iostream>
#include<vector>
#include<string>

// Header file
#include "../include/myclass.h"

using std::cout; using std::cin;
using std::endl; using std::string;
using std::vector;




int main(){
    Plan plan;
    plan.addPlan("Plan1");
    plan.addPlan("Plan2");
    plan.showPlan();
}