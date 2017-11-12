# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import pyperclip

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
            
        html += '\t\t\t<td class="title"><span class="booktitle"><a href=' + doc['Website'] + ' target="_blank">' + doc['Course Name'] + '</a></span</td>\n'
        
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

filename = 'Course Review 20171109.xlsx'

courses = pd.read_excel(filename)
html_references = convert_courses_to_table(courses)

pyperclip.copy(html_references)

