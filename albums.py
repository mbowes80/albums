from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Read JSON data from a file
with open('albums.json', 'r') as json_file:
    albums_data = json.load(json_file)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# Extract unique tags and genres
all_tags = set()
all_genres = set()

for album in albums_data["favoriteAlbums"]:
    all_tags.update(album["tags"])
    all_genres.update(album["genres"])

all_tags=list(all_tags)
all_tags.sort()
all_genres=list(all_genres)
all_genres.sort()
#all_tags=all_tags.sort()
#print(all_tags)
#print(all_genres)



@app.route('/albums')
def show_albums():
    tagParam = request.args.get('tag')
    genreParam = request.args.get('genre')
    return render_template('albums.html', albums=albums_data["favoriteAlbums"], all_tags=all_tags, all_genres=all_genres, tagParam=tagParam, genreParam=genreParam)

