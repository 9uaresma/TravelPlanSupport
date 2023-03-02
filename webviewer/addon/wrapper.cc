#include "wrapper.h"
#include <napi.h>

using namespace Napi;

// ---------------------------------------------------------- //
// ---------------------のり付け部分--------------------------- //
// ---------------------------------------------------------- //
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
            InstanceMethod("showPlan", &Wrapper::showPlan),
            InstanceMethod("getTtlHours", &Wrapper::getTtlHours),
        });

    Napi::FunctionReference *constructor = new Napi::FunctionReference();
    *constructor = Napi::Persistent(func);
    env.SetInstanceData(constructor);

    exports.Set("Wrapper", func);
    return exports;
}

// ---------------------------------------------------------- //
// ---------- これより下で ClassAのラッピングを定義する ----------- //
// ---------------------------------------------------------- //

// コンストラクタ
Wrapper::Wrapper(const Napi::CallbackInfo &info)
    : Napi::ObjectWrap<Wrapper>(info)
{
    m_classA = new ClassA();
};

Wrapper::~Wrapper()
{
    delete m_classA;
    m_classA = nullptr;
};

// メンバ関数
Napi::Value Wrapper::setPlan(const Napi::CallbackInfo &info)
{
    Napi::Env env = info.Env();
    std::string plan_name = info[0].As<Napi::String>().ToString();
    int plan_hour = info[1].As<Napi::Number>().Int32Value();
    m_classA->set_plan(plan_name, plan_hour);
    return env.Null();
}

Napi::Value Wrapper::showPlan(const Napi::CallbackInfo &info)
{
    Napi::Env env = info.Env();
    std::string ans = m_classA->show_plan();
    return Napi::String::New(env, ans);
}

Napi::Value Wrapper::getTtlHours(const Napi::CallbackInfo &info)
{
    Napi::Env env = info.Env();
    long ttl_hours = m_classA->get_ttl_hours();
    return Napi::Number::New(env, ttl_hours);
}
