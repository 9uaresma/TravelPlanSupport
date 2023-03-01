# **旅行計画を補助するアプリ**

## **デスクトップ版**
---------------------------
### 機能一覧
* 出発時刻と到着時刻を入力してEnterを押すと、時刻表に帯を表示する
* Removeボタンを押すと、帯が消える。



## **ブラウザ版**
---------------------------

### 概要  
ブラウザで動作する機能追加中．  
nodejsからc++のクラスを呼び出す構造

ビューワー: webviewer  
nodejsで作成

処理系: cpp  
c++ で作成

### 使い方
Input your plan の所に，Plan名 と，所要時間を記入して，Addをクリック  
すると，Planと所要時間の一覧が画面に表示される．  
トータル時間が一番下に表示される


![AboutWebViewer](docs\images\webviewer_image.PNG "image")


### ビルド手順

あらかじめ，c++のコンパイラをインストールしておく．

```
#! bash

cd travelplansupport/cpp/build
make

```


### Nodejsでc++クラスを利用する方法
参考：
https://qiita.com/Akihiro_Nakayama/items/dc31f9ae9519602f9f50

addon/native_cpp/classA.cpp に定義したクラスを，wrapper.cppやaddon.cc を使って
nodejsに引き渡している．
classA.cppの関数を増やしたら，他の関数を真似つつwrapperやaddonを編集し，以下を実行．

```
#! bash

cd travelplansupport/webviewer
npm install .

```

<!--

<<Markdown記法に関する自分用メモ>> 
Readme.md をvscode上で編集
    Ctl + 「K」 -> 「V」で，サイドパレットにプレビュー表示できる

Markdown チートシート
    https://gist.github.com/mignonstyle/083c9e1651d7734f84c99b8cf49d57fa

-->
