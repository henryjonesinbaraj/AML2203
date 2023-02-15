from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import docx2txt
import fitz
from nltk.tokenize import WhitespaceTokenizer
import streamlit as st

def count_words(listy):
    counts=dict()
    for word in listy:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    count_keys=list(counts.keys())
    count_keys.sort()
    sorted_counts={item: counts[item] for item in count_keys}
    return sorted_counts
def pdf_to_txt(pdffile): #reference: https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/
    #https://discuss.streamlit.io/t/how-to-use-pymupdf-to-read-a-pdf-after-uploading-that-via-st-file-uploader/7268/6
    with fitz.open(stream=pdffile.read(),filetype='pdf') as doc:
        resume_pdf=""
        for page in doc:
            resume_pdf+=page.get_text()
        return resume_pdf
    
text_tokenizer= WhitespaceTokenizer()
# reference : https://stackoverflow.com/questions/47301795/how-can-i-remove-special-characters-from-a-list-of-elements-in-python
remove_characters= str.maketrans("", "", "±§!@#$%^&*()-_=+[]}{;'\:,./<>?|")
#takes the job description word document in a text format
job_description= docx2txt.process("JD.docx")
cv = CountVectorizer()

st.title("Best resume match finder")
file_docx=st.file_uploader("Upload you CV\Resume",type=["docx"])

if st.button("Submit"):
    if file_docx is not None:
        #converts doc format to text
        resume_docx = docx2txt.process(file_docx)
        #takes the job description word document in a text format
        job_description= docx2txt.process("JD.docx")
        #takes the texts in a list
        text_docx= [resume_docx,job_description]
        #creating the list of words from the word document
        words_docx_list = text_tokenizer.tokenize(resume_docx)
        #removing speacial charcters from the tokenized words 
        words_docx_list=[s.translate(remove_characters) for s in words_docx_list]
        print(count_words(words_docx_list))
        #giving vectors to the words
        count_docx = cv.fit_transform(text_docx)
        #using the alogorithm, finding the match between the resume/cv and job description
        similarity_score_docx = cosine_similarity(count_docx)
        match_percentage_docx= round((similarity_score_docx[0][1]*100),2)
        st.write(f'match percentage with the resume word document {match_percentage_docx}')
    else:
        pass

file_pdf=st.file_uploader("Upload you CV\Resume",type=["pdf"])
#converts pdf format to text
if st.button("Submit",key='1'):
    if file_pdf is not None:
        resume_pdf=pdf_to_txt(file_pdf)
        #takes the texts in a list
        text_pdf=[resume_pdf,job_description]
        #creating the list of words from the pdf document
        words_pdf_list = text_tokenizer.tokenize(resume_pdf)
        #removing speacial charcters from the tokenized words 
        words_pdf_list=[s.translate(remove_characters) for s in words_pdf_list]
        print(count_words(words_pdf_list))
        count_pdf=cv.fit_transform(text_pdf)
        similarity_score_pdf= cosine_similarity(count_pdf)
        match_percentage_pdf= round((similarity_score_pdf[0][1]*100),2)
        st.write(f'match percentage with the resume pdf document {match_percentage_pdf}')    
    else:
        pass
    

# #print(resume_docx)

# #takes the job description word document in a text format
# job_description= docx2txt.process("JD.docx")
# #print(job_description)

# #takes the texts in a list
# text_docx= [resume_docx,job_description]
# text_pdf=[resume_pdf,job_description]

# #creating the list of words from the word document
# text_tokenizer= WhitespaceTokenizer()
# words_docx_list = text_tokenizer.tokenize(resume_docx)
# #print(words_docx_list)

# #creating the list of words from the pdf document
# words_pdf_list = text_tokenizer.tokenize(resume_pdf)
# #print(words_pdf_list)


# #removing speacial charcters from the tokenized words 
# remove_characters= str.maketrans("", "", "±§!@#$%^&*()-_=+[]}{;'\:,./<>?|")
# words_pdf_list=[s.translate(remove_characters) for s in words_pdf_list]
# words_docx_list=[s.translate(remove_characters) for s in words_docx_list]

# # print(words_pdf_list)
# # print("===============================================")
# # print(words_docx_list)

# #counting number of each word in the list

# def count_words(listy):
#     counts=dict()
#     for word in listy:
#         if word in counts:
#             counts[word]+=1
#         else:
#             counts[word]=1
#     count_keys=list(counts.keys())
#     count_keys.sort()
#     sorted_counts={item: counts[item] for item in count_keys}
#     return sorted_counts


# print(count_words(words_pdf_list))
# print(count_words(words_docx_list))

# #giving vectors to the words
# cv = CountVectorizer()
# count_docx = cv.fit_transform(text_docx)
# count_pdf=cv.fit_transform(text_pdf)

# #print(count)
# #print(text)

# #using the alogorithm, finding the match between the resume/cv and job description
# similarity_score_docx = cosine_similarity(count_docx)
# match_percentage_docx= round((similarity_score_docx[0][1]*100),2)
# similarity_score_pdf= cosine_similarity(count_pdf)
# match_percentage_pdf= round((similarity_score_pdf[0][1]*100),2)
# st.write(f'match percentage with the resume word document match_percentage_docx}')
# st.write(f'match percentage with the resume pdf document match_percentage_pdf}')
