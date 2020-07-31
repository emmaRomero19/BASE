import web

urls = (
    '/', 'controllers.controller.Control',
    '/page1/?', 'controllers.delete.Op',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()