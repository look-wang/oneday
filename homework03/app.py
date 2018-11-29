from flask import Flask, render_template, request, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/student?charset=utf8'

db = SQLAlchemy(app)
class stu(db.Model):
    s_id = db.Column(db.Integer,primary_key=True)
    s_name = db.Column(db.String(40))
    s_cla = db.Column(db.String(40))
    s_stuid = db.Column(db.String(40))
    s_phone = db.Column(db.Integer)

    def __init__(self,s_name, s_cla, s_stuid, s_phone):
        self.s_name = s_name
        self.s_cla = s_cla
        self.s_stuid = s_stuid
        self.s_phone = s_phone

@app.route('/')
def hello_world():
    return render_template('home.html', res='')

# TODO:添加信息
@app.route('/add_info',methods=['POST'])
def add_info():
    s_name = request.form['name']
    s_cla = request.form['cla']
    s_stuid = request.form['stu_id']
    s_phone = int(request.form['phone'])

    data = stu(s_name,s_cla,s_stuid,s_phone)
    db.session.add(data)
    db.session.commit()
    # return redirect(url_for('show_info'))

    all_datas = stu.query.all()
    res = []
    for data in all_datas:
        dicts = {
            'name': data.s_name,
            'cla': data.s_cla,
            'stuid': data.s_stuid,
            'phone': data.s_phone
        }
        res.append(dicts)
    return render_template('home.html', res=res)

if __name__ == '__main__':
    app.run()
