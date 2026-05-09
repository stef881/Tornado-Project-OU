import csv
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
def archive():
    years = [2020, 2021, 2022, 2023, 2024, 2025, 2026]
    return render_template('archive.html', years=years)

@app.route('/archive/<int:year>')
def archive_year(year):
    months = [
        (1, "January"), (2, "February"), (3, "March"), (4, "April"),
        (5, "May"), (6, "June"), (7, "July"), (8, "August"),
        (9, "September"), (10, "October"), (11, "November"), (12, "December")
    ]
    return render_template('year_menu.html', year=year, months=months)

@app.route('/archive/<int:year>/outbreaks')
def year_outbreaks(year):
    # Sample data for year summary (Outbreaks)
    data = {
        2020: [
            {'date': '2020-03-03', 'location': 'Nashville, TN', 'magnitude': 'EF3', 'wind': '165 mph', 'deaths': 25},
            {'date': '2020-04-12', 'location': 'Easter Outbreak (MS)', 'magnitude': 'EF4', 'wind': '190 mph', 'deaths': 32},
            {'date': '2020-05-17', 'location': 'Otter Tail, MN', 'magnitude': 'EF4', 'wind': '170 mph', 'deaths': 0},
            {'date': '2020-08-10', 'location': 'Midwest Derecho', 'magnitude': 'EF1', 'wind': '110 mph', 'deaths': 4},
            {'date': '2020-12-23', 'location': 'Southeast US', 'magnitude': 'EF2', 'wind': '130 mph', 'deaths': 0},
        ],
        2021: [
            {'date': '2021-12-10', 'location': 'Mayfield, KY', 'magnitude': 'EF4', 'wind': '190 mph', 'deaths': 57},
            {'date': '2021-03-25', 'location': 'Alabama Outbreak', 'magnitude': 'EF3', 'wind': '150 mph', 'deaths': 5},
        ],
    }
    year_data = data.get(year, [])
    return render_template('year_data.html', year=year, view_name="Yearly Outbreaks", year_data=year_data)

@app.route('/archive/<int:year>/month/<int:month_id>')
def month_data(year, month_id):
    month_names = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    month_name = month_names.get(month_id, "Unknown Month")
    
    # In a real app, you would filter your database/data by month_id
    # For now, we'll just show empty or sample filtered data
    all_data = {
        2020: [
            {'date': '2020-03-03', 'location': 'Nashville, TN', 'magnitude': 'EF3', 'wind': '165 mph', 'deaths': 25},
            {'date': '2020-04-12', 'location': 'Easter Outbreak (MS)', 'magnitude': 'EF4', 'wind': '190 mph', 'deaths': 32},
            {'date': '2020-05-17', 'location': 'Otter Tail, MN', 'magnitude': 'EF4', 'wind': '170 mph', 'deaths': 0},
            {'date': '2020-08-10', 'location': 'Midwest Derecho', 'magnitude': 'EF1', 'wind': '110 mph', 'deaths': 4},
            {'date': '2020-12-23', 'location': 'Southeast US', 'magnitude': 'EF2', 'wind': '130 mph', 'deaths': 0},
        ]
    }
    
    # Simple mock filtering for the demo
    year_records = all_data.get(year, [])
    month_records = [r for r in year_records if int(r['date'].split('-')[1]) == month_id]
    
    return render_template('year_data.html', year=year, view_name=month_name, year_data=month_records)

@app.route('/data2020')
def data2020():
    from flask import redirect, url_for
    return redirect(url_for('archive_year', year=2020))

@app.route('/archive/search')
def search_archive():
    query = request.args.get('query', '').lower()
    start_date = request.args.get('start_date', '')
    end_date = request.args.get('end_date', '')
    
    # Complete database for searching
    all_tornadoes = [
        {'date': '2020-03-03', 'location': 'Nashville, TN', 'magnitude': 'EF3', 'wind': '165 mph', 'deaths': 25},
        {'date': '2020-04-12', 'location': 'Easter Outbreak (MS)', 'magnitude': 'EF4', 'wind': '190 mph', 'deaths': 32},
        {'date': '2020-05-17', 'location': 'Otter Tail, MN', 'magnitude': 'EF4', 'wind': '170 mph', 'deaths': 0},
        {'date': '2020-08-10', 'location': 'Midwest Derecho', 'magnitude': 'EF1', 'wind': '110 mph', 'deaths': 4},
        {'date': '2020-12-23', 'location': 'Southeast US', 'magnitude': 'EF2', 'wind': '130 mph', 'deaths': 0},
        {'date': '2021-12-10', 'location': 'Mayfield, KY', 'magnitude': 'EF4', 'wind': '190 mph', 'deaths': 57},
        {'date': '2021-03-25', 'location': 'Alabama Outbreak', 'magnitude': 'EF3', 'wind': '150 mph', 'deaths': 5},
    ]
    
    results = []
    for t in all_tornadoes:
        # Filter by name/location
        match_query = not query or query in t['location'].lower()
        
        # Filter by date range
        t_date = t['date']
        match_start = not start_date or t_date >= start_date
        match_end = not end_date or t_date <= end_date
        
        if match_query and match_start and match_end:
            results.append(t)
            
    return render_template('year_data.html', year="Search", view_name="Results", year_data=results)

@app.route('/archive/2020/ashby-ef4')
def ashby_ef4():
    return render_template('year_data.html', 
                           year=2020, 
                           view_name="Ashby EF-4 Tornado", 
                           year_data=[
                               {'date': '2020-07-08', 'location': 'Ashby, MN', 'magnitude': 'EF4', 'wind': '170 mph', 'deaths': 1}
                           ])

@app.route('/archive/2020/easter-outbreak')
def easter_outbreak():
    return render_template('year_data.html', 
                           year=2020, 
                           view_name="Easter 2020 Tornado Outbreak", 
                           year_data=[
                               {'date': '2020-04-12', 'location': 'Mississippi/Alabama/Georgia', 'magnitude': 'EF4', 'wind': '190 mph', 'deaths': 32}
                           ])

@app.route('/archive/2021/lockett-texas')
def lockett_texas():
    return render_template('year_data.html', 
                           year=2021, 
                           view_name="Lockett, Texas Tornado", 
                           year_data=[
                               {'date': '2021-05-04', 'location': 'Lockett, TX', 'magnitude': 'EF3', 'wind': '150 mph', 'deaths': 0}
                           ])

@app.route('/archive/2021/selden-kansas')
def selden_kansas():
    return render_template('year_data.html', 
                           year=2021, 
                           view_name="Selden, Kansas Tornado", 
                           year_data=[
                               {'date': '2021-05-24', 'location': 'Selden, KS', 'magnitude': 'EF2', 'wind': '125 mph', 'deaths': 0}
                           ])

if __name__ == '__main__':
    app.run(debug=True)
