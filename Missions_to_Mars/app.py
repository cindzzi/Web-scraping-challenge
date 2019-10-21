from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask (__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_scrape_app"
mongo = PyMongo(app)



@app.route("/")
def index():
    mars_dict = mongo.db.mars_dict.find_one()
    return render_template("index.html", mars = mars_dict)

@app.route("/scrape")
def scraper():
   # mars_dict = mongo.db.mars_dict

    mars_dict = scrape_mars.scrape()

    #mars_dict.update({}, mars_dict, upsert = True)
    mongo.db.update({}, mars_dict, upsert = True)

    return redirect("/")    


if __name__ == "__main__":
    app.run(debug=True)
