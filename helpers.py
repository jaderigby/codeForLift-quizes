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

def write_json(FILEPATH, DATA):
	FILE = open(FILEPATH, 'w')
	data = json.dumps(DATA, sort_keys=True, indent=4)
	FILE.write(data)
	FILE.close()

def print_to_scorecard(ACTION, ELEM, TOTAL):
	home = expanduser("~")
	filePath = home + '/Documents/codeForLift-quizes/profiles/profile.py'
	settings = get_settings()
	print("settings: ".format(settings))
	if settings['name'] == "":
		settings['name'] = raw_input("Please enter your name: ")
	newObj = {}
	newObj['quiz'] = ACTION
	newObj['date'] = datetime.datetime.now().strftime("%m/%d/%Y")
	newObj['score'] = "{}/{}".format(ELEM, TOTAL)
	settings['codeForLift']['quizes'].append(newObj)
	write_json(filePath, settings)
