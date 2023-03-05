#pragma once
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

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

    void set_departure_date(int month, int date, int hour, int min);
    std::vector<int> get_departure_date();

private:
    // メンバ変数
    int plan_num;   // プランの数
    long ttl_hours; // トータルの所要時間

    std::vector<int> departure_date; //MM, dd, HH, mm 形式の出発日時 

    std::vector<std::string> plans;     // プラン名
    std::vector<long> hours;            // 所要時間
    std::vector<std::string> move_ways; // 移動手段
    std::vector<long> move_hours;       // 移動時間
};
