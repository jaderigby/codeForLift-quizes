import sys, action, status, helpers
import one
# [ new import hook ]

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

if action == 'status' or action == None:
	status.execute()

elif action == 'action':
	# You will want to change the name to something specific, when developing
	action.execute()

elif action == "1":
    one.execute(action)
# [ new action hook ]

else:
	print
	print("- {} - is not a recognized action.".format(action))
	print
