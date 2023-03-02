#include <napi.h>
#include "wrapper.h"
#include <iostream>

// jsオブジェクトが初期化された時 new()の呼び出し
Napi::Object CreateObject(const Napi::CallbackInfo& info) {
    return Wrapper::NewInstance(info.Env(), info);
}

// js内でexport()が呼び出されたとき
Napi::Object InitAll(Napi::Env env, Napi::Object exports) {
    // 関数定義
    Napi::Object new_exports = Napi::Function::New(env, CreateObject);
    return Wrapper::Init(env, new_exports);
}

// jsへバインドするためのマクロ
// jsで、 export('bindings')('addon')と記述したとき、上記のInitAll()が呼び出される
NODE_API_MODULE(addon, InitAll)