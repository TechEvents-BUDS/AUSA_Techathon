import google.generativeai as genai

# Configure Gemini API
API_KEY = "AIzaSyByMgx2PkLsFJs_4RHeo3S4h1B6gZllJrM"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

def query_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")  # This specifies the model
    response = model.generate_content(prompt)  # Sends the prompt to Gemini
    return response.text  # Returns the generated content

# Example usage
prompt = '''
Many people find it hard to manage their health for a variety of reasons, such as ignoring small symptoms until they escalate, not knowing which doctor to consult, or struggling to maintain healthy habits like proper exercise, diet, or stress management. This becomes particularly challenging for individuals with chronic diseases like diabetes, high blood pressure, or mental health issues, who require consistent guidance and monitoring.
Based on this, how can people improve their health management habits and overcome these challenges? Please provide practical solutions, focusing on managing symptoms, consulting the right medical professionals, and maintaining a healthier lifestyle
'''
response = query_gemini(prompt)
print(response)