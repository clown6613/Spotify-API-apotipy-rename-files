# Spotify-API-apotipy-rename-files
SpotifyのAPI（spotipy）をててファイルを、検索ファイルを基にリネームする。

# 使用技術
* Python3
* SpotifyAPI(spotipy)

# やったこと
不規則な楽曲ファイルのファイル名をSpotifyの検索機能を使って、該当するものに変更する。

# APIを使用した部分
APIを使った肝となる検索をかけるコード部分は以下のようなものである。

```results = sp.search(q=input("検索word->入力："), limit=30)```
