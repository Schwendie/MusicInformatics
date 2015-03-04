# Goal
The end product is a playlist that will choose what to play based on keywords present in any given Tweet that can be pulled from Twitter, whether that keyword be the name of an artist, a snippet of lyrics, or potentially a mood that corresponds to the feel of the song.

# artist_player

**Purpose**

This artist_player should explore the ways one can play music by supplying Echonest with an artist's name.

**Description**

This program uses the module [Spotipy] to search an artist and gain access to html links of thirty-second mp3s of their top tracks.  The program uses the [urllib2] module to open these html links and write them to a temporary file.  That file is then read using a class created by Luke Stack, the [aqplayer.py].  The entirety of the thiry-second mp3 is played, then the program jumps to the next track.

**Dependencies**

artist_player requires the following modules:

  - spotipy
  - remix
  - urllib2
  - pyaudio

# Code Explaination
Create a variable with the artist's name
```python
import spotipy
import echonest.remix.audio as audio
import urllib2
from aqplayer import Player

name = 'Simon & Garfunkel'
```
then use Spotipy to search for the artist.
```python
spotipy = spotipy.Spotipy()
results = spotipy.search(q='artist:' + name, type='artist')
```
Retrieve the artist's unique key and store their top tracks into a list.
```python
uri = results['artists']['items'][0][u'uri']
results = spotipy.artist_top_tracks(uri)
```
Now, all that's left is to iterate through the tracks in the list, open a temp file and write the mp3 supplied by spotipy to that file, and pass that file to Luke's program.
```python
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
```

[Spotipy]: http://spotipy.readthedocs.org/en/latest/
[urllib2]: https://docs.python.org/2/library/urllib2.html#module-urllib2
[aqplayer.py]: https://github.com/jlstack/PythonEchonestRemix/tree/master/aqplayer
