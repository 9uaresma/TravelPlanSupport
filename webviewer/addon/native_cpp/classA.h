#pragma once
#include <iostream>
#include <string>
#include <vector>

// Planを登録・表示するクラスです。
class ClassA
{
public:
    ClassA();   //コンストラクタ
    ~ClassA();  // デストラクタ

    // メンバ関数
    void set_plan(std::string plan, long hour);
    std::string show_plan();
    long ClassA::get_ttl_hours();

private:
    // メンバ変数
    int plan_num;
    long ttl_hours;

    std::vector<std::string> plans;
    std::vector<long> hours;
};
