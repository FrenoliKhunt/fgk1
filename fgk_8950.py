from flask import Flask, render_template, request
application = app = Flask(__name__)



#port = int(os.getenv("VCAP_APP_PORT"))
#port = os.getenv("VCAP_APP_PORT")

@app.route('/')
def home():
   return render_template('fgk_8950.html')


if __name__ == '__main__':
    app.run(debug=True)