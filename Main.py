from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import docx2txt
import fitz
from nltk.tokenize import WhitespaceTokenizer
import streamlit as st

text_tokenizer= WhitespaceTokenizer() # reference : https://stackoverflow.com/questions/47301795/how-can-i-remove-special-characters-from-a-list-of-elements-in-python
remove_characters= str.maketrans("", "", "±§!@#$%^&*()-_=+[]}{;'\:,./<>?|")
cv = CountVectorizer()

def pdf_to_txt(pdffile): #reference: https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/
    #https://discuss.streamlit.io/t/how-to-use-pymupdf-to-read-a-pdf-after-uploading-that-via-st-file-uploader/7268/6
    with fitz.open(stream=pdffile.read(),filetype='pdf') as doc:
        resume_pdf=""
        for page in doc:
            resume_pdf+=page.get_text()
        return resume_pdf

def docx_to_text(docxfile): #converts doc format to text
    jd_text_file=docx2txt.process(docxfile)
    return jd_text_file
    
def text_list_pdf(pdffile,docxfile): #takes the texts and creating the list with both documents
    text_pdf=[(pdf_to_txt(pdffile)), (docx_to_text(docxfile))]
    
def removecharcters(textfile):
    #creating the list of words from the word document
    words_list = text_tokenizer.tokenize(textfile)
    #removing speacial charcters from the tokenized words 
    words_list=[s.translate(remove_characters) for s in words_list]
    return words_list

def list_to_string(words_list): # converting list of words to string
    words= ' '.join(words_list)
    return words

def list_to_string1(listie): #converting first element of the list to string
    for item in range(1):
        text =listie[0]
        return text
    
def trimmed_text_docx(docx1): #trimming the text by removing speacial charcaters for the document
    document=docx_to_text(docx1)
    trim_list=removecharcters(document)
    trimming=list_to_string(trim_list)
    return trimming #gives list of words

def trimmed_text_pdf(docx1): #trimming the text by removing speacial charcaters for the pdf
    document=pdf_to_txt(docx1)
    trim_list=removecharcters(document)
    trimming=list_to_string(trim_list)
    return trimming #gives list of words
    
def trimmed_word_count(words_list): #removing speacial charcters from the tokenized words and counting the words
    trimmed_text_count = count_words(words_list)
    return trimmed_text_count
   
def best_match(textfile): #takes the texts and creating the list with both documents
    #giving vectors to the words
    word_count = cv.fit_transform(textfile)
    #using the alogorithm, finding the match between the resume/cv and job description
    similarity_score = cosine_similarity(word_count)
    match_percentage = round((similarity_score[0][1]*100),2)
    return match_percentage

def count_words(listy): # counting the each word count in the list of words
    counts=dict()
    for word in listy:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    count_keys=list(counts.keys())
    sorted_counts={item: counts[item] for item in count_keys}
    return sorted_counts



st.title("Nexus Resume Scorer")
st.write("Upload your resume/cv and the job description to get your resume score.\n ALL THE BEST !!")
 #takes the job description word document in a text format
file_jd_docx=st.file_uploader("Upload the Job Description [docx]",type=["docx"])
if st.button("Upload"):
    if file_jd_docx is not None:
        st.write("Job description uploaded successfuly. Now You can find the best match !!")
    

file_docx=st.file_uploader("Upload you CV\Resume [docx]",type=["docx"])

if st.button("Submit"):
    if file_docx is not None:
        text_docx=[trimmed_text_docx(file_docx),trimmed_text_docx(file_jd_docx)]
        resume_text=list_to_string1(text_docx)
        words_trimmed_list=removecharcters(resume_text)
        county_words=trimmed_word_count(words_trimmed_list)
        match_percentage_docx = best_match(text_docx)
        st.write(f'Match percentage with the resume word document {match_percentage_docx}')
        #st.write(county_words)
    else:
        pass

file_pdf=st.file_uploader("Upload you CV\Resume [pdf]",type=["pdf"])
#converts pdf format to text
if st.button("Submit",key='1'):
    if file_pdf is not None:
        #takes the texts and creating the list with both documents
        text_pdf=[trimmed_text_pdf(file_pdf),trimmed_text_docx(file_jd_docx)]
        resume_text= list_to_string1(text_pdf)
        words_trimmed_list=removecharcters(resume_text)
        county_words=trimmed_word_count(words_trimmed_list)
        match_percentage_pdf = best_match(text_pdf)
        st.write(f'Match percentage with the resume pdf document {match_percentage_pdf}')
        #st.write(county_words)  
    else:
        pass