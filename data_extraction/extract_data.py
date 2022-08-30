# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import shutil
import os

template = 'datascience_template.html'
outfile = 'datascience.html'
datafile = 'Data Science Resources 20220816.xlsx'
destination = '../'
replace = True

def convert_courses_to_table(df):
    # Setup table headers
    html = '<table class="table">\n\t<thead>\n\t<tr>\n'
    
    # Add table headers
    headers = ['Title', 'Instructor', 'Designation', 'University', 'Year', '']
    for head in headers:
        html += '\t\t<th>' + head + '</th>\n'
    
    # Close headers
    html += '\t</tr>\n\t</thead>\n'
    
    # Begin rows
    html += '\t<tbody class="list">\n'
    
    # Add Rows
    for index,doc in df.iterrows():
        if doc['Show']=='Yes':
            html += '\t\t<tr>\n'
            html += '\t\t\t<td class="title"><span  title=\'' + doc['Course Name'] + '\' class="booktitle"><a href=\'' + doc['Website'] + '\' target="_blank">' + doc['Course Name'] + '</a></span></td>\n'        
            html += '\t\t\t<td class="author">' + str(doc['Instructor Last']) + '</td>\n'            
            html += '\t\t\t<td class="designation">' + str(doc['Course Designation']) + '</span></td>\n'        
            html += '\t\t\t<td class="university">' + str(doc['University']) + '</span></td>\n'
            html += '\t\t\t<td class="year">' + str(doc['Year']) + '</td>\n'
            if doc['Starred']=='Yes':
                html += '\t\t\t<td class="starred"><i class="fa fa-star favorite" aria-hidden="true"></i></td>\n'
            else:
                html += '\t\t\t<td class="starred"></td>\n'
            html += '\t\t</tr>\n'
    
    # End Rows and table
    html += '\t</tbody>\n</table>\n'
    
    return html

def convert_references_to_table(df):
    # Setup table headers
    html = '<table class="table">\n\t<thead>\n\t<tr>\n'
    
    # Add table headers
    headers = ['Title', 'Author(s)', 'Topic', 'Year', '']
    for head in headers:
        html += '\t\t<th>' + head + '</th>\n'
    
    # Close headers
    html += '\t</tr>\n\t</thead>\n'
    
    # Begin rows
    html += '\t<tbody class="list">\n'
    
    # Add Rows
    for index,doc in df.iterrows():
        if doc['Show']=='Yes':
            html += '\t\t<tr>\n'
                
            if doc['Free']=='Yes':
                html += '\t\t\t<td class="title"><span  title=\'' + doc['Name'] + '\' class="booktitle"><a href=\'' + doc['Link'] + '\' target="_blank">' + doc['Name'] + '</a></span></td>\n'
            else:
                html += '\t\t\t<td class="title">' + doc['Name'] + '</td>\n'
            
            html += '\t\t\t<td class="author">' + doc['Author'] + '</td>\n'
            
            if pd.isnull(doc['Subcategory']):
                html += '\t\t\t<td class="category">' + doc['Category'] + '</span></td>\n'
            else:
                html += '\t\t\t<td class="category">' + doc['Category'] + ' - ' + str(doc['Subcategory']) + '</td>\n'
                
            html += '\t\t\t<td class="year">' + str(doc['Year']) + '</td>\n'
            
            if doc['Starred']=='Yes':
                html += '\t\t\t<td class="starred"><i class="fa fa-star favorite" aria-hidden="true"></i></td>\n'
            else:
                html += '\t\t\t<td class="starred"></td>\n'
            
            html += '\t\t</tr>\n'
    
    # End Rows and table
    html += '\t</tbody>\n</table>\n'
    
    return html

def convert_tools_to_table(df):
    # Setup table headers
    html = '<table class="table">\n\t<thead>\n\t<tr>\n'
    
    # Add table headers
    headers = ['Name', 'Topic', 'Description']
    for head in headers:
        html += '\t\t<th>' + head + '</th>\n'
    
    # Close headers
    html += '\t</tr>\n\t</thead>\n'
    
    # Begin rows
    html += '\t<tbody class="list">\n'
    
    # Add Rows
    for index,doc in df.iterrows():
        if doc['Show']=='Yes':
            html += '\t\t<tr>\n'          
            html += '\t\t\t<td class="name"><span title=\'' + str(doc['Name']) + '\' class="booktitle"><a href=\'' + str(doc['Link']) + '\' target="_blank">' + str(doc['Name']) + '</a></span></td>\n'        
            html += '\t\t\t<td class="topic">' + str(doc['Topic']) + '</td>\n'  
            html += '\t\t\t<td class="description">' + str(doc['Description']) + '</span></td>\n'        
            html += '\t\t</tr>\n'
    
    # End Rows and table
    html += '\t</tbody>\n</table>\n'
    
    return html

def convert_videos_to_table(df):
    # Setup table headers
    html = '<table class="table">\n\t<thead>\n\t<tr>\n'
    
    # Add table headers
    headers = ['Name', 'Author', 'Organization', 'Description']
    for head in headers:
        html += '\t\t<th>' + head + '</th>\n'
    
    # Close headers
    html += '\t</tr>\n\t</thead>\n'
    
    # Begin rows
    html += '\t<tbody class="list">\n'
    
    # Add Rows
    for index,doc in df.iterrows():
        if doc['Show']=='Yes':
            html += '\t\t<tr>\n'
            html += '\t\t\t<td class="name"><span class="booktitle"><a href=\'' + str(doc['Link']) + '\' target="_blank">' + str(doc['Name']) + '</a></span></td>\n' 
            html += '\t\t\t<td class="author">' + str(doc['Author']) + '</td>\n'
            html += '\t\t\t<td class="organization">' + str(doc['Organization']) + '</td>\n'            
            html += '\t\t\t<td class="description">' + str(doc['Description']) + '</span></td>\n'        
            html += '\t\t</tr>\n'
    
    # End Rows and table
    html += '\t</tbody>\n</table>\n'
    
    return html

def convert_data_to_table(df):
    # Setup table headers
    html = '<table class="table">\n\t<thead>\n\t<tr>\n'
    
    # Add table headers
    headers = ['Name', 'Description']
    for head in headers:
        html += '\t\t<th>' + head + '</th>\n'
    
    # Close headers
    html += '\t</tr>\n\t</thead>\n'
    
    # Begin rows
    html += '\t<tbody class="list">\n'
    
    # Add Rows
    for index,doc in df.iterrows():
        if doc['Show']=='Yes':
            html += '\t\t<tr>\n'           
            html += '\t\t\t<td class="name"><span class="booktitle"><a href=\'' + doc['Link'] + '\' target="_blank">' + doc['Name'] + '</a></span></td>\n'        
            html += '\t\t\t<td class="description">' + str(doc['Description']) + '</span></td>\n'        
            html += '\t\t</tr>\n'
    
    # End Rows and table
    html += '\t</tbody>\n</table>\n'
    
    return html


courses = pd.read_excel(datafile, sheet_name="Courses")
html_courses = convert_courses_to_table(courses)

references = pd.read_excel(datafile, sheet_name="References")
html_references = convert_references_to_table(references)

tools = pd.read_excel(datafile, sheet_name="Tools")
html_tools = convert_tools_to_table(tools)

videos = pd.read_excel(datafile, sheet_name="Videos")
html_videos = convert_videos_to_table(videos)

data = pd.read_excel(datafile, sheet_name="Data")
html_data = convert_data_to_table(data)


# Read in the file
with open(template, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('<!-- REFERENCES -->', html_references)
filedata = filedata.replace('<!-- COURSES -->', html_courses)
filedata = filedata.replace('<!-- TOOLS -->', html_tools)
# filedata = filedata.replace('<!-- VIDEOS -->', html_videos)

# Write the file out again
with open(outfile, 'w') as file:
  file.write(filedata)

if replace:
    shutil.copy(outfile,os.path.join(destination,outfile))