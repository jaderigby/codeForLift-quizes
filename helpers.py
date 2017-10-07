import json, os, datetime
from os.path import expanduser
from settings import settings

profilePath = settings['profile_url'] + settings['profile']

def load_profile():
	return json.loads(read_file(profilePath))

def get_settings():
	profile = load_profile()
	return profile['settings']

def read_file(FILEPATH):
	FILE = open(FILEPATH, 'r')
	data = FILE.read()
	FILE.close()
	return data

def write_file(FILEPATH, DATA):
	FILE = open(FILEPATH, 'w')
	FILE.write(DATA)
	FILE.close()

# def read_json(FILEPATH):
# 	return json.loads(read_file(FILEPATH))
#
# def write_json(FILEPATH, DATA):


def print_to_scorecard(ACTION, ELEM, TOTAL):
	home = expanduser("~")
	filePath = home + '/Desktop/scorecard.md'
	if not os.path.isfile(filePath):
		write_file(filePath, 'NAME: {}\n'.format(raw_input("Please enter your name: ")))
	oldData = read_file(filePath)
	s = '''
quiz: {quiz}
date: {date}
score: {points}/{possible}
'''.format(quiz = ACTION, date = datetime.datetime.now().strftime("%m/%d/%Y"), points = ELEM, possible = TOTAL)
	newData = oldData + s
	write_file(filePath, newData)
