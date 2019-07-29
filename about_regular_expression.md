Regular Expressions
A helpful article here
https://towardsdatascience.com/web-scraping-regular-expressions-and-data-visualization-doing-it-all-in-python-37a1aade7924
-------------------------------------

The basic idea of regular expressions is we define a pattern (the “regular expression” or “regex”) that we want to match in a text string and then search in the string to return matches. Some of these patterns look pretty strange because they contain both the content we want to match and special characters that change how the pattern is interpreted. Regular expressions come up all the time when parsing string information and are a vital tool to learn at least at a basic level!
There are 3 pieces of info we need to extract from the text table:
The names of the presidents
The names of the colleges
The salaries
First up is the name. In this regular expression, I make use of the fact that each name is at the start of a line and ends with a comma. The code below creates a regular expression pattern, and then searches through the string to find all occurrences of the pattern:
# Create a pattern to match names
name_pattern = re.compile(r'^([A-Z]{1}.+?)(?:,)', flags = re.M)
# Find all occurrences of the pattern
names = name_pattern.findall(content)

Like I said, the pattern is pretty complex, but it does exactly what we want! Don’t worry about the details of the pattern, but just think about the general process: first define a pattern, and then search a string to find the pattern.
We repeat the procedure with the colleges and the salary:
# Make school patttern and extract schools
school_pattern = re.compile(r'(?:,|,\s)([A-Z]{1}.*?)(?:\s\(|:|,)')
schools = school_pattern.findall(content)
# Pattern to match the salaries
salary_pattern = re.compile(r'\$.+')
salaries = salary_pattern.findall(content)

Unfortunately the salary is in a format that no computer would understand as numbers. Fortunately, this gives us a chance to practice using a Python list comprehension to convert the string salaries into numbers. The following code illustrates how to use string slicing, split , and join, all within a list comprehension to achieve the results we want:
# Messy salaries
salaries = ['$876,001', '$543,903', '$2453,896']
# Convert salaries to numbers in a list comprehension 
[int(''.join(s[1:].split(','))) for s in salaries]

[876001, 543903, 2453896]
We apply this transformation to our salaries and finally have the all info we want. Let’s put everything into a pandas dataframe. At this point, I manually insert the information for my college (CWRU) because it was not in the main table. It’s important to know when it’s more efficient to do things by hand rather than writing a complicated program (although this whole article kind of goes against this point!).

Subset of Dataframe
