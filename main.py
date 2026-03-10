from flask import Flask, render_template, request

import scholar

app = Flask(__name__, template_folder='templates')


@app.route('/')
def search():

    response = None

    query = request.args.get('query')
    if query:
        response = scholar.fetch_papers(query)

    venues = request.args.get('venues', default='ICSOC,EDOC,ICSA')

    return render_template('base.html', response=response, query=query, venues=venues)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
