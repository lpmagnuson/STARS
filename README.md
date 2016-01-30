Analyzing Research Abstracts and Course Information for the STARS Report
========================================================================

The AASHE Sustainability Tracking, Assessment, and Rating System (STARS) Report
(https://stars.aashe.org/) requires the analysis of data from campus course offerings as well as research
output by faculty.

These scripts can be used to perform keyword lookups across courses and research output.

####Course Analysis
Download course information as a .csv file.  The script expects the course description to be in the 7th column of the spreadsheet (column G in Excel).
Use the LOWER excel function to transform the field to lower case, as matching by keyword in the script is case sensitive.  Perform a search and replace to replace all phrases with the phrase using a % instead of a space (e.g., public health becomes public%health).  Save the file as coursesv.csv.
You may need to adjust the script to return the information you want - by default, the script returns all fields per line and adds a column at the end with the list of keyword matches found.

Run the script using python courses.py.

To find the count of keywords (in order to find the courses that have the most keywords, and thus are likely most relevant to sustainability) in the adjacent column, add this Excel Formula:  

=SUM(LEN(G2)-LEN(SUBSTITUTE(G2,",","")),1)

This formula counts the commas in the field and adds 1, so that a row with 0 commas (1 word) will be counted as 1.

####Research Analysis

Perform an 'Organizational-Enhanced' search in Web of Science to retrieve research by your institution.  Save the results to your marked list (limited to 500 articles at a time) and export the marked records as tab-delimited text:

![Marked List Export Settings](https://raw.githubusercontent.com/lpmagnuson/STARS/master/WOSrecords/WOS_Field_Export.png)

Combine the file into one large tab-delimited text file.  Perform a search and replace to replace all potential phrase matches with % (e.g., public health becomes public%health).  Save this file as combinedrecs.csv.

Run research.py.  The resulting file is research_output.txt.

Open this file in Excel and use text-to-columns to distribute all of the authors into their own column.  Do a find and replace to replace spaces in author names with % (e.g., Smith, J becomes Smith%J).

Create a list of current faculty at your institution using the same format (e.g., Smith%J,Doe%J. and replace the word_list value in authors.py.

Run authors.py.  This will result in an tab-delimited text file of all research articles identifying the faculty you are searching for.





