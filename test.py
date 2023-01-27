from flask import Flask, flash, redirect, render_template, request, session, abort

#all routes need to be below this app variable declaration
app = Flask(__name__)

@app.route('/')
def test1():
	return 'Accessed endpoint powered by Flask and Python.'
	
@app.route('/param')
def param_home():
	return 'Parameter may be submitted to this url.'
	
@app.route('/param/<name>')
def param_submit(name):
	return render_template('test.html', name=name)	#Added call to html template
	#return 'Parameter %s!' % name	#comment out this line when using template

#all routes need to be above this if statement
if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5090')
