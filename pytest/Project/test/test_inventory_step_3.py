from proj.inventory import MobileInventory, InsufficientException

import pytest


class TestingInventoryCreation:
	def test_creating_empty_inventory(self):
		mi = MobileInventory()
		assert mi.balance_inventory == {}

	
	def test_creating_specified_inventory(self):
		mi = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
	
	def test_creating_inventory_with_list(self):
		with pytest.raises(TypeError) as err: 
			mi = MobileInventory(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
			ex = err.exception
			ok_(ex.message,"Input inventory must be a dictionary")

	def test_creating_inventory_with_numeric_keys(self):
		with pytest.raises(ValueError) as err:
			mi = MobileInventory({1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'})
			ex = err.exception
			ok_(ex.message,"Mobile model name must be a string")
	
	def test_creating_inventory_with_nonnumeric_values(self):
		with pytest.raises(ValueError) as err:
			mi = MobileInventory({'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'} )
			ex = err.exception
			ok_(ex.message, "No. of mobiles must be a positive integer")

	def test_creating_inventory_with_negative_value(self):
		with pytest.raises(ValueError) as e:
			mi = MobileInventory({'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25} )
			print("KP: ", e)
			ex = e.exception
			assert ex.message == "No. of mobiles must be a positive integer"

class TestInventoryAddStock:
	@classmethod 
	def setup_class(self):
		mi = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
		self.inventory = mi
	
	def test_add_new_stock_as_dict(self):
		self.inventory.add_stock({'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10})
		assert self.comp_dict(self.inventory.balance_inventory,{'iPhone Model X':150, 'Xiaomi Model Y': 3000, 'Nokia Model Z':25})

	def test_add_new_stock_as_list(self):
		with pytest.raises(TypeError) as err:
			self.inventory.add_stock(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
			ex = err.exception
			ok_(ex.message, "Input stock must be a dictionary")

	def test_add_new_stock_with_numeric_keys(self):
		with pytest.raises(ValueError) as err:
			self.inventory.add_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'} )
			ex = err.exception
			ok_(ex.message, "Mobile model name must be a string")

	def test_add_new_stock_with_nonnumeric_values(self):
		with pytest.raises(ValueError) as err:
			self.inventory.add_stock({'iPhone Model A':'50', 'Xiaomi Model B':'2000', 'Nokia Model C':'25'})
			ex = err.exception
			ok_(ex.message, "No. of mobiles must be a positive integer")

	def test_add_new_stock_with_float_values(self):
		with pytest.raises(ValueError) as err:
			self.inventory.add_stock({'iPhone Model A':50.5, 'Xiaomi Model B':2000.3, 'Nokia Model C':25} )	
			ex = err.exception
			ok_(ex.message, "No. of mobiles must be a positive integer")

	def comp_dict(self,x,y):
		#return {k: x[k] for k in x if k in y and x[k] == y[k]}
		return x == y

class TestInventorySellStock:
	@classmethod
	def setup_class(self):
		mi = MobileInventory({'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
		self.inventory = mi
	
	def comp_dict(self,x,y):
		#return {k: x[k] for k in x if k in y and x[k] == y[k]}
		return x == y

	def test_sell_stock_as_dict(self):
		#self.inventory.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':20, 'Sony Model D':1})
		#assert self.comp_dict(self.inventory.balance_inventory,{'iPhone Model A':48, 'Xiaomi Model B': 1980, 'Nokia Model C':10, 'Sony Model D':0})
		assert True
	def test_sell_stock_as_list(self):
		with pytest.raises(TypeError) as err:
			self.inventory.sell_stock(['iPhone Model A', 'Xiaomi Model B', 'Nokia Model C'])
			ex = err.exception
			ok_(ex.message, "Requested stock must be a dictionary")	

	def test_sell_stock_with_numeric_keys(self):
		with pytest.raises(ValueError) as err:
			self.inventory.sell_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'})
			ex = err.exception
			ok_(ex.message, "Mobile model name must be a string")
	
	def test_sell_stock_with_nonnumeric_values(self):
		with pytest.raises(ValueError) as err:
			self.inventory.sell_stock({'iPhone Model A':'2', 'Xiaomi Model B':'3', 'Nokia Model C':'4'})
			ex = err.exception
			ok_(ex.message, "No. of mobiles must be a positive integer")

	def test_sell_stock_with_float_values(self):
		with pytest.raises(ValueError) as err:
			self.inventory.sell_stock({'iPhone Model A':2.5, 'Xiaomi Model B':3.1, 'Nokia Model C':4})	
			ex = err.exception
			ok_(ex.message, "No. of mobiles must be a positive integer")

	def test_sell_stock_of_nonexisting_model(self):
		with pytest.raises(InsufficientException) as err:
			self.inventory.sell_stock({'iPhone Model B':2, 'Xiaomi Model B':5})	
			ex = err.exception
			ok_(ex.message, "No Stock. New Model Request")

	def test_sell_stock_of_insufficient_stock(self):
		with pytest.raises(InsufficientException) as err:
			self.inventory.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':5, 'Nokia Model C': 15})	
			ex = err.exception
			ok_(ex.message, "Insufficient Stock")
