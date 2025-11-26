




skills = agent1_extract_skills(resume, job_desc)
gaps = agent2_find_gap(skills)
docs = agent3_rag_retrieve(gaps)
study_plan = agent4_generate_plan(docs, skills)
