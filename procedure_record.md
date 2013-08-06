### あらかじめ，ローマ字化スクリプトでローマ字にしておく

### norm_farsi.pyで一応，正規化（笑）しておく

### まずはcorpusを３つに分割する
`python random_split_3sets.py hoge 0.4 0.5`  
結果は  
````
#Tokens in original file: 423136
#Tokens in A set: 169254
#Tokens in B set: 211568
#Tokens in C set: 42314
````
### ../data に作成したファイルを移動

### foma用のlexiconの作成
`sh add_lemmas_from_corpus.sh A`

### .tokenとlemmaを作成して評価の準備
`python setup_eval.py {A,B,C}.txt`  

### Cを対象にしてanalyze.shを実行
`sh analyze.sh C`  

このままではlexファイルの定義がされていなかったので，意味がなかった．やり直し．
自分でlexファイルを作成するのでなく，既存のlexファイルに対してローマ字化スクリプトを実行してみる． 

### 再度，analyze.shを実行

結果，fomaからのメッセージにエラーはなし．  
result/以下にファイルが生成される．中身は`6+N+Sg`の様な記述がたくさん並ぶ．  
これの意味は？次に何をしたらよい？

### evaluate.pyによる評価
他にできることもないようなので，evaluate.pyによって評価を行う．  
````
Precision=0.000167188134419
7 correct lemmas out of 41869 total analysis hypotheses
Recall=0.000175013125984
7 correct lemmas out of 39997 total lemmas
F-Score=0.000171011164586
````
かなり低い....  
怪しいので，もう一度，もとの構成で再実験

元の構成でもとてつもなく低い精度．．．何か間違っているんだろうか．．．

原因を発見．直接の原因は，.tokenと.lemmaが正しく生成できていなかったこと．これはsetup_eval.pyでindexがずれていたのが原因．
正しく直した結果は以下のとおり（アラビア文字で評価を行った結果）
````
Corpus A
Precision=0.749272527787
172777 correct lemmas out of 230593 total analysis hypotheses
Recall=0.638665868228
172777 correct lemmas out of 270528 total lemmas
F-Score=0.689562001992
````  

以下がローマ字化にして行った結果．若干低いのは，ローマ字化でミスがあったから．
````
Corpus A
Precision=0.745260314999
167223 correct lemmas out of 224382 total analysis hypotheses
Recall=0.618352789785
167223 correct lemmas out of 270433 total lemmas
F-Score=0.675901094348
````
