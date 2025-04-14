from flask import Flask, render_template

app = Flask(__name__)

# You can modify this information about the dogs here
# Just change the text between the quotes to update the website
dogs = {
    'bella': {
        'name': 'Bella',
        'breed': 'Cavalier Spaniel',
        'age': '8 years old',
        'description': 'Bella loves to eat sleep and more!',
        'fun_fact': 'Bella can catch treats in the air sometimes',
        # Change this to the path of your image file for Bella
        'image_path': 'static/Bella.jpeg'
    },
    'jasper': {
        'name': 'Jasper',
        'breed': 'Cavalier Spaniel',
        'age': '2 years old',
        'description': 'Jasper likes to sunbathe eat pencils and more!',
        'fun_fact': 'Jasper knows that cookie means food!',
        # Change this to the path of your image file for Jasper
        'image_path': 'static/Jasper.jpeg'
    }
}

@app.route('/')
def home():
    return render_template('index.html', dogs=dogs)

if __name__ == '__main__':
    app.run(debug=True)