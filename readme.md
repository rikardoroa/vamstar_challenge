## Vamstar Challenge

###### This Backend Script uses Python V3.9 for the transformation of 1 million records randomly, also contains all the transformations associated to this test were using the following procedures as follows:


* 1 -> for the calculation of BMI it used the following formula: BMI(kg/m2) = mass(kg) / height(m), the implementation of that formula was used in the
 function **_data_gen_and_filtering_** in the script


* 2 -> the counting of total overweight and the others BMI category variables were found applying the function  **_bmi_category_count_** using pandas

* 3 -> the build test of this app, was developed using pytest library, it was created two files using pytest a html and xml files for the test results

* 4 --> the script was developed using oop approach

* 5 --> the main repository of this test is in this link: https://github.com/rikardoroa/vamstar_challenge

## Note
* to create an html file for the test results of this application, the following CLI command should be used: **_pytest myfile.py --html=HTML test Report.html_**

## Note
* If you Want to create a xml file, the following CLI command should be used:  **_pytest myfile.py -rA --junitxml="testReport.xml"_**

## Note
* for this test , it's necessary install this two python libraries: **_pytest and pytest-html_**


###### enjoy!
