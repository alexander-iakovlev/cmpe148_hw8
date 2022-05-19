from app import myapp_obj

myapp_obj.run(debug=True, ssl_context=('cert.pem', 'key.pem'))
