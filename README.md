# カモメbot
カモメbot (旧、新)

1. 概要

  リプライを送るとカモメのような鳴き声が返ってくるtwitterbotです。毎回多様な返事をしますが会話能力はありません。

2. 仕様

  アカウント@kit_systemyou　宛に"カモメbot"の文字列を含むリプライを送ることで返事が返ってきます。
また、 **"カモメbot"** を含む、かつ **"群れ"** を含むリプライを送ると群れた返事が返ってきます。
さらに **"カモメbot"** を含む、かつ **"時間"** または **"タイム"** または **"time"** を含むリプライを送ると
鳴き声と共に時間を教えてくれます。

3. 仕様言語等

  プログラムの動作確認をした環境
OS:Windows 10 Pro 64bit(1803)
言語:Python3.6.5(Anaconda4.5.11)
ライブラリ:tweepy3.7.0
標準ライブラリ:yaml, datetime, random, time

※必須ファイル
このプログラムを動かすにはTwitterAPIの認証キーを記述した"api_key.yml"が必要です。
