# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from datascience_template_pieces import part_1_up_to_resources, part_2_up_to_courses, part_3_up_to_tools, part_4_up_to_videos, part_5
#import pyperclip

def convert_courses_to_table(df):
    # Setup table headers
    html = '<table class="table">\n\t<thead>\n\t<tr>\n'
    
    # Add table headers
    headers = ['Instructor', 'Title', 'Designation', 'University', 'Year', '']
    for head in headers:
        html += '\t\t<th>' + head + '</th>\n'
    
    # Close headers
    html += '\t</tr>\n\t</thead>\n'
    
    # Begin rows
    html += '\t<tbody class="list">\n'
    
    # Add Rows
    for index,doc in df.iterrows():
        html += '\t\t<tr>\n'
        html += '\t\t\t<td class="author">' + doc['Instructor Last'] + '</td>\n'            
        html += '\t\t\t<td class="title"><span  title=\'' + doc['Course Name'] + '\' class="booktitle"><a href=\'' + doc['Website'] + '\' target="_blank">' + doc['Course Name'] + '</a></span></td>\n'        
        html += '\t\t\t<td class="designation">' + doc['Course Designation'] + '</span></td>\n'        
        html += '\t\t\t<td class="university">' + doc['University'] + '</span></td>\n'
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
    headers = ['Author', 'Name', 'Topic', 'Year', '']
    for head in headers:
        html += '\t\t<th>' + head + '</th>\n'
    
    # Close headers
    html += '\t</tr>\n\t</thead>\n'
    
    # Begin rows
    html += '\t<tbody class="list">\n'
    
    # Add Rows
    for index,doc in df.iterrows():
        html += '\t\t<tr>\n'
        html += '\t\t\t<td class="author">' + doc['Author'] + '</td>\n'
            
        if doc['Free']=='Yes':
            html += '\t\t\t<td class="title"><span  title=\'' + doc['Name'] + '\' class="booktitle"><a href=\'' + doc['Link'] + '\' target="_blank">' + doc['Name'] + '</a></span></td>\n'
        else:
            html += '\t\t\t<td class="title">' + doc['Name'] + '</td>\n'
        
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
        html += '\t\t<tr>\n'          
        html += '\t\t\t<td class="name"><span title=\'' + doc['Name'] + '\' class="booktitle"><a href=\'' + doc['Link'] + '\' target="_blank">' + doc['Name'] + '</a></span></td>\n'        
        html += '\t\t\t<td class="topic">' + doc['Topic'] + '</td>\n'  
        html += '\t\t\t<td class="description">' + doc['Description'] + '</span></td>\n'        
        html += '\t\t</tr>\n'
    
    # End Rows and table
    html += '\t</tbody>\n</table>\n'
    
    return html

def convert_videos_to_table(df):
    # Setup table headers
    html = '<table class="table">\n\t<thead>\n\t<tr>\n'
    
    # Add table headers
    headers = ['Author', 'Organization', 'Name', 'Description']
    for head in headers:
        html += '\t\t<th>' + head + '</th>\n'
    
    # Close headers
    html += '\t</tr>\n\t</thead>\n'
    
    # Begin rows
    html += '\t<tbody class="list">\n'
    
    # Add Rows
    for index,doc in df.iterrows():
        html += '\t\t<tr>\n'
        html += '\t\t\t<td class="author">' + doc['Author'] + '</td>\n'
        html += '\t\t\t<td class="organization">' + doc['Organization'] + '</td>\n'            
        html += '\t\t\t<td class="name"><span class="booktitle"><a href=\'' + doc['Link'] + '\' target="_blank">' + doc['Name'] + '</a></span></td>\n'        
        html += '\t\t\t<td class="description">' + doc['Description'] + '</span></td>\n'        
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
        html += '\t\t<tr>\n'           
        html += '\t\t\t<td class="name"><span class="booktitle"><a href=\'' + doc['Link'] + '\' target="_blank">' + doc['Name'] + '</a></span></td>\n'        
        html += '\t\t\t<td class="description">' + doc['Description'] + '</span></td>\n'        
        html += '\t\t</tr>\n'
    
    # End Rows and table
    html += '\t</tbody>\n</table>\n'
    
    return html

filename = 'Data Science Resources 20191018.xlsx'

courses = pd.read_excel(filename, sheet_name="Courses")
html_courses = convert_courses_to_table(courses)

references = pd.read_excel(filename, sheet_name="References")
html_references = convert_references_to_table(references)

tools = pd.read_excel(filename, sheet_name="Tools")
html_tools = convert_tools_to_table(tools)

videos = pd.read_excel(filename, sheet_name="Videos")
html_videos = convert_videos_to_table(videos)

data = pd.read_excel(filename, sheet_name="Data")
html_data = convert_data_to_table(data)


f = open('datascience.html','w')
f.write(part_1_up_to_resources)
f.write(html_references)
f.write(part_2_up_to_courses)
f.write(html_courses)
f.write(part_3_up_to_tools)
f.write(html_tools)
f.write(part_4_up_to_videos)
f.write(html_videos)
f.write(part_5)
f.close()