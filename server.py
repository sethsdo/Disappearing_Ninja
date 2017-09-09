from flask import Flask, render_template, request, redirect, session

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
def ninjas_color(color):
    print color
    if color == 'blue':
        print 'blue'
        return redirect('/blue')
    elif color == 'orange':
        return redirect('/orange')
    elif color == 'purple':
        return redirect('/purple')
    elif color == 'red':
        return redirect('/red')
    else:
        return redirect('/random')


@app.route('/blue')
def show_blue():
    return render_template('ninja_color.html', current="leonardo.jpg")

@app.route('/orange')
def ninjas2():
    return render_template('ninja_color.html', current="michelangelo.jpg")

@app.route('/red')
def ninjas3():
    return render_template('ninja_color.html', current="raphael.jpg")

@app.route('/purple')
def ninjas4():
    return render_template('ninja_color.html', current="donatello.jpg")

@app.route('/random')
def not_ninja():
    return render_template('ninja_color.html', current="notapril.jpg")

app.run(debug=dev)

