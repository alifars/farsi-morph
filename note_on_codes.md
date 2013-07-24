````
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
````
## 全体的に
`stem = stem.strip().decode('utf-8').strip(u'\u200c').encode('utf-8')`  
tokenの前後に存在するZWNJを削除するためだけにこのような処理をしているっぽい

`stem = re.sub(' ','\xe2\x80\x8c',stem)`  
`stem = re.sub('\#','\xe2\x80\x8c',stem)`
次のような場合に対応するためと思われる．
`نمی<U+200C>توا`
でも，わざわざZWNJでつながっているものをスペースに変換して意味はあるのだろうか？わからないが，これのおかげで，変な文字列が生成されていることだけは間違いない．
当たり前だが，tokenの中に#が入るケースは存在しなかった．

まずこの方針は色々と気に入らない．  
* スペースは見にくいので，明示的な記号で形態素区切りを表示したい
* unicodeで扱わないのが気に食わない．

この２つを修正する．

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

## infer_morph.py

コードの中でA.txt,B.txt,C.txtを読んでいるので，少なくともこの３つは必要とする．

`if pos == 'v' and '#' in list(lemma):`posが動詞かつ，lemmaの行に#が存在するときのif 
\#はstemの前についている記号．例えば動詞のmy_twnmなら，twnと記述されている．
list(lemma)により，文字が１文字ずつリストに格納されて，#があるかどうか？を簡単に走査できる．  
````
					stem = re.sub(' ','\xe2\x80\x8c',stem)
					dummy = token.replace(stem,'_')
````
により，tokenに中にstemがあった場合には，stemを_に置き換えてしまう．
````
				if "_" in list(dummy):
					affixes.add(dummy)
````
により，dummyの中に_がある（つまりstemが置き換えられた形）時にstem以外の部分をaffix集合に追加する．

一方`if pos == 'v' and '#' in list(lemma):`が偽だった場合，
````
			else:
				#Check lemma against token
				dummy = token.replace(lemma,"_")
				if "_" in list(dummy):
					affixes.add(dummy)
````
が実行される．つまりlemmaそのままの形をstemと思ってtoken中で_におきかえてしまう．

その後，prefixとsuffixの切り出しを行う．
````
	for item in affixes:
		if len(item.split('_')) > 2:
			other.add(item)
			continue
		prefix = item.split('_')[0]
		prefix = prefix.strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		if (not prefix.isspace()) and (prefix != ''):
			prefixes.add(prefix)
		suffix = item.split('_')[-1]
		suffix = suffix.strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		if (not suffix.isspace()) and (suffix != ''):
			suffixes.add(suffix)
````

以上より，このスクリプトはPersian Dep. Treebankの行構成と#によるstem表現を利用して，入力のTreebankの中にある語からprefixとsuffixを切り出すためのスクリプトと判断できる．
尚，特にファイルに書き出しをしているわけではないので，他に使うでもなく，ただの確認用のスクリプトか？

ただ，~/src/lexica以下のファイルを見ると，
````
LEXICON VPrefix
!Negation
+Neg:نه^ V;
+Neg:نا^ V;
!Durative
+Dur+Neg:نهمی~ V; !Form with ZWNJ
+Dur:می~ V; !Form with ZWNJ
!Subjunctive/Imperative
+Subj/Imp:به^ V;
````
のような記述がされていて，このスクリプトの出力とかなり似ていることが確認できる．つまり，このスクリプトの存在意義は
### Dep. Treebankからprefixとsuffixを切り出して，lexファイルに追加するため．
と考えられる．
### またlexへの追加は，手作業でコピペした．と思われる．


## fill_in.py

`"Usage: python fill_in.py corpus.token corpus.results"`から少なくとも形態素解析結果に使うコードだと判断できる．  
````
	hyp_raw = open(args[2]).readlines()
	hyp = [] # list of lists, hypotheses for each token
	buff = [] # buffer list for current hypothesis
	for line in hyp_raw:
		if line.isspace():
			#New lemma, append hypotheses for last lemma to hyp list
			hyp.append(buff)
			buff = [] # restart buffer
		else:
			#New hypothesis for current lemma
			buff.append(line)
````
hyp_rawが形態素解析結果の行．この行にスペースが含まれていれば，hypにbuffを追加して，buffを初期化．つまり，空白行のみから空白行まで，がひとつの固まりとして記録されているものと思われる．  

その後，以下の条件分岐をしている．
````
	for item in hyp:
		if item == ['+?\n']:
			out.append(tokens[i].strip()+"+Guess\n")
		else:
			out.append(item)
		i+=1
````
`+?`は正規表現ではなかろうから，きっとfomaの出力かと思う．ご丁寧に`"+Guess\n"`ってついているし．

最後にoutの内容を書き出しているんだけど，ちょっと謎な内容がひとつある．
````
	for item in out:
		if type(item) is str:
			f.write(item)
		else:
			for next in item:
				f.write(next)
````
このnextは予約語？にしてもitemがstrでない場合ってどんな場合？

````
-------src
	|
	|-farsi.foma
````


## farsi_foma

transducerの設定図とも言える部分．
Handoutはwebで公開されている．[hadout](http://foma.sourceforge.net/lrec2010/lrec2010handout.pdf) 
基本的な使い方は[turtorial](https://code.google.com/p/foma/wiki/GettingStarted)
このページが[形態素解析器のチュートリアル](https://code.google.com/p/foma/wiki/MorphologicalAnalysisTutorial) 

foma interfaceというものがあり，ここでいくつかのコマンドを実行する．
`words` または `print words`で，受理可能な単語を表示（ただし，自己サイクルがある場合は表示しない）
`foma[1]: view`でグラフを図示してくれる（Xがないと動作しない）
`down`または`up`でテストモード（？）に移行．Contr+Dでinterfaceに戻る．



### 基本的には正規表現でエッジを表現できるみたい．  
いくつか特殊な点があり，  
* any characterを示す.は?で表現
* 0が空のイプシロンを表す


### ネットワーク間の接続に関して  
ネットワーク１　.o.　　ネットワーク２ってすれば２つのネットワークの接続ができるようだ．
