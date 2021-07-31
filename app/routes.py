
def routes(api):
    from app.resources.HomeResource import HomeResource
    from app.resources.TodoResource import AllTodoResource, SingleTodoResource
    api.add_resource(HomeResource ,'/')
    api.add_resource(AllTodoResource, '/todos/')
    api.add_resource(SingleTodoResource, '/todo/<int:id>')
