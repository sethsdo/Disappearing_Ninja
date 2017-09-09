from flask import Flask, render_template, request, redirect,session,g
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

dev = True

@app.route('/')
def no_ninjas():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def ninjas1(color):
    print color
    if color == 'blue':
        print 'green' 
        return render_template('ninja_color.html', current="raphael.jpg")
    else:
        return render_template('ninja_color.html')

# @app.route('/ninja/orange')
# def ninjas2():
#     print "blue"
#     return render_template('ninja_color.html')

# @app.route('/ninja/red')
# def nijas3():
#     print "blue"
#     return render_template('ninja_color.html')

# @app.route('/ninja/purple')
# def nijas4():
#     print "blue"
#     return render_template('ninja_color.html')

app.run(debug=dev)

