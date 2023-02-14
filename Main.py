from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import docx2txt
import fitz
from nltk.tokenize import WhitespaceTokenizer

#converts doc format to text
resume_docx = docx2txt.process("resume.docx")
#print(resume_docx)

#converts pdf format to text
reader = fitz.open('myresume.pdf')
for page in reader:
    resume_pdf=page.get_text()

#takes the job description word document in a text format
job_description= docx2txt.process("JD.docx")
#print(job_description)

#takes the texts in a list
text_docx= [resume_docx,job_description]
text_pdf=[resume_pdf,job_description]

#giving vectors to the words
cv = CountVectorizer()
count_docx = cv.fit_transform(text_docx)
count_pdf=cv.fit_transform(text_pdf)

#print(count)
#print(text)

#using the alogorithm, finding the match between the resume/cv and job description
similarity_score_docx = cosine_similarity(count_docx)
match_percentage_docx= round((similarity_score_docx[0][1]*100),2)
similarity_score_pdf= cosine_similarity(count_pdf)
match_percentage_pdf= round((similarity_score_pdf[0][1]*100),2)
print(f'match percentage with the resume word document {match_percentage_docx}')
print(f'match percentage with the resume pdf document {match_percentage_pdf}')
