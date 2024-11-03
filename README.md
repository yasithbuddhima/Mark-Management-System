# Mark Management System

#### Video Demo:   [Watch Here](https://youtu.be/W47pEsDMp1o)
#### Visit Site: [Click Here](https://markmanagementsystem1-mfnhggum.b4a.run/)
#### Description:
This project is a web application that allows teachers to manage mark sheets effectively. 
It offers features such as add , edit , view marks , calculate percentage and download the full marksheet as a Excel file.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
    - [Add Marks](#1--add-marks)
    - [Edit Marks](#2-edit-marks)
    - [View Marks](#3-view-marks)
    - [Calculate Percentage](#4-calculate-percentage)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yasithbuddhima/Mark-Management-System.git
```
2. Navigate to the project directory:
```bash
 cd Mark-Management-System
```
3. Install dependencies:
```bash
pip install -r requirments.txt
```

## Usage
To run the application, 

execute:
```bash
flask run
```
then you will see
```
 * Debug mode: off
 * INFO: WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```


### or
execute:
```bash
python app.py
```
then you will see
```
 * Serving Flask app 'app'
 * Debug mode: off
 * INFO: WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://<your-ip-address>:5000
```

#### To visit the site Ctrl + click the link



## Features
### 1.  Add Marks
1. go to   Add Mark  
2. select the subject
3. Quickly add the marks from given number pad
   - In the Green box you will see the previous marks
   - Input field you can see the current student that you can enter the mark
   - For 0 marks or Absent use the 0 button
   - For 100 marks use 100 button

> [!IMPORTANT]
> You Should quickly type the mark or it will auto submit the wrong mark .
> you can edit marks later



### 2. Edit Marks
`There are two ways to change marks`

1. Through Homepage
    - Click Edit Marks
    - Enter the student Id 
    - Then you can see the Full details about the student
    - Select the subject
    - Enter the new mark 
    - Click the Edit Marks button

2. Through Marksheet
    - There is a button in last column of every row
    - Select the correct button in the correct row
    - Click it
    - Then you will see the full details about the student
    - Fill the new mark and the subject
    - Click the Edit Marks button
### 3. View Marks

- Click the View Marks on homepage
- You will see the complete marksheet
- Top 3 places will be highlighted
    1. <sup> st</sup> place `#ffc107` (Yellow)
    2. <sup> nd</sup> place `#198754` (Green)
    3. <sup> rd</sup> place  `#0dcaf0` (Blue / cyan)
- You can download the Marksheet as an Excel file from  clicking the button above the table

### 4. Calculate Percentage
- Go to the calculate the percentage section
- Enter the Number of subject
- Click calculate button 
- Then enter the marks and hit Enter


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License 
####  [MIT](https://choosealicense.com/licenses/mit/)
Copyright 2024 yasithbuddhima 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
