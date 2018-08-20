#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 20:00:11 2018

@author: firefreezing
"""

#%%

from gensim.summarization import keywords
import pickle
from docx import Document
import os 
## read this to get more sense of it
##http://bdewilde.github.io/blog/2014/09/23/intro-to-automatic-keyphrase-extraction/

#%%
text1 = """The 2018 FIFA World Cup was the 21st FIFA World Cup, an international football \
tournament contested by the men's national teams of the member associations of FIFA once \
every four years. It took place in Russia from 14 June to 15 July 2018. It was the \
first World Cup to be held in Eastern Europe, and the 11th time that it had been \
held in Europe. At an estimated cost of over $14.2 billion, it was the most expensive World Cup. \
It was also the first World Cup to use the video assistant referee (VAR) system. \
The finals involved 32 teams, of which 31 came through qualifying competitions, \
while the host nation qualified automatically. Of the 32 teams, 20 had also appeared in \
the previous tournament in 2014, while both Iceland and Panama made their first appearances \
at a FIFA World Cup. A total of 64 matches were played in 12 venues across 11 cities. \
The final took place on 15 July at the Luzhniki Stadium in Moscow, between France and Croatia. \
France won the match 4–2 to claim their second World Cup title, marking the fourth consecutive \
title won by a European team."""


#%%
text2 ='''Challenges in natural language processing frequently involve \
speech recognition, natural language understanding, natural language \
generation (frequently from formal, machine-readable logical forms), \
connecting language and machine perception, dialog systems, or some \
combination thereof.'''


#%%
keywords(text1,split=True,ratio=1,scores=True,lemmatize=True)
#%%
def get_file_paths(folder_path):
    files = os.listdir(folder_path)
    files = [f for f in files if '.docx' in f]
    files = [f for f in files if not '~' in f]
    files_path = [os.path.join(folder_path,f) for f in files]

    return files,files_path

def read_doc(f_path):
    doc = Document(f_path)
    text_list = [p.text for p in doc.paragraphs if len(p.text)>0]#[3:]
    text_list = [p.replace('\xa0',' ') for p in text_list] # some clean up 
    text_list = [p for p in text_list if len(p.split()) > 15]
    text = ' '.join(text_list)
    return text

#%%

data_folder = '../data/IMFC Communiques'
file_names,files_path = get_file_paths(data_folder)
docs = [read_doc(f) for f in files_path]

#%%
docs[0]
#%%

keywords(docs[-2],split=True,ratio=0.5,scores=True,lemmatize=True)