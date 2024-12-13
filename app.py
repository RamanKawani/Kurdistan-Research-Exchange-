from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from models import db, Research

# App setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Initialize database
db.init_app(app)

# Routes
@app.route('/')
def index():
    researches = Research.query.all()
    return render_template('index.html', researches=researches)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        description = request.form['description']
        file = request.files['file']

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            new_research = Research(title=title, author=author, description=description, filepath=filepath)
            db.session.add(new_research)
            db.session.commit()
            flash('Research uploaded successfully!', 'success')
            return redirect(url_for('index'))

    return render_template('upload.html')

@app.route('/research/<int:id>')
def research_details(id):
    research = Research.query.get_or_404(id)
    return render_template('research_details.html', research=research)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure database tables are created
    app.run(debug=True)
