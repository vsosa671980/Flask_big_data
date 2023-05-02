from flask import Flask,render_template,redirect,request,url_for
import pandas as pd
import openpyxl
from database.query_db import Querie
from database.connection import Connection
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static')

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/",methods=["GET"])
def home():
    return redirect(url_for("show_products_all"))

"""Route for show alls products"""
@app.route("/products/",methods=["GET"])
def show_products_all():
    products = Querie.select_product_alls()
    return render_template("products.html",products = products)
"""Route update produc"""
@app.route("/products/update",methods=["POST"])
def update_product():
    id  = request.form  ['id']
    code =request.form["code"]
    description = request.form["description"]
    price = request.form["price"]
    Querie.update_product(id,code, description, price)
    return redirect(url_for("show_products_all"))
"""Route for acces to insert view templates or """
@app.route('/insertfile/',methods=["GET","POST"])
def insertFile():
    is_saving = False
    if request.method == 'GET':
        return  render_template("insertFile.html")
    else:
       redirect(url_for("show_products_all",is_saving=is_saving))
       is_saving = True
       file =request.files['file']
       df = pd.read_excel(file) 
       for indice,fila in df.iterrows():
           codigo = fila['Codigo']
           descripcion  = fila['Descripcion']
           precio = fila['importe']
           print(f'codigo = {codigo}')
           Querie.insert_product(codigo,descripcion,precio)
    is_saving = False
    return redirect(url_for("show_products_all"))
"""Delete a product"""
@app.route('/products/delete/<product_id>',methods=["GET"])
def delete_product(product_id):
    Querie.delete_products(product_id)
    products = Querie.select_product_alls()
    return render_template("products.html",products = products)
"""Find products by id"""
@app.route('/products/<product_id>',methods = ['GET'])
def find_products(product_id):
    product =Querie.find_product_by_id(product_id)
    print(product[1])
    print(product[2])
    print(product [3])
    return render_template("product.html",product = product)
"""Find Products by code"""
@app.route('/products/code',methods= ['POST'])
def find_products_code():
    product_code = request.form['code']
    product = Querie.find_product_by_code(product_code)
    print(product)
    if product is None:
        return redirect(url_for("show_products_all"))
    else:
          return render_template("productfound.html",product = product)
       
        