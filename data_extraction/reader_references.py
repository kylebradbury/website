# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import pyperclip

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
            html += '\t\t\t<td class="title"><span class="booktitle"><a href=' + doc['Link'] + ' target="_blank">' + doc['Name'] + '</a></span></td>\n'
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

filename = 'Data Science Resources.xlsx'

resources = pd.read_excel(filename)
html_references = convert_references_to_table(resources)

pyperclip.copy(html_references)

