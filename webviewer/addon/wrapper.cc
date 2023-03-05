#include "wrapper.h"
#include <napi.h>

using namespace Napi;

// new() の定義
Napi::Object Wrapper::NewInstance(Napi::Env env, const Napi::CallbackInfo &info)
{
    Napi::EscapableHandleScope scope(env);
    // jsからコンストラクタに渡されるArgsは infoに配列として入っている
    const std::initializer_list<napi_value> initArgList = {info[0]};
    // ここでWrapper:::Wrapper()が呼ばれる
    Napi::Object obj = env.GetInstanceData<Napi::FunctionReference>()->New(initArgList);
    // gcにメモリ解放されないようにスコープを除外する
    return scope.Escape(napi_value(obj)).ToObject();
}

//　メンバ関数のバインド
Napi::Object Wrapper::Init(Napi::Env env, Napi::Object exports)
{
    Napi::Function func = DefineClass(
        env, "Wrapper", {
            // ここにメソッドを登録する
            InstanceMethod("setPlan", &Wrapper::setPlan),
            InstanceMethod("getPlans", &Wrapper::getPlans),
            InstanceMethod("getHours", &Wrapper::getHours),
            InstanceMethod("showPlan", &Wrapper::showPlan),
            InstanceMethod("getTtlHours", &Wrapper::getTtlHours),
            InstanceMethod("swapPlanElements", &Wrapper::swapPlanElements),
            InstanceMethod("setDepartureDate", &Wrapper::setDepartureDate),
            InstanceMethod("getDepartureDate", &Wrapper::getDepartureDate),
        });

    Napi::FunctionReference *constructor = new Napi::FunctionReference();
    *constructor = Napi::Persistent(func);
    env.SetInstanceData(constructor);

    exports.Set("Wrapper", func);
    return exports;
}

// ---------------------------------------------------------- //
// ---------- これより下で Classのラッピングを定義する ----------- //
// ---------------------------------------------------------- //

// コンストラクタ
Wrapper::Wrapper(const Napi::CallbackInfo &info)
    : Napi::ObjectWrap<Wrapper>(info)
{
    m_class = new PlanContainer();
};

Wrapper::~Wrapper()
{
    delete m_class;
    m_class = nullptr;
};

// メンバ関数
Napi::Value Wrapper::setPlan(const Napi::CallbackInfo &info)
{
    Napi::Env env = info.Env();
    std::string plan_name = info[0].As<Napi::String>().ToString();
    int plan_hour = info[1].As<Napi::Number>().Int32Value();
    m_class->set_plan(plan_name, plan_hour);
    return env.Null();
}


Napi::Value Wrapper::getPlans(const Napi::CallbackInfo &info)
{
    Napi::Env env = info.Env();
    std::vector<std::string> plans = m_class->get_plans();
    Napi::Array outArr = Napi::Array::New(env, plans.size());
    for (size_t i=0; i < plans.size(); i++){
        outArr[i] = Napi::String::New(env, plans[i]);
    }
    return outArr;
}

Napi::Value Wrapper::getHours(const Napi::CallbackInfo &info)
{
    Napi::Env env = info.Env();
    std::vector<long> hours = m_class->get_hours();
    Napi::Array outArr = Napi::Array::New(env, hours.size());
    for (size_t i=0; i < hours.size(); i++){
        outArr[i] = Napi::Number::New(env, hours[i]);
    }
    return outArr;
}

Napi::Value Wrapper::showPlan(const Napi::CallbackInfo &info)
{
    Napi::Env env = info.Env();
    std::string ans = m_class->show_plan();
    return Napi::String::New(env, ans);
}

Napi::Value Wrapper::getTtlHours(const Napi::CallbackInfo &info)
{
    Napi::Env env = info.Env();
    long ttl_hours = m_class->get_ttl_hours();
    return Napi::Number::New(env, ttl_hours);
}

Napi::Value Wrapper::swapPlanElements(const Napi::CallbackInfo &info)
{
    Napi::Env env = info.Env();
    int i = info[0].As<Napi::Number>().Int32Value();
    int j = info[1].As<Napi::Number>().Int32Value();
    int ret = m_class->swap_plan_elements(i, j);
    return Napi::Number::New(env, ret);
}

Napi::Value Wrapper::setDepartureDate(const Napi::CallbackInfo &info)
{
    Napi::Env env = info.Env();
    int month = info[0].As<Napi::Number>();
    int date = info[1].As<Napi::Number>();
    int hour = info[2].As<Napi::Number>();
    int min = info[3].As<Napi::Number>();
    m_class->set_departure_date(month, date, hour, min);
    return env.Null();
}

Napi::Value Wrapper::getDepartureDate(const Napi::CallbackInfo &info)
{
    Napi::Env env = info.Env();
    std::vector<int> dep_date = m_class->get_departure_date();
    Napi::Array outArr = Napi::Array::New(env, dep_date.size());
    for (size_t i=0; i < dep_date.size(); i++){
        outArr[i] = Napi::Number::New(env, dep_date[i]);
    }
    return outArr;
}