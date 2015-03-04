import spotipy
import echonest.remix.audio as audio
from aqplayer import Player
import urllib2

name = 'Simon & Garfunkel'
spotipy = spotipy.Spotify()
results = spotipy.search(q='artist:' + name, type='artist')
uri = results['artists']['items'][0][u'uri']
results = spotipy.artist_top_tracks(uri)
for t in results['tracks'][:10]:
    url = t['preview_url']
    page = urllib2.urlopen(url)
    fname = 'tmp.mp3'
    file = open(fname, 'wb')
    file.write(page.read())
    file.close()
    audiofile = audio.LocalAudioFile(fname)
    player = Player(audiofile)
    bars = audiofile.analysis.bars
    print t['name']
    for bar in bars:
        player.play(bar, intro=True)
