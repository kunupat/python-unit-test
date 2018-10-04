import re

class InsufficientException(Exception):
	pass

class MobileInventory:
	def __init__(self,inventory=None):
		if(inventory == None):
			self.balance_inventory = {}
		elif(not isinstance(inventory,dict)):
			raise TypeError("Input inventory must be a dictionary")
		elif(isinstance(inventory, dict)):
			self.balance_inventory = inventory
			for key in self.balance_inventory.keys():
				if(not isinstance(key, str)):
					raise ValueError("Mobile model name must be a string")
			for val in self.balance_inventory.values():
				print("KP:::", val)
				if isinstance(val,str) or int(val) < 0:
					print("KP::: Raise.....")
					raise ValueError("No. of mobiles must be a positive integer")
					break;	

	def add_stock(self, new_stock):
		if(not isinstance(new_stock, dict)):
			raise TypeError("Input stock must be a dictionary")
		else:
			for key in new_stock.keys():
				if(not isinstance(key, str)):
					raise ValueError("Mobile model name must be a string")
			for val in new_stock.values():
				if(not isinstance(val, int)):
					raise ValueError("No. of mobiles must be a positive integer")
			for new_stock_key in new_stock.keys():
				for balance_inventory_key in self.balance_inventory.keys():
					if(new_stock_key == balance_inventory_key):
						self.balance_inventory[balance_inventory_key] = self.balance_inventory.get(balance_inventory_key) + new_stock.get(new_stock_key)

	def sell_stock(self,requested_stock):
		if(not isinstance(requested_stock, dict)):
			raise TypeError("Requested stock must be a dictionary")
		else:
			for key in requested_stock.keys():
				if(notisinstance(key, str)):
					raise ValueError("Mobile model name must be a string")
			for val in requested_stock.values():
				if(not isinstance(val, int)):
					raise ValueError("No. of mobiles must be a positive integer")
			if not all (keys in requested_stock for keys in (self.balance_inventory.keys())):
				raise InsufficientException("No Stock. New Model Request")
			
			if all(vals in requested_stock.values() != vals in self.balance_inventory.values()):
				raise InsufficientException("Insufficient Stock")
