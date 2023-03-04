#ifndef WRAPPER
#define WRAPPER

#include <napi.h> // 必要なヘッダ
#include "./native_cpp/planContainer.h"

class Wrapper : public Napi::ObjectWrap<Wrapper> {
public:
    static Napi::Object Init(Napi::Env env, Napi::Object exports);
    static Napi::Object NewInstance(Napi::Env env, const Napi::CallbackInfo& info);

    Wrapper(const Napi::CallbackInfo& info);
    ~Wrapper();

    // クラスAのラッピング関数
    Napi::Value setPlan(const Napi::CallbackInfo &info);
    Napi::Value getPlans(const Napi::CallbackInfo &info);
    Napi::Value getHours(const Napi::CallbackInfo &info);
    Napi::Value showPlan(const Napi::CallbackInfo &info);
    Napi::Value getTtlHours(const Napi::CallbackInfo &info);
    Napi::Value swapPlanElements(const Napi::CallbackInfo &info);

private:
    PlanContainer* m_class;
};

#endif