----scripts
	|
	|-print_lemmas.py
	|-norm_farsi.py
	|-setup_eval.py
	|-random_split_3sets.py
	|-evaluate.py
	|-fill_in.py
	|-infer_morph.py
	|-analyze.sh
	|-add_lemmas_from_corpus.sh

## norm_farsi.py

`Usage: python norm_farsi.py input_filename`

対象のコーパスの正規化を行う．ここで言う正規化とは，diacriticsマークの削除とalf,heh,yeに関する正規化．  

alfについて：Arabic_alf_hamza_aboveをArabic_alfにする．Arabic_alf_hamza_belowをArabic_alfにする．Arabic_alf_madda_aboveをArabic_alfにする．  

hehについて：heh_hamza_aboveをhehに統一

yeについて：Arabic_yeをPersian_yeに統一


##random_split_3sets.py

`Usage: python random_split_3sets.py farsi_tokens.txt A_fraction B_fraction`

対象のコーパス（ここではPersian Dependency Treebank）を３分割する．Aの割合とBの割合を選択することができ，あまった部分はCとして出力する．

## print_lemmas.py

`Usage: python print_lemmas.py corpus.txt part-of-speech >> part-of-speech.lexc`
入力はコーパス単位．おそらくrandom_split_3sets.pyで分割したものを入力としているはず．part-of-speechは自分の好きなように指定できる．詳しくはprint_lemmas.pyを参照．  
````
		lis = line.strip().split('\t')
		#Strip token edges of whitespace and ZWNJ
		token = lis[0].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
```
タブで区切って，０番目（lemma）のみを出力とする．ただ，またもZWNJをwhite spaceに置き換えしていて，謎が多い．

````
		if check_pos == pos:
			#Check if POS is verb
			if pos != 'v':
````
指定したPOSがvでなければ通常の出力，vであれば複合動詞（#が含まれる）とsimple verb(#なし)に区別している．
````
		else:
				#Check for #-character in verb lemma
				if '#' in list(lemma):
				（略）
				else:
					lemmas.add(lemma)
````
最後に次の形式でファイルに書き出し`print lemma+'\t'+check_pos.capitalize()+'Inf;'`

## add_lemmas_from_corpus.sh
print_lemmas.pyを複数のPOSに対して実行できるようにしたシェルスクリプト．

## analyze.sh
これがfomaの実行そのもの？ 

## fill_in.py

まだ読んでいるところ

## infer_morph.py

まだ読んでいるところ

##setup_eval.py  

評価の準備を行う．
`Usage: python setup_eval.py corpus.txt`  

`lis = line.strip().split('\t')`  
対象コーパスに合わせて，タブで区切っている．

````
		token = lis[0].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		#Substitute ZWNJ for space or #-character internally in token
		token = re.sub(' ','\xe2\x80\x8c',token)
		token = re.sub('\#','\xe2\x80\x8c',token)
````
この辺りの挙動は謎が多い．初めの行でZWNJを消しているはずなのに，その後に置換を行ったり，#で置き換えたりと，意図が見えない．

````
		lemma = lis[1].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		#Substitute ZWNJ for space internally in lemma
		lemma = re.sub(' ','\xe2\x80\x8c',lemma)
		#Don't use empty lemmas
````
lemmaからも同様にZWNJをwhite spaceに置き換えている．この部分は書き換えた方が良さそう．

`f = open(args[1][:-4]+'.token','w')`と`f = open(args[1][:-4]+'.lemma','w')`でファイルに書き出している．


## evaluate.py

`Usage: python evaluate.py corpus.lemma corpus.results`

このスクリプトがやっていること．
１：形態素解析のgold data，つまりcorpus.lemmaを読み込んで，形態素解析の結果，つまりcorpus.resultsと比較．
２：比較した結果を元にprecisionとrecallを計算

lemmaについて動詞の時，かつ＃マークがある時とそうでない時で処理を分けている．#マークがつくのはたしか動詞の語根に対して（？不明確なので，要チェック）

