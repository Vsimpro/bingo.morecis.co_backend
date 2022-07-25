# Vsim 7/7/22
# bingo.morecis.co backend API -- provides  .json from Maria.
# I've used tabs, don't use spaces or it'll not run.
import json, random, mysql.connector
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder="")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# Credentials to database
conn = mysql.connector.connect(
user = "",
password = "",
host = "localhost",
port=3306,
database="bingo"
)

# Global variables
cursor = conn.cursor()
items = list()
default_json = {"status":  "offline"}

def get_data():
	query = "SELECT item FROM Items;"
	cursor.execute(query)
	data = cursor.fetchall()
	for item in data:
		items.append(item[0])

# TODO: readme file for the API
@app.route("/",  methods=['GET'])
def index(): return render_template("index.html")

# expand here if needed!
@app.route("/<file>",  methods=['GET'])
def a_file(file): return default_json

# version 1
# TODO: v1 documentations
@app.route("/v1/",  methods=['GET'])
def v1(): return default_json

@app.route("/v1/<file>",  methods=['GET'])
def v1_file(file): return default_json

# bingo API
# TODO: bingo documentations
@app.route("/v1/bingo/",  methods=['GET'])
def bingo_file(): return default_json

@app.route("/v1/bingo/items",  methods=['GET'])
def bingo_index():
	default_json = {"status":  "offline"}
	list_of_items = list()

	if len(items) == 0: get_data()

	if len(items) != 0:
		for integer in random.sample(range(0,len(items)),25):
			list_of_items.append(items[integer])

		print(list_of_items)
		default_json =  {"pool" : list_of_items}
	return jsonify(default_json)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8123)
