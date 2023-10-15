from flask import Flask, render_template, request,jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

def connect_MongoDB():
    client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
    db = client["college"]  # Replace with your database name
    return db

@app.route('/<value>')
def wellcome_msg(value):
    return "hello "+str(value.capitalize())

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/home', methods=['POST'])
def home_post():
    db = connect_MongoDB()
    user_data = db["stud"]  # Replace with your collection name
    Name = request.form['Name']
    Age = request.form['Age']
    Dept = request.form["Dept"]
    City = request.form["City"]
    user_data.insert_one({"Name":Name,"Age":Age,"Dept":Dept,"City":City})    
    return render_template("admission.html")


@app.route('/admission')
def add_data():
    return render_template("admission.html")

@app.route('/showdata',methods =['GET'])
def show_data():
        db = connect_MongoDB()
        collection = db['stud']
        user_data = list(collection.find())
        for data in user_data:
            data["_id"] = str(data["_id"])
        return render_template("show.html",data = user_data)

@app.route('/aboutus')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)