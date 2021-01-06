from flask import Flask, render_template, request, redirect
from scrapper import get_jobs
app = Flask("Job_Scrapper")

@app.route("/")
def home():
  return render_template("home.html")


@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    jobs=get_jobs(word)
    print(jobs)
  else:
    return redirect("/")
  return render_template("report.html", word = word)

app.run(host="0.0.0.0")