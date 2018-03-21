# Intro to Hadoop and MapReduce from Udacity
I enrolled this course within the school course A0X36MOOC which is taught at CTU FEL

Scripts, that are listed in this github, written in Python 2.7 for Udacity course [Intro to Hadoop and MapReduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617).

The The Apache™ Hadoop® project develops open-source software for reliable, scalable, distributed computing. Learn the fundamental principles behind it, and how you can use its power to make sense of your Big Data.

## Lessons 
- Lesson 6: Project
  - Part 1 - Sales Data
    - Q1 - Sales per Category 
    - Q2 - Highest Sale
    - Q3 - Total Sales
  - Part 2 - Web Log Data
    - Q1 - Hits to Page
    - Q2 - Hits from IP
    - Q3 - Most Popular
- Lesson 7: MapReduce Design Patterns
  - Q1 - Filtering Exercise
  - Q2 - Top 10
  - Q3 - Inverted Index
  - Q4 - Finding Mean
  - Q5 - Combiners
  - Q6 - Combine Datasets
- Lesson 8: Project Prep
  - Q1 - Student Times
  - Q2 - Post and Answer Length
  - Q3 - Top Tags
  - Q4 - Study Groups

## Example Use
1. Download and run a virtual machine for this course
2. Download and unpack datasets into the virtual machine
3. Create a directory in hadoop HDFS
```
hadoop fs -mkdir myinput
```
4. Upload dataset into hadoop HDFS 
```
hadoop fs -put name_of_dataset myinput
```
5. Make mapper.py and reducer.py according to the Quiz questions
6. Run a mapreduce job 
```
hs mapper.py reducer.py myinput myoutput
```
7. Read results directly from the output file
```
hadoop fs -cat myoutput/part-00000
```
or if the file is too big to read, save output file
```
hadoop fs -get myoutput/part-00000 myoutputfile.txt
```
8. search for the answer to the Quiz questions
9. If the directory isn't needed in hadoop HDFS, delete the directory
```
hadoop fs -R myoutput
```