from flask import Flask, render_template

app = Flask(__name__)

# Define a route to the home page
@app.route('/')
def home():
    # Data to be displayed dynamically on the web page
    dynamic_data = {
        'title': 'Dynamic Web Page',
        'content': 'This is a dynamic web page created using Python Flask.',
        'items_list': ['Item 1', 'Item 2', 'Item 3']
    }
    return render_template('index.html', data=dynamic_data)

if __name__ == '__main__':
    app.run(debug=True)
