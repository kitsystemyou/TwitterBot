# カモメbot
カモメbot (旧:tbot.py 新:seagull.py)

## 1. 概要
リプライを送るとカモメのような鳴き声が返ってくるtwitterbotです。毎回多様な返事をしますが会話能力はありません。

## 2. 仕様
アカウント@kit_systemyou　宛に"カモメbot"の文字列を含むリプライを送ることで返事が返ってきます。
また、 **"カモメbot"** を含む、かつ **"群れ"** を含むリプライを送ると群れた返事が返ってきます。
さらに **"カモメbot"** を含む、かつ **"時間"** または **"タイム"** または **"time"** を含むリプライを送ると
鳴き声と共に時間を教えてくれます。

## 3. 仕様言語等
プログラムの動作確認をした環境
OS:Windows 10 Pro 64bit(1803)
言語:Python3.6.5(Anaconda4.5.11)
ライブラリ:tweepy3.7.0
標準ライブラリ:yaml, datetime, random, time

※必須ファイル：
このプログラムを動かすにはTwitterAPIの認証キーを記述した"api_key.yml"が必要です。

## 4. Twitter APIとリプライ取得
このプログラムはTwitterAPIのmentions_timelineを用いてリプライを取得しています。
また、取得時の最新リプライのidを保存することで、次回取得時には反応済みでないリプライだけ取得しています。
(Account Activity APIとWebhookを使うともっとスマートにできると思います。）

## 5. 参考

tweepyの扱い
https://github.com/Marsan-Ma/twitter_scraper

mentions_timeline
https://sites.google.com/site/cloverplusrose/twitter-mentionwo-dumeruyouninarumade

Cursol(tweepy)
https://tweepy.readthedocs.io/en/3.7.0/cursor_tutorial.html

リプライ送信時の注意(in_reply_to_status_idはデフォルトだと自分以外無視される)
https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update

API制限について
https://developer.twitter.com/en/docs/basics/rate-limits.html
