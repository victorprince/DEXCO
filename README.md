# DEXCO



## WHY DEXCO?
Due to the current pandemic situation,it has become a difficult job for
teachers to correct answer papers as the exams have turned online
,its pretty difficult to correct the answer scripts for descriptive
exams.This has led to the decrease of class tests as it takes a lot of
effort to correct an answer script submitted online.This was the prime
motivation which led me to this project,"DEXCO".
This program will be a great help for the evaluation of theoretical subjects like History,English etc

## WHAT IS DEXCO
DEXCO is a program which is capable of correcting answer
scripts(pdf) both handwritten as well as printed texts.This program
can recognize,the handwriting of a student and can even check for grammatical mistakes.

## HOW DOES DEXCO WORK?
When we submit an answer sheet to this software along with a text
file containing the keywords of each answer and marks along side.
#### NB(In the keyword file,the question number should be followed by the keyword and the mark,it can be written in anyway(1 when 4,2-overtones-4 etc) .The mark which should be reduced for grammatical erros should be given last if not given,by default 0.25 marks is reduced.)
After each answer the character "#" should be given, so that
the program can recognize the end of an answer.
The program then splits the pdf to multiple images,recognizes the handwriting,checks for grammar and gives marks, after that images
will get automatically deleted.The user can view a small graph which
shows the mark distribution.

#### For image recognition google's cloud vision API is used.

## REQUIREMENTS
Install the required python libraries using the package manager [pip](https://pip.pypa.io/en/stable/).
Use the command
```bash
pip install -r requirements.txt
```

## HOW TO USE
Create an account in the [Google Cloud Vision API website](https://cloud.google.com/vision),download the auth token and paste the location of the auth token in the file DEXCO.py in the given line,
```
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"ENTER THE TOKEN FILE LOCATION HERE(JSON FILE,AUTH TOKEN)"
```


Now run the file 
```
python DEXCO.py
```

## CONTRIBUTING
This program has a lot of limitations due to the time limitations a lot of errors might have crept in feel free to 
pull requests . For major changes, please open an issue first to discuss what you would like to change.
A lot of grammatical errors will be there in this 'readme' extremely sorry for that.

Please make sure to update tests as appropriate.

## CONTACT
Use my Gmail id: ```victorprince2003@gmail.com```
