from flask import Flask

app = Flask(__name__)

@app.route('/templates')
def dynamic_default(value):
    print(f'型{type(value)}, 値：{value}')
    return (f'<h1>渡された値は「{value}」です</h1>')

@app.route('/templates2/<int:number>')
def dynamic_converter(number):
    print(f'<h1>型：{type(number)}, 値：{number}</h1>')
    
    if __name__ == '__main__':
        app.run()