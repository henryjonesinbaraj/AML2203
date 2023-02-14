from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import docx2txt

resume = docx2txt.process("resume.docx")
#print(resume)
job_description= docx2txt.process("JD.docx")
#print(job_description)
text = [resume,job_description]
cv = CountVectorizer()
count = cv.fit_transform(text)

#print(count)
#print(text)

similarity_score = cosine_similarity(count)
match_percentage= round((similarity_score[0][1]*100),2)
#print(match_percentage)
