# mission-chan
ミッションちゃんの大冒険

## epub作成方法
**参考：** [画像ファイルをEPUB3/mobiにする(mkepub 1.4)](http://wakufactory.jp/densho/tools/mkepub.html)

1. 画像ファイル名をゼロパディングする．
```
% for i in $(ls -v); do mv $i $(printf '%03d.png' $(basename $i .png)); done
```
2. ナビゲーションは画像フォルダに `navi.txt` をTSV形式で保存する．
```
[表紙]  001.png
第1部   002.png
第2部   034.png
第3部   062.png
第4部   092.png
第5部   119.png
第6部   146.png
第7部   177.png
[奥付]  218.png
```
3. フォルダ名を変更し，著者・タイトルのメタデータを併せて保存する．
```
% ~/dev/mkepub/jpg2epub.sh '[OH MY GOD!! (模造クリスタル)] ミッションちゃんの大冒険'
```
