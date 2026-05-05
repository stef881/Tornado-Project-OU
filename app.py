from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/analyzer', methods=['GET', 'POST'])
def analyzer():
    result = None
    color = None
    if request.method == 'POST':
        try:
            mph = int(request.form.get('speed', 0))
            if mph < 65:
                result, color = "Gale", "#ADD8E6"  # Light Blue
            elif 65 <= mph <= 85:
                result, color = "EF0", "#ADD8E6"
            elif 86 <= mph <= 110:
                result, color = "EF1", "#90EE90"   # Light Green
            elif 111 <= mph <= 135:
                result, color = "EF2", "#FFFFE0"   # Light Yellow
            elif 136 <= mph <= 165:
                result, color = "EF3", "#FFD700"   # Bright Orange (Gold)
            elif 166 <= mph <= 200:
                result, color = "EF4", "#FF4500"   # OrangeRed
            else:
                result, color = "EF5", "#FF0000"   # Red
        except ValueError:
            result = "Invalid input"
            color = "white"
            
    return render_template('index.html', result=result, color=color)

@app.route('/archive')
@app.route('/data2020')
def archive():
    return render_template('archive.html')

if __name__ == '__main__':
    app.run(debug=True)
