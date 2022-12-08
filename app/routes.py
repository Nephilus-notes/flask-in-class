

# user_data = { #mock user table
#     'dylans': {
#         'user_id':1,
#         'email': 'dylans@gmail.com',
#         'name': 'Dylan Smith',
#         'favorite_color': 'Purple',
#         'is_active': True,
#         'reviews': ['Dylan is a great dev!', 'He\'s the best']
#     },
#     'jdoe': {
#         'user_id':2,
#         'email': 'jd@gmail.com',
#         'name': 'Jessica Doe',
#         'favorite_color': 'Yellow',
#         'is_active': True,
#             'reviews': ['Jess is a great dev!', 'She\'s awesome']

#     },
#     'dannyboy': {
#         'user_id':3,
#         'email': 'dannyb@gmail.com',
#         'name': 'Danny Boylston',
#         'favorite_color': 'Purple',
#         'is_active': False,
#         'reviews': ['Danny is a terrible dev!', 'He\'s the rough']

#     }
# }

# @app.route('/api/test')
# def test():
#     context = { 
#         'name': 'Sandrine',
#         'score': 100,
#         'max_score': 100,
#         'test_name': 'Python Challenge'
#     }

#     return render_template('test_message.html', **context)

# max_score = 100
# test_name = "Python Challenge"
# students = [
#     {"name": "Sandrine",  "score": 100},
#     {"name": "Gergeley", "score": 87},
#     {"name": "Frieda", "score": 92},
# ]

# @app.route('/profile/<username>')
# def display_profile(username):
#     return render_template('profile.html.j2', **user_data[username])

# # functions/Endpoints
# # 1. Get all users and their data /
# # 2. Get all user emails /
# # 3. Get a user by their username
# # 4. Get a user by their email
# # 5. Find all users by a specificed favorite color

# # write an endpoint that gives active users names


# @app.route('/api/users')
# def get_users():
#     return user_data

# @app.route('/api/users/emails')
# def get_user_emails():
#     emails = []
#     for user in user_data.values():
#         emails.append(user['email'])

#     return emails

# @app.route('/api/users/active')
# def get_active_users():
#     full_names = []

#     for user in user_data.values():
#         if user['is_active'] == True:
#             full_names.append(user['name'])

#     return full_names

# @app.route('/api/user/<username>')
# def get_user_by_username(username):
#     if username in user_data:
#         return user_data[username]
    
#     return f'User with username {username} not found'
# @app.route('/api/user/email/<email>')
# def get_user_by_email(email):
#     for user in user_data.values():
#         if user['email'] == email:
#             return user
    
#     return f'User with email {email} not found'

# @app.route('/api/users/color/<favorite_color>')
# def get_users_by_color(favorite_color):
#     users = []

#     for user in user_data.values():
#         if user['favorite_color'].lower() == favorite_color.lower():
#             users.append(user)

#     return users

# @app.route('/api/users/<username>/reviews/<review_idx>')
# def get_user_review(username, review_idx):
#     return user_data[username]['reviews'][int(review_idx)]


# car_data = {
#     '0': {
#         "name": "Maruti Swift Dzire VDI",
#         "year": 2014,
#         "selling_price": 450000
#     },
#     '1': {
#         "name": "Skoda Rapid 1.5 TDI Ambition",
#         "year": 2014,
#         "selling_price": 370000
#     },
#     '2': {
#         "name": "Honda City 2017-2020 EXi",
#         "year": 2006,
#         "selling_price": 158000
#     }
# }

# # create 2 routes/templates
# #  - display all cars and their information (not dynamic)
# #  - display a specific car, will be dynamic

# @app.route('/cars')
# def show_cars():
#     return render_template('./cars.html.j2', car_data=car_data)

# @app.route('/cars/<id>')
# def show_car(id):
#     return render_template('./car.html.j2', **car_data[id])


# # Get all cars _/
# @app.route('/api/cars')
# def get_cars():
#     return car_data

# # Get cars in a dictionary separated by year, for example:
# @app.route('/api/cars/by_year')
# def get_cars_by_year():
#     result = {}

#     for car in car_data.values():
#             if car['year'] in result:
#                 result[car['year']].append(car['name'])
#             else:
#                 result[car['year']] = [car['name']]
                
#     return result

# car_year_result = {
#     2014: ["Maruti Swift Dzire VDI","Skoda Rapid 1.5 TDI Ambition"],
#     2006: ["Honda City 2017-2020 EXi"]
# }
# # Get a car by it's ID (it's ID is just the key in the car data dictionary)
# @app.route('/api/cars/<id>')
# def get_car_by_id(id):
#     id = int(id)
#     if id in car_data:
#         return car_data[id]



#     # for car, value in car_data.items():
#     #     if int(id) == car:
#     #         return value 
    
#     return f'ID number {id} not found'

# # Get all cars below a given price point, so if the user enters 380000, you'd show the second and third cars

# @app.route('/api/cars/by_pricepoint/<price>')
# def get_car_by_pricepoint(price):
#     # result = {}
#     # n = 0
#     # for car, info in car_data.items():
#     #     if info['selling_price'] < int(price):
#     #         result[car] = info
    
#     result = []

#     for car in car_data.values():
#         if car['selling_price'] < int(price):
#             result.append(car)

#     return result



# # @app.route('/contact')
# # def best():
# #     return 'contact'

# # @app.route('/blog')
# # def blog():
# #     return 'blog'

# # @app.route('/shop')
# # def shop():
# #     return 'shop'
