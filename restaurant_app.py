from flask import Flask, render_template, redirect, request
from database import *
from restaurant_fake_data import *
app = Flask(__name__)

DBSession = sessionmaker(bind=engine)

@app.route("/")
@app.route("/restaurants/")
def list_restaurants():
	session = DBSession()
	restaurants = session.query(Restaurant).all()
	items = session.query(MenuItem).all()
	session.close()
	return render_template('restaurants.html', restaurants = restaurants, items = items)

# TODO: add try-except structure for malformed form, null fields, and overlong strings
@app.route("/restaurants/add", methods = ['GET', 'POST'])
def add_restaurant():
	if request.method == 'POST':
		restaurant = Restaurant()
		restaurant.name = request.form['name']
		restaurant.description = request.form['description']
		session = DBSession()
		session.add(restaurant)
		session.commit()
		session.close()
		return redirect("/", code = 302)
	else:
		return render_template('restaurants_add.html')

@app.route("/restaurants/<int:restaurant_id>/edit", methods = ['GET', 'POST'])
def edit_restaurant(restaurant_id):
	if request.method == 'POST':
		session = DBSession()
		restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
		restaurant.name = request.form['name']
		restaurant.description = request.form['description']
		session.commit()
		session.close()
		return redirect("/", code = 302)
	else:
		session = DBSession()
		restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
		session.close()
		return render_template('restaurants_edit.html', restaurant = restaurant)

@app.route("/restaurants/<int:restaurant_id>/delete", methods = ['GET', 'POST'])
def delete_restaurant(restaurant_id):
	if request.method == 'POST':
		if request.form['submit'] == 'delete':
			session = DBSession()
			restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
			session.delete(restaurant)
			session.commit()
			session.close()
		return redirect("/", code = 302)
	else:
		session = DBSession()
		restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
		session.close()
		return render_template('restaurants_delete.html', restaurant = restaurant)

@app.route("/restaurants/<int:restaurant_id>/")
@app.route("/restaurants/<int:restaurant_id>/menu/")
def list_menu_item(restaurant_id):
	session = DBSession()
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
	session.close()
	return render_template('menu.html', restaurant = restaurant, items = items)

@app.route("/restaurants/<int:restaurant_id>/menu/add")
def add_menu_item(restaurant_id):
	return render_template('menu_add.html', restaurant = test_res)

@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>/")
@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>/edit")
def edit_menu_item(restaurant_id, menu_item_id):
	return render_template('menu_edit.html', restaurant = test_res, item = test_item_1)

@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>/delete")
def delete_menu_item(restaurant_id, menu_item_id):
	return render_template('menu_delete.html', restaurant = test_res, item = test_item_1)


if __name__ == "__main__":
	app.debug = True
	app.run(host = '0.0.0.0', port = 8180)