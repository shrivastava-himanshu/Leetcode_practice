import sqlite3, flask

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/v1/resources/books/all', methods=['GET'])
def books_show():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()

    return jsonify(all_books)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404




@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_param = request.args

    id = query_param.get('id')
    published = query_param.get('published')
    author = query_param.get('author')

    query = "Select * from books where"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    #if 'id' in request.args:
    #    id = int(request.args['id'])
    #else:
    #    return "Error: No id field provided. Please specify an id."

    #results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results

    #for book in books:
    #    if book['id'] == id:
    #        results.append(book)

    #return jsonify(results)





app.run()