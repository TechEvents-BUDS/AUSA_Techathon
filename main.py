from flask import Flask, request, jsonify, render_template
from gemini_api import query_gemini
from database import save_user_data, fetch_user_data

app = Flask(__name__, static_folder='static', template_folder='templates')  # Corrected to use __name__

@app.route('/')
def home():
    # This will render the index.html file from the templates folder
    return render_template('index.html')

@app.route('/analyze_symptoms', methods=['POST'])
def analyze_symptoms():
    try:
        # Ensure that the request has the correct JSON body
        data = request.json
        symptoms = data.get('symptoms')
        
        if not symptoms:
            return jsonify({"error": "Symptoms not provided"}), 400
        
        # Query Gemini API for advice based on the symptoms
        response = query_gemini(f"Analyze these symptoms: {symptoms}")
        
        # Return the response from Gemini API
        return jsonify({"advice": response})
    
    except Exception as e:
        # Handle errors and return error message
        return jsonify({"error": str(e)}), 500

@app.route('/save_health_data', methods=['POST'])
def save_health_data():
    try:
        data = request.json
        # Save the data in the database
        save_user_data(data)
        return jsonify({"message": "Data saved successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_health_data/<user_id>', methods=['GET'])
def get_health_data(user_id):
    try:
        user_data = fetch_user_data(user_id)
        if not user_data:
            return jsonify({"error": "User data not found"}), 404
        return jsonify(user_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':  # Corrected to use __name__
    app.run(debug=True)
