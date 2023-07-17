from flask import Flask,render_template,url_for,redirect,request,flash
from flask_mysqldb import MySQL

app=Flask(__name__)
#MYSQL CONNECTION
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="Jagan@101102"
app.config["MYSQL_DB"]="libdb"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)


#Loading Home Page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="SELECT * FROM bookshop"
    con.execute(sql)
    res=con.fetchall()
    return render_template("home.html",datas=res)
    
#New User
@app.route("/addUsers",methods=['GET','POST'])
def addUsers():
    if request.method=='POST':
        bookname=request.form['bookname']
        username=request.form['username']
        author=request.form['author']
        con=mysql.connection.cursor()
        sql="insert into bookshop(BOOKNAME,USERNAME,AUTHOR) value (%s,%s,%s)"
        con.execute(sql,[bookname,username,author])
        mysql.connection.commit()
        con.close()
        flash('User Details Added')        
        return redirect(url_for("home"))
    return render_template("addUsers.html")
#update User
@app.route("/editUser/<string:bookid>",methods=['GET','POST'])

def editUser(bookid):
    con=mysql.connection.cursor()
    if request.method=='POST':
        bookname=request.form['bookname']
        username=request.form['username']
        author=request.form['author']
        sql="update bookshop set BOOKNAME=%s,USERNAME=%s,AUTHOR=%s where BOOKID=%s"
        con.execute(sql,[bookname,username,author,bookid])
        mysql.connection.commit()
        con.close()
        flash('User Detail Updated')
        return redirect(url_for("home"))
        con=mysql.connection.cursor()
        
    sql="select * from bookshop where BOOKID=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("editUser.html",datas=res)
#Delete User
@app.route("/deleteUsername/<string:bookid>",methods=['GET','POST'])
def deleteUser(bookid):
    con=mysql.connection.cursor()
    sql="delete from bookshop where BOOKID=%s"
    con.execute(sql,bookid)
    mysql.connection.commit()
    con.close()
    flash('User Details Deleted')
    return redirect(url_for("home"))

if(__name__=='__main__'):
    app.secret_key="abc123"
    app.run(debug=True)
