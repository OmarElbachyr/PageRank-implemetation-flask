from flask import Flask, request, render_template, url_for
from flask_cors import CORS, cross_origin
import pandas as pd
import os
from static.py.PageRank import PageRank

UPLOAD_FOLDER = './static/files'

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
@app.route('/home')
def hello_world():
    return render_template('./index.html')


@app.route('/PageRank/<string:method>', methods=['POST'])
@cross_origin()
def page_rank(method):  # put application's code here
    if request.method == 'POST':
        PageRank_obg = PageRank()

        if method == 'transition-probability-matrix':
            file = request.files['graph_tp']
            # print(f'type {file}')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'transition-probability-matrix.xlsx'))
            print('File Saved!')
            df_TP = pd.read_excel('./static/files/transition-probability-matrix.xlsx', header=None)
            TP = df_TP.to_numpy()
            result = PageRank_obg.PageRank_TP(TP)
            # print(f'type: {type(result)}')

            ranks = [*range(1, result.shape[0] + 1)]

            return render_template('./result.html', ranks=ranks, scores=result, zip=zip)

        elif method == 'adjacency-matrix':
            file = request.files['graph_am']
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'adjacency-matrix.xlsx'))
            print('File Saved!')
            df_A = pd.read_excel('./static/files/adjacency-matrix.xlsx', header=None)
            A = df_A.to_numpy()
            result = PageRank_obg.PageRank_adjacency_matrix(A)

            return str(result)

    # return render_template('./index.html')


if __name__ == '__main__':
    app.run(debug=True)
