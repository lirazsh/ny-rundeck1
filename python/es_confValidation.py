import yaml, sys, getopt

#Config reference file
CONF = "/etc/ansible/global.config"

def es_validateConfig(argv):
	if len(argv) < 3:
		print "Not enough args provided. -h for help"
		return False

	try:
		opts, args = getopt.getopt(argv,"hv:t:")
	except getopt.GetoptError:
		print 'es_confValidation.py -v <es_version> -t <es_node_type>'
		return False
	
	for opt,arg in opts:
		if opt == '-h':
			print 'es_confValidation.py -v <es_version> -t <es_node_type>'
			return False
		elif opt in ("-v"):
			es_version = arg
		elif opt in ("-t"):
			es_role = arg.split(",")

	fd1 = open(CONF,"r")
	globalConfig = yaml.load(fd1)
	elasticConfig = globalConfig['Type']['Elastic']

	if not es_version in elasticConfig['Version']:
		print "Invalid version provided: %s. Current acceptable versions: %s \nPlease check %s" % (es_version,elasticConfig['Version'],CONF)
		return False
	
	for role in es_role:
		if not role in elasticConfig['Subtype']:
			print "Invalid elastic role provided: %s. Current acceptable roles: %s \nPlease check %s" % (es_role,elasticConfig['Subtype'],CONF)
			return False
	return True

if es_validateConfig(sys.argv[1:]):
	sys.exit(0)
else:
	sys.exit(1)
