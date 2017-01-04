CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/pi/project',
    #'working_dir': '/home/pi/project/project',
    'user': 'www-data',
    'group': 'www-data',
    'python': '/usr/bin/python',
    'args': (
        '--bind=127.0.0.1:8081',
        '--workers=5', # 5 достаточно для малинки
        '--graceful-timeout=60',
        '--timeout=60',
        #'--debug',
        #'wsgi:application',
	'project.wsgi',
    ),
