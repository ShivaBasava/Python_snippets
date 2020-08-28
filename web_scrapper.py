''''
This Snippet is used to Scrappe a website, which consists of various video clips of below mentiond video format types and to store the direct dowload links in an Excel document

Consider your 'base_url_' - www.google.com (example, which consists of various video clips of below mentiond video format types)
    
    file name (will get from link address's text) - someName.mp4

    Final format - DURL_ | someName.mp4
                    ----   -------- ----
                     ||     ||
    link.has_attr['href]   link.text                        

# install openpyxl
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd


DURL_file_frmat = input("Enter respective number for download file format from the below\n1] .avi\n2] .mp4\n3] .ogv\n4] .mkv\n")
vari_video_fmt = {"1": ".avi", "2": ".mp4", "3": ".ovg", "4": ".mkv"}

if (DURL_file_frmat == "1"):
    final_file_frmat = vari_video_fmt['1']
    
elif (DURL_file_frmat == "2"):
    final_file_frmat = vari_video_fmt['2']
    
elif (DURL_file_frmat == "3"):
    final_file_frmat = vari_video_fmt['3']
    
elif (DURL_file_frmat == "4"):
    final_file_frmat = vari_video_fmt['4']
    
else:
    print("Please select the available Number or include this file format in your menu list")
    exit()

base_url_ = 'YOUR_URL_for_Scrapping'
html_ = requests.get(base_url_)
bs = BeautifulSoup(html_.text, 'html.parser')
possible_links = bs.find_all('a')
temp = []
final_links = []

for link in possible_links:
    if link.has_attr('href'):      
        temp.append(link.attrs['href'] + " | " + link.text)

for i in temp:
    if final_file_frmat in i:
        final_links.append(base_url_ + "/" + i )

try:
    df = pd.DataFrame(final_links)  
    df.to_excel('Your_File_Name.xlsx', header=True, index=True)
    print("\nScrapping Success :)")
except Exception as e:
    print(e)
 
