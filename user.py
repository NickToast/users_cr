#import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

#model the class after the users table from db
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #use class method to query our database
    @classmethod
    def get_all(cls):
        query = """
        SELECT *
        FROM users;
        """
        #call the connectToMySQL function with the schema I'm targeting 
        results = connectToMySQL('users_schema').query_db(query)
        #create an empty list to append our instances of users
        users = [];
        #iterate over the db users and create instances with cls
        for u in results:
            users.append(cls(u))
        print (users)
        return users
    
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s)
        """

        results = connectToMySQL('users_schema').query_db(query, data)
        return results
    
