from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/restaurants/")
def list_restaurants():
    return "list_restaurants"

@app.route("/restaurants/add")
def add_restaurant():
	return "add_restaurant"

@app.route("/restaurants/<int:restaurants_id>/edit")
def edit_restaurant():
	return "edit_restaurant"

@app.route("/restaurants/<int:restaurants_id>/delete")
def delete_restaurant():
	return "delete_restaurant"

@app.route("/restaurants/<int:restaurants_id>/")
@app.route("/restaurants/<int:restaurants_id>/menu/")
def list_restaurant_menu(restaurants_id):
	return "list_restaurant_menu"

@app.route("/restaurants/<int:restaurants_id>/menu/add")
def add_menu_item(restaurants_id):
	return "add_menu_item"

@app.route("/restaurants/<int:restaurants_id>/menu/<int:menu_item_id>/")
@app.route("/restaurants/<int:restaurants_id>/menu/<int:menu_item_id>/edit")
def edit_menu_item(restaurants_id, menu_item_id):
	return "edit_menu_item"

@app.route("/restaurants/<int:restaurants_id>/menu/<int:menu_item_id>/delete")
def delete_menu_item(restaurants_id, menu_item_id):
	return "delete_menu_item"


if __name__ == "__main__":
	app.debug = True
	app.run(host = '0.0.0.0', port = 8180)