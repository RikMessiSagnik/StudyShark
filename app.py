from flask import Flask, render_template

app = Flask(__name__)
classes = {
    "Class 12": {

        "Mathematics": [
            {
                "name": "Relations and Functions",
                "image": "relations.png"
            },
            {
                "name": "Inverse Trigonometric Functions",
                "image": "inverse-trigonometry.png"
            },
            {
                "name": "Matrices",
                "image": "matrices.png"
            },
            {
                "name": "Determinants",
                "image": "determinants.png"
            },
            {
                "name": "Continuity and Differentiability",
                "image": "continuity.png"
            },
            {
                "name": "Application of Derivatives",
                "image": "derivatives.png"
            },
            {
                "name": "Integrals",
                "image": "integrals.png"
            }
        ],

        "Physics": [
            {
                "name": "Electric Charges and Fields",
                "image": "electric-charges.png"
            },
            {
                "name": "Electrostatic Potential and Capacitance",
                "image": "electrostatic-potential.png"
            },
            {
                "name": "Current Electricity",
                "image": "current-electricity.png"
            },
            {
                "name": "Moving Charges and Magnetism",
                "image": "moving-charges.png"
            },
            {
                "name": "Magnetism and Matter",
                "image": "magnetism.png"
            },
            {
                "name": "Electromagnetic Induction",
                "image": "electromagnetic-induction.png"
            },
            {
                "name": "Alternating Current",
                "image": "alternating-current.png"
            },
            {
                "name": "Electromagnetic Waves",
                "image": "electromagnetic-waves.png"
            }
        ],

        "Chemistry": [
            {
                "name": "Solutions",
                "image": "solutions.png"
            },
            {
                "name": "Electrochemistry",
                "image": "electrochemistry.png"
            },
            {
                "name": "Chemical Kinetics",
                "image": "chemical-kinetics.png"
            },
            {
                "name": "d and f Block Elements",
                "image": "d-f-block.png"
            },
            {
                "name": "Coordination Compounds",
                "image": "coordination.png"
            },
            {
                "name": "Haloalkanes and Haloarenes",
                "image": "haloalkanes.png"
            }
        ],

        "English": [
            {
                "name": "The Last Lesson",
                "image": "last-lesson.png"
            },
            {
                "name": "Lost Spring",
                "image": "lost-spring.png"
            },
            {
                "name": "Deep Water",
                "image": "deep-water.png"
            },
            {
                "name": "The Rattrap",
                "image": "rattrap.png"
            },
            {
                "name": "Indigo",
                "image": "indigo.png"
            },
            {
                "name": "Poets and Pancakes",
                "image": "poets-pancakes.png"
            }
        ],

        "Computer Science": [
            {
                "name": "Python Revision Tour",
                "image": "python.png"
            },
            {
                "name": "Functions",
                "image": "functions.png"
            },
            {
                "name": "Exception Handling",
                "image": "exception-handling.png"
            },
            {
                "name": "File Handling",
                "image": "file-handling.png"
            },
            {
                "name": "Data Structures",
                "image": "data-structures.png"
            },
            {
                "name": "Database Management",
                "image": "database.png"
            }
        ]
    }
}

@app.route('/')
def home():
    return render_template('home.html', classes=classes)

@app.route('/subject/<subject_name>')
def subject(subject_name):
    chapters = classes["Class 12"].get(subject_name)

    if chapters is None:
        return "Subject not found", 404

    return render_template(
        'subject.html',
        subject=subject_name,
        chapters=chapters
    )

@app.route('/subject/<subject_name>/<chapter_name>')
def chapter(subject_name, chapter_name):
    return render_template(
        'chapter.html',
        subject=subject_name,
        chapter=chapter_name
    )


if __name__ == '__main__':
    app.run(debug=True)