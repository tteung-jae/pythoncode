from flask import Flask,request, render_template, redirect
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usersform', methods=['GET', 'POST'])
def usersform():
    if request.method == 'GET':
        return render_template('usersform.html')
    else:
        userid = request.form.get('userid')
        userpw = request.form.get('userpw')
        username = request.form.get('username')
        userage = request.form.get('userage')
        useremail = request.form.get('useremail')
        useradd = request.form.get('useradd')
        usergender= request.form.get('usergender')
        usertel = request.form.get('usertel')
    
        try:
            connection = pymysql.connect(host = 'localhost',
                                    user = 'root',
                                    password = 'qwer1234',
                                    db = 'test',
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor)

            with connection.cursor() as cursor:
                sql='''
                    insert into users values(%s,%s,%s,%s,%s,%s,%s,%s)
                '''
                data = (userid, userpw, username, userage, useremail, useradd, usergender, usertel)
                # print(data)
                cursor.execute(sql,data)
                connection.commit()

        finally:
            connection.close()

    return redirect('/list')

@app.route('/list')
def list():
    connection = pymysql.connect(host = 'localhost',
                                    user = 'root',
                                    password = 'qwer1234',
                                    db = 'test',
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "select * from users;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()
    return render_template('list.html', list = result)

# @app.route('/form')
# def formTest():
#     return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)