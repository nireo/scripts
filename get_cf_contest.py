#!/usr/bin/python3

# Codeforces url's are formatted as: codeforces.com/contest/NUMBER/problem/LETTER
import sys
import requests
import os
import time
from bs4 import BeautifulSoup

# get the current directory so that we can create the competition file in there
start_time = time.time()
current_directory = os.path.dirname(os.path.realpath(__file__))
problem_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
# test url https://codeforces.com/contest/1422
url = str(sys.argv[1])

contest_number = url.split("/")
contest_number = contest_number[len(contest_number)-1]
print("Starting to get contest from url: ", url)

problems_count = 0
# first fetch the contest page
try:
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if 'problem' in href and 'problems' not in href:
            problems_count += 1

    # since every problem apperas twice as a link
    problems_count /= 2
except requests.exceptions.ConnectionError as exc:
    print(exc)

# Create a directory for the problem
path = os.path.join(current_directory, "C"+contest_number)
os.mkdir(path)

for i in range(int(problems_count)):
    os.system("cp ./cf_template.cpp ./C{}/{}.cpp".format(contest_number, problem_letters[i]))
    print("Created problem {}.cpp".format(problem_letters[i]))

print("Finished, took: {}".format(time.time() - start_time))
