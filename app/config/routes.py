"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes


routes['default_controller'] = 'Welcome'
routes['/registerPage'] = 'Welcome#register_page'
routes['/loginPage'] = 'Welcome#login_page'
routes['POST']['/register'] = 'Welcome#register'
routes['POST']['/login'] = 'Welcome#login'
routes['/user/new'] = 'Welcome#view_add'
routes['/users/show/<user_id>'] = 'Welcome#show'
routes['/remove/<user_id>'] = 'Welcome#destroy'
routes['/dashboard'] = 'Welcome#dashboard'
routes ['POST']['/message'] = 'Welcome#add_message'
routes ['POST']['/comment'] = 'Welcome#add_comment'
routes['POST']['/create'] = 'Welcome#create_user'
routes['/viewedit/<user_id>'] = 'Welcome#view_edit'
routes['/edits/<user_id>'] = 'Welcome#admin_edit'
routes['POST']['/update'] = 'Welcome#update'
routes['POST']['/update/password'] = 'Welcome#update_password'
routes['POST']['/update/description'] = 'Welcome#update_description'
routes['POST']['/admin/edit'] = 'Welcome#admin_edit_users'












"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.
    
    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
