from flask import Flask, jsonify, request, render_template
import random
from email_Sender import *
from flask_cors import CORS
import os
# from werkzeug.utils import secure_filename
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity


def sendOTP(email):
    OTP = str(random.randint(100000,999999))
    send_otp_email(email,OTP)
    return OTP


app = Flask(__name__,template_folder="templates")
CORS(app)  # Enable CORS for all routes


@app.route("/")
def defaultPage():
    return render_template("index.html")


@app.route('/api/login', methods=['POST'])
def login():
    try:
        # Assuming the data is sent as JSON in the request body.
        data = request.get_json()

        # Retrieve id from the data.
        user_id = data.get('user_id')
        user_pass = data.get('user_pass')

        flag = 0
        # in the if statement below check data with the db
        if user_id == 'k213218@nu.edu.pk' and user_pass == 'pass123':
            flag = 1

        return jsonify(flag)
    
        # getOTP = sendOTP(user_id)

        # # Return the validation flag as a response.
        # return jsonify(getOTP)

    except Exception as e:
        print(f'Exception during request: {e}')
        return jsonify({'error': 'Internal Server Error'}), 500
    

@app.route('/api/signup_attempt', methods=['POST'])
def signup_attempt():
    try:
        # Assuming the data is sent as JSON in the request body.
        data = request.get_json()

        # Retrieve id from the data.
        user_email = data.get('user_email')
        
        getOTP = sendOTP(user_email)

        # Return the OTP and check it within the JS file.
        return jsonify(getOTP)

    except Exception as e:
        print(f'Exception during request: {e}')
        return jsonify({'error': 'Internal Server Error'}), 500


@app.route('/api/signup_success', methods=['POST'])
def signup_success():
    try:
        # Assuming the data is sent as JSON in the request body.
        data = request.get_json()

        # Retrieve id from the data.
        user_name = data.get('user_name')
        user_email = data.get('user_email')
        user_pass = data.get('user_pass')
        c_id = data.get('c_id')


        # enter the user_id and user_pass into the db
        # if db successful then return 1 else 0
        return jsonify(1)

    except Exception as e:
        print(f'Exception during request: {e}')
        return jsonify({'error': 'Internal Server Error'}), 500



UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/view/teacher_view", methods=['GET'])
def teacher_view():
    return render_template("TeacherView.html")

@app.route("/view/teacher_view/uploadData", methods=["POST"])
def upload_data():
    try:
        course_code = request.form.get('courseCode')
        student_id = request.form.get('studID')
        project_title = request.form.get('projectTitle')

        if 'report' not in request.files or 'code' not in request.files:
            return jsonify({"error": "Both report and code files are required"}), 400

        report_file = request.files['report']
        code_file = request.files['code']

        if report_file.filename == '' or code_file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        # Upload files to DB or save to disk
        # report_file.save("uploads/" + report_file.filename)
        # code_file.save("uploads/" + code_file.filename)

        return jsonify({"message": "Files uploaded successfully",
                        "courseCode": course_code,
                        "studID": student_id,
                        "projectTitle": project_title}), 200

    except Exception as e:
        print(f"Exception during file upload: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route("/view/teacher_view/checkPlag", methods=["POST"])
def check_plag():
    try:
        course_code = request.form.get('courseCode')
        student_id = request.form.get('studID')
        project_title = request.form.get('projectTitle')

        if 'report' not in request.files or 'code' not in request.files:
            return jsonify({"error": "Both report and code files are required"}), 400

        report_file = request.files['report']
        code_file = request.files['code']

        if report_file.filename == '' or code_file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        # Retrieve files from DB
        # check plag

        return jsonify({"message": "Files uploaded successfully",
                        "courseCode": course_code}), 200

    except Exception as e:
        print(f"Exception during file upload: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/view/teacher_view/pastProj', methods=['GET'])
def past_projects():
    try:
        # Get the list of files in the specified directory
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({'files': files})
    except Exception as e:
        print(f'Error retrieving files: {e}')
        return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)