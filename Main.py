from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import docx2txt
import fitz


resume_docx = docx2txt.process("resume.docx")
#print(resume_docx)

reader = fitz.open('myresume.pdf')
for page in reader:
    resume_pdf=page.get_text()

job_description= docx2txt.process("JD.docx")
#print(job_description)
text_docx= [resume_docx,job_description]
text_pdf=[resume_docx,job_description]

cv = CountVectorizer()
count_docx = cv.fit_transform(text_docx)
count_pdf=cv.fit_transform(text_pdf)

#print(count)
#print(text)

similarity_score_docx = cosine_similarity(count_docx)
match_percentage_docx= round((similarity_score_docx[0][1]*100),2)
similarity_score_docx = cosine_similarity(count_docx)
match_percentage_pdf= round((similarity_score_docx[0][1]*100),2)
print(match_percentage_docx)
print(match_percentage_pdf)
