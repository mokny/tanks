import mokkalib

class Main():
    def __init__(self, database, webserver, websocketserver):  
        self.database = database
        self.webserver = webserver
        self.websocketserver = websocketserver

        # Set Script variables for the webserver.
        self.webserver.setscriptvar('websocket.host', self.websocketserver.host)
        self.webserver.setscriptvar('websocket.port', self.websocketserver.port)

        self.webserver.setscriptfunction('test', self.test)

        mokkalib.triggerGlobalEvent('INITIALIZED')

    def test(self, a):
        return 'yop' + str(a)