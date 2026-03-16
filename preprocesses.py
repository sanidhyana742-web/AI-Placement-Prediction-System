import pandas as pd

FEATURES = [
'cgpa','backlogs','coding_skills','dsa_score','aptitude_score',
'communication_skills','ml_knowledge','system_design','internships',
'projects_count','certifications','hackathons','open_source_contributions',
'extracurriculars','salary_package_lpa','branch_CSE','branch_Chemical',
'branch_ECE','branch_EE','branch_IT','branch_ME',
'college_tier_Tier-2','college_tier_Tier-3'
]

def prepare_input(data):
    df = pd.DataFrame([data])
    return df[FEATURES]