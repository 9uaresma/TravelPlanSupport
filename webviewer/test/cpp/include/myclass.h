// #pragma once

#include<iostream>
#include<vector>
#include<string>

using std::cout; using std::cin;
using std::endl; using std::string;
using std::vector;

class Plan{
public:
    vector<string> plans;
    Plan();

    // メンバ関数
    void addPlan(string plan);
    void showPlan();
};
