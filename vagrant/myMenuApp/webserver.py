from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"): #path is a variable that contains the URL sent by client to server as a string
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "Hello!"
                output += '''<form method ='POST' enctype = 'multipart/form-data' action = '/hello'><h2>What would you like me to say?</h2>
                            <input name = 'message' type = 'text' ><input type = 'submit' value = 'Submit'> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/hola"): #path is a variable that contains the URL sent by client to server as a string
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "&#161Hola!  <a href = '/hello'>Back to Hello</a>"
                    output += '''<form method ='POST' enctype = 'multipart/form-data' action = '/hello'><h2>What would you like me to say?</h2>
                                <input name = 'message' type = 'text' ><input type = 'submit' value = 'Submit'> </form>'''
                    output += "</body></html>"
                    self.wfile.write(output)
                    print output
                    return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Conent-type', 'text/html')
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]

            output += '''<form method ='POST' enctype = 'multipart/form-data' action = '/hello'><h2>What would you like me to say?</h2>
                        <input name = 'message' type = 'text' ><input type = 'submit' value = 'Submit'> </form>'''
                        #call it 'message' because it matches the get command in the post request
            output += "</body></html>"
            self.wfile.write(output)
            print output

        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('',port), webserverHandler) #webserverHandler is class that we defined
        print "Web server running on port %s" % property
        server.serve_forever() #command to keep it constantly listening until ctrlC or closed

    except KeyboardInterrupt: #User holds CTRL+C on keyboard
            print "^C entered, stopping web server..."
            server.socket.close() #shuts down the server

if __name__ == '__main__':
    main()
