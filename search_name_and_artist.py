import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="ddc88c09165e4cd5949fbba22287d522",
                                                           client_secret="977d633b95144b3ebd2ed6406ce36bdc"))

class Search:

  def music_artist_name(self):
    music_l=list()
    results = sp.search(q=input("検索word->入力："), limit=30)
    for idx, track in enumerate(results['tracks']['items']):
      print(idx, track['name']+"／"+track['album']['artists'][0]['name'])
      
      music_l.append(track['name']+"／"+track['album']['artists'][0]['name'])

    rename_m=music_l[int(input("対応するインデックス番号を入力："))]
    print(rename_m)
    return rename_m  

m_dir=r"C:\Users\kota713\Music\mp3"
save_dir=r"C:\Users\kota713\Music\rename_mp3"
musics=os.listdir(m_dir)

#print(musics)

for music in musics:
  print(music)
  s=Search()
  rename_m=s.music_artist_name()
  

  os.rename(os.path.join(m_dir,music),os.path.join(save_dir,rename_m)+".mp3")