from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Restaurant(Base):
	__tablename__ = 'restaurant'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	description = Column(String(250))
	menu_items = relationship('MenuItem', backref = 'restaurant')

	@property
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'menu_items': [menu_item.serialize for menu_item in self.menu_items]
		}

class MenuItem(Base):
	__tablename__ = "menu_item"

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	description = Column(String(250))
	course = Column(String(250))
	price = Column(String(8))

	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	# restaurant = relationship(Restaurant)

	@property
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'course': self.course,
			'price': self.price
		}

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)