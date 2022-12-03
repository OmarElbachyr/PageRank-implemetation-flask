from flask import Flask, request, render_template, url_for
from flask_cors import CORS, cross_origin
import pandas as pd
import os
import xml.dom.minidom
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

            return render_template('./result.html', ranks=ranks, scores=result, zip=zip, header='Result')

        elif method == 'adjacency-matrix':
            file = request.files['graph_am']
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'adjacency-matrix.xlsx'))
            print('File Saved!')
            df_A = pd.read_excel('./static/files/adjacency-matrix.xlsx', header=None)
            A = df_A.to_numpy()
            result = PageRank_obg.PageRank_adjacency_matrix(A)
            ranks = [*range(1, result.shape[0] + 1)]

            return render_template('./result.html', ranks=ranks, scores=result, zip=zip, header='Result')

        elif method == 'graphMl':
            file = request.files['graphMl']
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'graphMl.xml'))
            print('File Saved!')
            graph = xml.dom.minidom.parse("./static/files/graphMl.xml")

            result = PageRank_obg.PageRank_graphMl(graph)
            ranks = [*range(1, result.shape[0] + 1)]

            return render_template('./result.html', ranks=ranks, scores=result, zip=zip, header='Result')

        elif method == 'networkx':
            sources = list()
            values = request.values
            print(values)
            # for i in len(values):
            #     values[f'sources-{i}']
            result = PageRank_obg.PageRank_networkx(values)
            return str(result)

@app.route('/draw-graph', methods=['GET'])
def draw_graph():
    return render_template('./graph.html')



if __name__ == '__main__':
    app.run(debug=True)
