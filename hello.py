def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield environ['QUERY_STRING'].replace('&', '\n').encode('UTF-8')
