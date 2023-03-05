#include "planContainer.h"
#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

std::vector<int> getDateInt() {
    time_t t = time(nullptr);
    const tm* localTime = localtime(&t);

    std::vector<int> s;
    s = {
        localTime->tm_mon+1,
        localTime->tm_mday,
        localTime->tm_hour,
        localTime->tm_min
    };
    return s;
}

PlanContainer::PlanContainer() {
    plan_num = 0;
    ttl_hours = 0.0;
    departure_date = getDateInt();  //現在の日時で初期化
}

PlanContainer::~PlanContainer()
{
}

// Planを登録する
void PlanContainer::set_plan(std::string plan, long hour) {
    plans.push_back(plan);
    hours.push_back(hour);
    plan_num++;
    ttl_hours = ttl_hours + hour;
}

std::vector<std::string> PlanContainer::get_plans(){
    return plans;
}

std::vector<long> PlanContainer::get_hours(){
    return hours;
}

// Planを表示する
std::string PlanContainer::show_plan() {
    std::stringstream ss;
    // ss << m_plan << " : " << m_hour << " hours " << std::endl;
    ss << "plan_num = " << plan_num << std::endl;
    for(int i=0; i<plan_num; i++){
        ss << plans[i] << " : " << hours[i] << " hours " << std::endl;
    }

    return ss.str();
}

// TTLの時間を返す
long PlanContainer::get_ttl_hours() {
    return ttl_hours;
}

/// @brief plansとhours配列の順番を入れ替える
/// @param i 
/// @param j 
int PlanContainer::swap_plan_elements(int i, int j) {
    std::string tmp_plan;
    long tmp_hour;
    if (sizeof(plans) > i && sizeof(hours) > j){
        tmp_plan = plans[j];
        tmp_hour = hours[j];

        plans[j] = plans[i];
        hours[j] = hours[i];

        plans[i] = tmp_plan;
        hours[i] = tmp_hour;
    } else{
        return -1;
    }
    return 0;
}

void PlanContainer::set_departure_date(int month, int date, int hour, int min){
    departure_date[0] = month;
    departure_date[1] = date;
    departure_date[2] = hour;
    departure_date[3] = min;
}

std::vector<int> PlanContainer::get_departure_date(){
    return departure_date;
}
