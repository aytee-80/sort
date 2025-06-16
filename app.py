from flask import Flask, request, jsonify,render_template
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/reverse', methods=['POST'])
def sort_word():
    data = request.get_json()
    word = data.get('word', '').lower() 
    
    order = list(word)
    order.sort()
    sorted_word = ''.join(order)
    return jsonify({'sorted_word': sorted_word})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')