#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

DEFAULT_ADDR = "127.0.0.1"
DEFAULT_PORT = 8123

def encodingNumToEncoding( num ):
    if num == 0:
        return "utf-8"
    elif num == 1:
        return "utf-16"
    else:
        return "utf-32"

def boilerplateResponse( req ):
    req.send_response( 200 )
    req.send_header( "Content-type", "text/html" )
    req.end_headers()
    message = "Boiler plate"
    req.wfile.write( message.encode( "utf-8" ) )

class SillyLinesReqHandler( BaseHTTPRequestHandler ):
    def do_POST( self ):
        boilerplateResponse( self )
        content_len = int( self.headers.get( "Content-Length" ) )
        if content_len < 1:
            return
        req_body_bytes = self.rfile.read( content_len )

        # TODO: decode the body
        encoding = "TODO"
        print( "The client chose encoding %s" % encoding )
        lines = [ "TODO", "TODO", "TODO" ]

        for idx in range( len( lines ) ):
            print( "%d:%s  -  " % ( idx, lines[ idx ] ), end="" )
        print( "" )
        return

def runServer():
    print( "Starting server..." )
    server_address = ( DEFAULT_ADDR, DEFAULT_PORT )
    httpd = HTTPServer( server_address, SillyLinesReqHandler )
    print( "Running server..." )
    httpd.serve_forever()

if __name__ == "__main__":
    runServer()
