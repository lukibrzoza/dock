from flask import Flask, render_template, request, redirect, url_for


COUNTS = {'GET':0, 'POST':0, 'PUT':0, 'DELETE':0}


app = Flask(__name__, static_url_path='/static')


@app.route("/")
@app.route("/request-counter", methods=['GET', 'POST'])
def main_page():
    global COUNTS
    if request.method == 'GET':
        COUNTS['GET'] += 1

    elif request.method == 'POST':
        COUNTS['POST'] += 1

    elif request.method == 'PUT':
        COUNTS['PUT'] += 1

    elif request.method == 'DELETE':
        COUNTS['DELETE'] += 1
    
    print(COUNTS)
    return render_template('page.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
