from system.core.model import Model
import re     

class Model(Model):
    def __init__(self):
        super(Model, self).__init__()
    def register(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')
        errors = []
        if len(info['first_name']) < 2 or not info['first_name'].isalpha():
            errors.append("Invalid First Name. (Letters only, at least 2 characters.)")
        if len(info['last_name']) < 2 or not info['last_name'].isalpha():
            errors.append("Invalid Last Name. (Letters only, at least 2 characters.)")
        if len(info['email']) < 1 or not EMAIL_REGEX.match(info['email']):
            errors.append ("Invalid Email Address!")    
        if len(info['password']) < 8 :
            errors.append("Password should be more than 8 characters")
        if info['password'] != info['confirm_password']:
            errors.append('Password and confirm password must match!')
        if PASSWORD_REGEX.match(info['confirm_password']):
            errors.append("Password requires to have at least 1 uppercase letter and 1 numeric value ")   
        if errors:
            return {"status":False, "errors":errors}            
        else:  
            query = "INSERT into users (first_name, last_name, email, user_level, description, password, created_at, updated_at) VALUES(:first_name,:last_name,:email, :user_level, :description,:password, NOW(),NOW())"
            data = {'first_name': info['first_name'], 'last_name': info['last_name'], 'email' :info['email'], 'user_level' :'normal', 'description' :'', 'password' :info['password']}
            self.db.query_db(query, data)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return {"status": True, "user": users[0]}
    def login(self,info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if len(info['email']) < 1 or not EMAIL_REGEX.match(info['email']):
            errors.append ("Invalid Email Address!")    
        if len(info['password']) < 8 :
            errors.append("Password should be more than 8 characters")
        if errors:
            return {"status":False, "errors":errors}            
        else:  
            query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            data = {'email' : info['email']}
            users = self.db.query_db(query,data) 
            return {"status": True, "user": users[0]}
    def get_all_users(self):
        query = "SELECT users.id as user_id, user_level, concat(first_name,' ', last_name) as name, email, created_at FROM users" 
        return self.db.query_db(query) 
    def remove(self, users_id):
        query = "DELETE FROM users WHERE users.id = :users_id"
        data =  {"users_id" : users_id}
        return self.db.query_db(query, data) 
    def show(self, user_id):
        query = "SELECT users.id as users_id, first_name, last_name, email, created_at, description FROM users WHERE id=:user_id"
        data =  {"user_id" : user_id}
        return self.db.query_db(query, data)
    def post_message(self, info):
        query = "INSERT INTO messages(message, created_at, updated_at, users_id, poster_id) VALUES(:message, now(), now(), :users_id, :poster_id);"
        data = {'message': info['message'], 'users_id' : info['users_id'], 'poster_id' : info['poster_id']}
        return self.db.query_db(query, data)
    def messages(self, user_id):
        query = 'select messages.users_id as m_users, messages.id as m_id, messages.message, messages.created_at as m_c_at, concat(users.first_name," ", users.last_name) as m_author from messages left join users on messages.users_id = users.id'
        data =  {"users_id" : user_id}
        return self.db.query_db(query,data)
    def comments(self, user_id):
        query = 'select comments.id as c_id, comments.comment, comments.created_at as c_c_at,comments.message_id as m_id, concat(users.first_name," ", users.last_name) as c_author from comments left join users on comments.user_id = users.id'
        data =  {"users_id" : user_id}
        return self.db.query_db(query,data)
    def post_comment(self, info):
        query = "INSERT INTO comments(comment, created_at, updated_at, user_id, message_id) VALUES(:comment, now(), now(), :user_id, :message_id)"
        data = {'comment': info['comment'], 'user_id' : info['user_id'], 'message_id' : info['message_id']}
        return self.db.query_db(query, data)
    def add_users(self, info):
        query = "INSERT into users (first_name, last_name, email, user_level, description, password, created_at, updated_at) VALUES(:first_name,:last_name,:email, :user_level, :description,:password, NOW(),NOW())"
        data = {'first_name': info['first_name'], 'last_name': info['last_name'], 'email' :info['email'], 'user_level' :'normal', 'description' :'', 'password' :info['password']}
        return self.db.query_db(query, data)
    def edit(self, info):
        query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email WHERE users.id = :id"
        data = {'last_name': info['last_name'], 'first_name' : info['first_name'], 'email' : info['email'], 'id' : info['id']}
        return self.db.query_db(query, data)
    def edit_password(self, info):
        query = "UPDATE users SET password = :password WHERE users.id = :id"
        data = {'password': info['password'], 'id' : info['id']}
        return self.db.query_db(query, data)
    def edit_description(self, info):
        query = "UPDATE users SET description = :description WHERE users.id = :id"
        data = {'description': info['description'], 'id' : info['id']}
        return self.db.query_db(query, data)
    def admin_edit(self, info):
        query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, user_level =:user_level WHERE users.id = :id"
        data = {'last_name': info['last_name'], 'first_name' : info['first_name'], 'email' : info['email'],'user_level' : info['user_level'], 'id' : info['id']}
        return self.db.query_db(query, data)
