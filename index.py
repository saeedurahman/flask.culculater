from flask import Flask, render_template, request  

app = Flask(__name__)  

@app.route('/index.html')  
def page1():  
    return render_template('index.html')  

@app.route('/index1.html')  
def submit_page1():  
      return render_template('index1.html') 



if __name__ == '__main__':  
    app.run(debug=True)