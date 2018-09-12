import tornado.ioloop
import tornado.web
import os
#USO
#"IPdoPC/videos/"NomedoVideo"
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        
class DownloadHandler(tornado.web.RequestHandler):
    
    def get(self):
        lista = os.listdir(os.path.dirname(os.path.realpath(__file__))+'\\videos')

        listaVideos = ''
        for videos in lista:
            listaVideos += videos +"\n"

        print(listaVideos)    
        self.write(listaVideos)

def make_app():
    script_path = os.path.join(os.path.dirname(__file__), 'videos')
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/videos/(.*)", tornado.web.StaticFileHandler, {"path": script_path}),
        (r'/download', DownloadHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen('8888')
    print("Server ON")
    tornado.ioloop.IOLoop.current().start()
