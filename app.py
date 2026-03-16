from flask import Flask, render_template, request
import joblib
import pandas as pd

def prepare_input(data):
    return pd.DataFrame([data])
app = Flask(__name__)

model = joblib.load("model/placement_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = {
        "cgpa": float(request.form["cgpa"]),
        "backlogs": int(request.form["backlogs"]),
        "coding_skills": int(request.form["coding_skills"]),
        "dsa_score": int(request.form["dsa_score"]),
        "aptitude_score": int(request.form["aptitude_score"]),
        "communication_skills": int(request.form["communication_skills"]),
        "ml_knowledge": int(request.form["ml_knowledge"]),
        "system_design": int(request.form["system_design"]),
        "internships": int(request.form["internships"]),
        "projects_count": int(request.form["projects_count"]),
        "certifications": int(request.form["certifications"]),
        "hackathons": int(request.form["hackathons"]),
        "open_source_contributions": int(request.form["open_source_contributions"]),
        "extracurriculars": int(request.form["extracurriculars"]),
        "salary_package_lpa": float(request.form["salary_package_lpa"]),
        "branch_CSE": int(request.form["branch_CSE"]),
        "branch_Chemical": int(request.form["branch_Chemical"]),
        "branch_ECE": int(request.form["branch_ECE"]),
        "branch_EE": int(request.form["branch_EE"]),
        "branch_IT": int(request.form["branch_IT"]),
        "branch_ME": int(request.form["branch_ME"]),
        "college_tier_Tier-2": int(request.form["tier2"]),
        "college_tier_Tier-3": int(request.form["tier3"])
    }

    input_data = prepare_input(data)
    prediction = model.predict(input_data)[0]

    result = "Placed 🎉" if prediction == 1 else "Not Placed ❌"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)