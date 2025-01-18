import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient

#def create_app():
app = Flask(__name__)
client = MongoClient("mongodb+srv://naviddavoudi80:Cmogtf04MWKcEKLQ@microblogdb.hjdx5.mongodb.net/")
app.db = client.micro_blog

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.now().strftime("%y-%m-%d")
        app.db.entries.insert_one({ "content" : entry_content, "date" : formatted_date })
    entries_with_date = [
        (
            entry["content"],
            entry["date"],
            datetime.datetime.strptime(entry["date"], "%y-%m-%d").strftime("%b %d")
        ) 
        for entry in app.db.entries.find({})
    ]
    return render_template("home.html", entries=entries_with_date)
#return app
