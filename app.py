from flask import Flask
import pymysql

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '이 메시지가 나온다면 플라스크 성공!'
    
@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'
if __name__ == '__main__':
    app.run(debug=True)


# conn = pymysql.connect(
#     host='127.0.0.1',
#     user='root',
#     password='TheoHernandez19!',
#     port=3306,
#     db='aitrading_db',
#     charset='utf-8'
# )

# cur = conn.cursor()