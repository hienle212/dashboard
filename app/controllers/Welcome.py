from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('Model')
        self.db = self._app.db

   
    def index(self):
        return self.load_view('demo.html')
    def register_page(self):
        return self.load_view('register.html')
    def login_page(self):
    	return self.load_view('signin.html')
    def register(self):
        user_info = self.models['Model'].register(request.form)
        print user_info
        if user_info['status'] == True:
            session['id'] = user_info['user']['id'] 
            session['first_name'] = user_info['user']['first_name']
            session['last_name'] = user_info['user']['last_name']
            session['created_at'] = user_info['user']['created_at'] 
            session['email'] = user_info['user']['email']
            session['user_level'] = user_info['user']['user_level']
            return redirect ('/dashboard')        
        else:
            for message in user_info['errors']:
                flash(message)
            return redirect ('/registerPage')

    def login(self):
        login_info = self.models['Model'].login(request.form)
        print login_info
        if login_info['status'] == True:
            session['id'] = login_info['user']['id'] 
            session['first_name'] = login_info['user']['first_name']
            session['last_name'] = login_info['user']['last_name']
            session['created_at'] = login_info['user']['created_at'] 
            session['email'] = login_info['user']['email']
            session['user_level'] = login_info['user']['user_level']
            return redirect ('/dashboard')
        else:
            for message in login_info['errors']:
                flash(message)
    		return redirect('/loginPage')
    def dashboard(self):
        all_users = self.models['Model'].get_all_users()
        if session['user_level'] != 'normal':
            return self.load_view('admin_page.html', all_users = all_users)
        else:
            return self.load_view('users_page.html',all_users = all_users)

    def show(self, user_id):
        users_info =  self.models['Model'].show(user_id)
        messages = self.models['Model'].messages(user_id)
        comments = self.models['Model'].comments(user_id)
        return self.load_view('usermain.html', users_info = users_info,comments = comments, messages = messages, user_id = user_id)

    def destroy(self,user_id):
        self.models['Model'].remove(user_id)
        return redirect ('/dashboard')
    def add_message(self):
        self.models['Model'].post_message(request.form)
        return redirect ('/users/show/' + request.form['poster_id']) 
    def add_comment(self):
        newcomment = {'comment': request.form['comment'], 'user_id': session['id'], 'message_id' : request.form['message_id']}
        self.models['Model'].post_comment(newcomment)
        return redirect ('/users/show/' + newcomment['message_id']) 
    def view_add(self):
        return self.load_view('adduser_page.html')
    def create_user(self, methods=['POST']):
        self.models['Model'].add_users(request.form)
        return redirect('/dashboard')
    def view_edit(self,user_id):
        return self.load_view('edit_profile.html')
    def admin_edit(self,user_id):
        return self.load_view('edit_user.html', user_id = user_id)
    def update(self):
        self.models['Model'].edit(request.form)
        return redirect('/dashboard')
    def update_password(self):
        self.models['Model'].edit_password(request.form)
        return redirect ('/dashboard')
    def update_description(self):
        self.models['Model'].edit_description(request.form)
        return redirect('/dashboard')
    def admin_edit_users(self):
        self.models['Model'].admin_edit(request.form)
        return redirect('/dashboard')



