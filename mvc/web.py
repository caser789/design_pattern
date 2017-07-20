import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3


class IndexHanlder(tornado.web.RequestHandler):

    def get(self):
        query = "select * from task"
        todos = _execute(query)
        self.render('index.html', todos=todos)


class NewHanlder(tornado.web.RequestHandler):

    def post(self):
        name = self.get_argument('name', None)
        query = 'create table if not exists task (id INTEGER PRIMARY KEY, name TEXT, status NUMERIC)'
        _execute(query)
        query = "insert into task (name, status) values ('%s', %d)" % (name, 1)
        _execute(query)
        self.redirect('/')

    def get(self):
        self.render('new.html')


class UpdateHanlder(tornado.web.RequestHandler):

    def get(self, id, status):
        query = 'update task set status=%d where id=%s' % (int(status), id)
        _execute(query)
        self.redirect('/')


class DeleteHanlder(tornado.web.RequestHandler):

    def get(self, id):
        query = 'delete from task where id=%s' % id
        _execute(query)
        self.redirect('/')

class RunApp(tornado.web.Application):

    def __init__(self):
        Handlers = [
            (r"/", IndexHanlder),
            (r"/todo/new", NewHanlder),
            (r"/todo/update/(\d+)/status/(\d+)", UpdateHanlder),
            (r"/todo/delete/(\d+)", DeleteHanlder),
        ]
        settings = dict(
            debug=True,
            template_path='templates',
            static_path='static'
        )
        tornado.web.Application.__init__(self, Handlers, **settings)

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
