import re;
import sys;

fp=open(sys.argv[1]);

for line in fp:
	matchObj=re.search('www\..*\.edu', line);
	if matchObj:
		print matchObj.group();


