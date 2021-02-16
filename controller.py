import json


class DB_Controller(object):

    def __init__(self):

        self.PRODUCT_CATEGORIES = [
            "Computers",
            "Video Games",
            "Computer Accessories",
            "Video Game Accessories"
        ]
        self.db_file = 'Database/db.json'

        with open(self.db_file, 'r') as openfile:
            json_obj = json.load(openfile)

        self.json_object = json_obj

        self.num_entries = len(json_obj['products'])

    def insert_product(self, name, category, price):
        if category in self.PRODUCT_CATEGORIES and not bool(self.select_product(name)):
            new_product = {
                'name': name,
                'id': self.num_entries + 1,
                'category': category,
                'price': price
            }

            self.num_entries += 1

            self.json_object['products'].append(new_product)

            with open(self.db_file, 'w') as outfile:
                json.dump(self.json_object, outfile)

            return True
        else:
            return False

    def select_product(self, name):
        product = {}

        for entry in self.json_object['products']:
            if name == entry['name']:
                product = entry

        return product

    def delete_product(self, name):
        for entry in self.json_object['products']:
            if name == entry['name']:
                self.json_object['products'].remove(entry)
                with open(self.db_file, 'w') as outfile:
                    json.dump(self.json_object, outfile)
                return True
        return False

    def input_controller(self):
        print('Welcome to the DB Controller')
        while True:
            action = ''
            while action != 'Insert' and action != 'Select' and action != 'Delete' and action != 'Exit':
                action = input(
                    'What do you want to do? (Insert - Insert New Product; Select - Select existing Product according to name; Delete - Delete Existing Product; Exit)\n')

            if action == 'Insert':
                name = input('What is the name of the product?\n')
                price = input('What is its price?\n')

                category = ''

                while category not in self.PRODUCT_CATEGORIES:
                    category = input(
                        'In which category does this product fits (Computers, Computer Accessories, Video Games, Video Game Accessories)\n')

                self.insert_product(name, category, price)
                print('You have successfully inserted the product')

            elif action == 'Select':
                name = input('What is the name of the product?\n')
                product = self.select_product(name)
                if bool(product):
                    print('Name:' + product['name'])
                    print('Category:' + product['category'])
                    print('Price: $' + str(product['price']))
                    print('\n')
                else:
                    print('There is no such product available')

            elif action == 'Delete':
                name = input('What is the name of the product?\n')
                result = self.delete_product(name)
                if result:
                    print('Product has been removed succesfully')
                else:
                    print('There is no such product available')

            else:
                break
