from flask import Flask, render_template, redirect, url_for, session, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/index/')
def landing():
    ## 세션 정보 있으면 home로 이동, 없으면 landing page 출력
    if 'userID' in session:
        return redirect(url_for('home'))
    else:
        return render_template("index.html")

@app.route('/login/', methods=['GET', 'POST'])
def login():     
    ## 세션 정보 있으면 home로 이동
    if 'userID' in session:
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            ##로그인 정보 일치하는 지 확인
            ##1) 아이디 검색
            ##2) 아이디+비밀번호 검색
            ##1) 2) 결과 없으면 html 출력 시 parameter로 message 전달 ID_NOT_FOUND / PASSWORD_NOT_FOUND, header = 'login'
            ##2) 결과 있으면 세션 설정(하단 코드)
            session['userID'] = request.form['userID']
            return redirect(url_for('home'))
        else:
            header='login'
            return render_template("/login/login.html", status=header)

@app.route('/logout/')
def logout():
    session.pop('userID', None)
    return redirect(url_for('landing'))

@app.route('/join/')
def join():
    ## 세션 정보 있으면 home로 이동
    if 'userID' in session:
        return redirect(url_for('home'))
    else:
        header='login'
        return render_template("/login/join.html", status=header)    

@app.route('/')
def home():
    if 'userID' in session:
        header='logout'
        return render_template("/home/home.html", status=header)
    else:
        return redirect(url_for('landing'))


@app.route('/search/')
def search():
    if 'userID' in session:
        header='logout'
        return render_template("/search/search.html", status=header)
    else:
        return redirect(url_for('landing'))
    
@app.route('/bookInfo/')
def bookInfo():
    if 'userID' in session:
        header='logout'
        return render_template("/bookInfo/bookInfo.html", status=header)
    else:
        return redirect(url_for('landing'))
    

@app.route('/share/')
def share():
    if 'userID' in session:
        header='logout'
        return render_template("/share/share.html", status=header)
    else:
        return redirect(url_for('landing'))    

@app.route('/map/')
def map():
    return render_template("/bookInfo/map.html")

app.run(debug=True)