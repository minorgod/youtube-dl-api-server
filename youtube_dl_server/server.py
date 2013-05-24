from paste import httpserver
import argparse

from .app import app
from .version import __version__

"""
    A server for providing the app anywhere, no need for GAE
"""

def main():

    desc="""
         The youtube-dl API server.
         """
    default_port = 9191
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-p','--port',
                       default= default_port,
                       type=int,
                       help='The port the server will use. The default is: {}'.format(default_port)
                       )
    parser.add_argument('--version', action='store_true', help='Print the version of the server')

    args = parser.parse_args()
    if args.version:
        print(__version__)
        exit(0)
    httpserver.serve(app, host='localhost', port=args.port)

if __name__ == '__main__':
    main()
