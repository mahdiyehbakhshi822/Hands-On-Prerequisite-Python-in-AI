'''
Write the products management project as follows.
1. Product information includes name and price.
2. Use list to save information
3. We do not have duplicate product name
4. This project includes sections for adding, deleting, editing, detail and searching by
product name.
6. For the detail section, display the total number of products, the average price, the
most expensive and cheapest product.
5. The program should continue until the user enters "exit".
'''
print("************you are welcome***************")
name_product = []
price_product = []

while True:
	user = input("enter a option(add/delete/edit/detail/search) :")
######################################
	if user == "add":
		product = input("Enter a product to add: ")
		price = int(input("Enter price: "))
		if product not in name_product:
			name_product.append(product)
			price_product.append(price)
			print("product add\n")
		else:
			print(f"{product}: exist!\n")
#######################################
	elif user == "delete":
		pro_del = input("enter product: ")
		if pro_del in name_product:
			name_product.remove(pro_del)
			i = pro_del.index()
			pro_del.pop(i)
			print("successfully delete!!")
		else:
			print("product not exist ")
        
# 		index = input("index of product: ")
# 		list1 = [int(i)-1 for i in index.split()]
# 		for i in list1:
#  			name_product.pop(i)
#  			price_product.pop(i)
        
        
####################################
	elif user == "edit":
		new_product = input("new product  : ")
		new_price = input("new pricce  : ")
		i = int(input("index of porduct which will edit : "))
		if new_product not in name_product:
			name_product[i] = new_product
			price_product[i] = new_price
			print("successfully edited")
		else:
			print(f"{new_product}: exist!")
        
# 		index = input("index of product: ") 
# 		list1 = [int(i)-1 for i in index.split()]
# 		for i in list1:
# 			new_product = input("new product: ")
# 			if new_product not in name_product:
# 				name_product[i] = new_product
# 			else:
# 				print(f"{new_product}: exist!")
    
###################################
	elif user == "detail":
		for i in range(len(name_product)):
			print(f"product {i+1} : {name_product[i]} ====> price : {price_product[i]}")
#display the total number of products, the average price, the most expensive and cheapest product
		print(f"total number of products : {len(name_product)}")
		print(f"average price : {sum(price_product)/len(price_product)}")
		i = price_product.index(max(price_product))
		j = price_product.index(min(price_product))
		
		print(f"most expensive product : {name_product[i]}")
		print(f"cheapest product : {name_product[j]}" )
        
##################################
	elif user == "search":
		word = input("product to search: ")
		for i, p in enumerate(name_product):
			if word in p:
				print(f"found in index {i}")
			else:
				print("not found!!")
################################
	elif user == "":
		pass
#################################
	elif user == "exit":
		break
#################################
	else:
		print(f"{user}: command not found!")
