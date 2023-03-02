//#include "pch.h"
#include "classA.h"
#include <iostream>
#include <string>
#include <sstream>


ClassA::ClassA() {
    plan_num = 0;
    ttl_hours = 0.0;
}

ClassA::~ClassA()
{
}

// Planを登録する
void ClassA::set_plan(std::string plan, long hour) {
    plans.push_back(plan);
    hours.push_back(hour);
    plan_num++;
    ttl_hours = ttl_hours + hour;
}

// Planを表示する
std::string ClassA::show_plan() {
    std::stringstream ss;
    // ss << m_plan << " : " << m_hour << " hours " << std::endl;
    ss << "plan_num = " << plan_num << std::endl;
    for(int i=0; i<plan_num; i++){
        ss << plans[i] << " : " << hours[i] << " hours " << std::endl;
    }

    return ss.str();
}

// TTLの時間を返す
long ClassA::get_ttl_hours() {
    return ttl_hours;
}