#!/usr/bin/env python3

import sys
import http.client
import json
import random

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 8123

openConnection = http.client.HTTPConnection

def encodingNumToEncoding( num ):
    if num == 0:
        return "utf-8"
    elif num == 1:
        return "utf-16"
    else:
        return "utf-32"

def runClient():
    print( "Running Silly Encoding Client" )
    lines = []
    for line in sys.stdin:
        lines.append( line.strip() )
        encoding_num = random.randint( 0, 2 )

        # TODO encode lines
        encoding = "TODO"
        body_bytes = b'TODO - do not forget to prepend the encoding number'

        print( "I randomly chose encoding %s" % encoding )
        connection = openConnection( DEFAULT_HOST, DEFAULT_PORT )
        connection.request( "POST", "does_not_matter.html", body=body_bytes )
        connection.close()

if __name__ == "__main__":
    runClient()
