#include<iostream>
#include<vector>
#include<string>

// Header file
#include "myclass.h"

using std::cout; using std::cin;
using std::endl; using std::string;
using std::vector;


Plan::Plan()
{
    // cout << "Constructor\n";
}

void Plan::addPlan(string plan){    
    cout << "A plan added : " << plan << endl;
    plans.push_back(plan);
}

void Plan::showPlan(){
    cout << "<< plans >>" << endl;
    for(int i=0; i<sizeof(plans); i++){
            cout << i << " : " << plans[i] << endl;
    }
}