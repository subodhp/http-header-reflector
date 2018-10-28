# Maintainer - subodh.cyber@gmail.com
# Inspired from https://gist.github.com/huyng/814831

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        request_path = self.path

        print("\n----- Begin ----->")
        print(request_path)
        print( self.headers)
        print("<----- End -----\n")

        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")

    def do_POST(self):

        request_path = self.path

        print("\n----- Start ----->")
        print(request_path)

        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0

        print(request_headers)
        print(self.rfile.read(length))
        print("<----- End -----\n")

        self.send_response(200)

    do_PUT = do_POST
    do_DELETE = do_GET
        
def main():
    port = 8181
    print('Server running on all interfaces:%s' % port)
    server = HTTPServer(('0.0.0.0', port), RequestHandler)
    server.serve_forever()
        
if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Simple HTTP Server to log the http request header and fields for POST/GET\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()
    
main()
