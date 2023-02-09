from factory_method import ObjectSerializer

class Song:
    def __init__(self, song_id, title, artist) -> None:
        self.song_id = song_id
        self.title = title
        self.artist = artist
    
    def serialize(self, serializer):
        serializer.start_object('song', self.song_id)
        serializer.add_property('title', self.title)
        serializer.add_property('artist', self.artist)

if __name__ == '__main__':
    song = Song('1', 'Water of Love', 'Dire Straits')
    serializer = ObjectSerializer()
    print(serializer.serialize(song, 'JSON'))
    print(serializer.serialize(song, 'XML'))
    print(serializer.serialize(song, 'YAML'))