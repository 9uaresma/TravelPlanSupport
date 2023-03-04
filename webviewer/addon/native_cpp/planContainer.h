#pragma once
#include <iostream>
#include <string>
#include <vector>

// Planを登録・表示するクラス
class PlanContainer
{
public:
    PlanContainer();   //コンストラクタ
    ~PlanContainer();  // デストラクタ

    // メンバ関数
    void set_plan(std::string plan, long hour);
    std::string show_plan();
    long get_ttl_hours();
    int swap_plan_elements(int i, int j);
    std::vector<std::string> PlanContainer::get_plans();
    std::vector<long> PlanContainer::get_hours();

private:
    // メンバ変数
    int plan_num;
    long ttl_hours;

    std::vector<std::string> plans;
    std::vector<long> hours;
};
