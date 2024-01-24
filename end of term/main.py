from flask import *
import CRUD as crud
import selectonweb as select

app = Flask(__name__)


@app.route('/index')
def star_page():
    return render_template('index.html')


@app.route("/select_position", methods=["POST"])
def select_position():
    data = request.form['position_id']
    result = jsonify(crud.select_position(data))
    return result

@app.route("/doinsert", methods=["POST"])
def doinsert():
    name = request.form['name']
    gender = request.form['gender']
    age = request.form['age']
    position_id = request.form['position_id']
    nation = request.form['nation']
    county = request.form['county']
    township = request.form['township']
    

    data = (name,gender,age,position_id,nation,county,township)
    
    return jsonify(crud.insert_user(data))
@app.route("/dodelete", methods=["POST"])
def dodelete():
    id = request.form['id']
    
    data = (id)

    return jsonify(crud.delete_user(data))

@app.route("/doupdate", methods=["POST"])
def doupdate():
    
    name = request.form['name']
    gender = request.form['gender']
    position_id = request.form['position_id']
    age = request.form['age']
    nation = request.form['nation']
    county = request.form['county']
    township = request.form['township']
    id = request.form['id']
    
    data =(id,name,gender,position_id,age,nation,county,township,id)

    return jsonify(crud.update_user(data))

@app.route("/select_id", methods=["POST"])
def select_id():    
    id = request.form['id']
    data = (id)
    result = jsonify(crud.select_id(data))
    return result


if __name__ == '__main__':
    app.run(debug=True)
