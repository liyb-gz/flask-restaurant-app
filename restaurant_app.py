from flask import Flask, render_template
from restaurant_fake_data import *
app = Flask(__name__)

@app.route("/")
@app.route("/restaurants/")
def list_restaurants():
    return render_template('restaurants.html', restaurants = test_reses, items = test_items)

@app.route("/restaurants/add")
def add_restaurant():
	return render_template('restaurants_add.html')

@app.route("/restaurants/<int:restaurant_id>/edit")
def edit_restaurant(restaurant_id):
	return render_template('restaurants_edit.html', restaurant = test_res)

@app.route("/restaurants/<int:restaurant_id>/delete")
def delete_restaurant(restaurant_id):
	return render_template('restaurants_delete.html', restaurant = test_res)

@app.route("/restaurants/<int:restaurant_id>/")
@app.route("/restaurants/<int:restaurant_id>/menu/")
def list_menu_item(restaurant_id):
	return render_template('menu.html', restaurant = test_res, items = [test_item_1])

@app.route("/restaurants/<int:restaurant_id>/menu/add")
def add_menu_item(restaurant_id):
	return "add_menu_item"

@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>/")
@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>/edit")
def edit_menu_item(restaurant_id, menu_item_id):
	return "edit_menu_item"

@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>/delete")
def delete_menu_item(restaurant_id, menu_item_id):
	return "delete_menu_item"


if __name__ == "__main__":
	app.debug = True
	app.run(host = '0.0.0.0', port = 8180)