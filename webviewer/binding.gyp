{
  "targets": [
    {
      # ↓addon.cc内の NODE_API_MODULE(addon, InitAll) と同名にする
      "target_name": "addon",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      # ↓必要な.ccファイルを全て記述する
      # ワイルドカードを使って、native_cpp内のファイルを全て読み込む
      "sources": [ "./addon/addon.cc", "./addon/wrapper.cc",
                   "<!@(node -p \"require('fs').readdirSync('./addon/native_cpp').map(f=>'addon/native_cpp/'+f).join(' ')\")"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      "defines": [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    }
  ]
}

