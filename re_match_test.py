import re;
import sys;

fp=open(sys.argv[1]);
for line in fp:
	matchObj=re.findall(u"[\w.!#$%&*+'-/=?^_`{|}~\"\\]*@\w[\w.-]*\w\.\w[\w.-]*\w", line);
	if matchObj:
		print matchObj;


