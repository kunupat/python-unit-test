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
