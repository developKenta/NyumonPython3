# P8 例1-3

#Pythonの辞書
#「quotes」は「辞書に名前を与える変数」である。
#辞書を調べるような感じ。ここでは「hirano」と入力すれば「hello」が出力される。
#配列の番号が文字列に変わっただけだと思う。

quotes = {
    "hirano": "hello",
    "kenta": "ohayou",
    "mac": "bye",
}
stooge = "mac"
print(quotes[stooge])