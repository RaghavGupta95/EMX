# from rejson import Client 
import puzzlesolver
from flask import Flask, render_template, request, jsonify
#from http import HTTPStatus
app = Flask(__name__)
# rj = Client(host='localhost', port=6379)

"""
All bad routes get send to 404.html with response code 404- Page not found

"""
@app.errorhandler((404)) 
def handle_error(error):
    return render_template('404.html'), 404
"""
Parse input and respond with appropriate value, 200- OK. If no value return 400- Bad request
"""
@app.route('/' , methods=['GET'])
def index():
    # if query or description missing return 400 
    if "q" not in request.args or "d" not in request.args: 
        return "400 Bad Request",400
    query  = request.args.get("q")
    query = query.lower()
    description = request.args.get("d")
    info = {
    "ping" : "OK",
    "status" : "Yes",
    "degree" : "B.S in Computer Engineering With Focus In Data Sciences From Penn State University",
    "years" : "2+ years of experience working at different startups",
    "email address" : "rwg5289@outlook.com",
    "name" : "Raghav Gupta",
    "phone" : "+1 8143845075",
    "resume" : "https://drive.google.com/file/d/15Rh3MWbIkvLTGp3LaNeormddyORZaqCP/view?usp=sharing",
    "position" : "Software Engineer",
    "referrer" : "Matched on AngelList and reached out by Jenny Gasparis",
    "source" : "https://github.com/RaghavGupta95/EMX",
    }
    if query in info:
        return info[query],200
    elif query == "puzzle":
        print "came"
        return puzzlesolver.solve_puzzle(description)
    else:
        return "400 Bad Request",400
    


        
"""
Define Init and configurations for flask

"""
if __name__ == '__main__':

    app.run(host='0.0.0.0',port=80, debug=True) #ssl_context=('cert.pem','key.pem'))
#     app.run(ssl_context='adhoc')
