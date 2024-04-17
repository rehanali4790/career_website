from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)

JOBS = [{
    "id": 1,
    "title": "Software Engineer",
    "location": "San Francisco, CA",
    "salary": "$100,000 - $120,000 per year"
}, {
    "id": 2,
    "title": "Data Analyst",
    "location": "New York, NY",
    "salary": "$80,000 - $90,000 per year"
}, {
    "id": 3,
    "title": "Marketing Manager",
    "location": "Los Angeles, CA",
    "salary": "$90,000 - $110,000 per year"
}]
# You can add more jobs here if needed


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Rehan')


@app.route('/api/jobs')
def json_world():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
