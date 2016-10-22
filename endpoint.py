import requests,json
from requests.auth import HTTPBasicAuth
import subprocess
import os,sys,time,re

##Global varibales
token_id='MAOGMZMGNJN2Q1OWZJOD'
token_pass='YzNhNTc0MDAwNjU0YjNjMTRjYmM5M2JmMzI2MDI2'
ENDURL='https://api.plivo.com/v1/Account/'+token_id+'/Endpoint/'

class plivo:
	def create_endpoint(self,username, password, alias):

		code='failed'
		# Create an Endpoint
		params = {
	    	'username': username,
	    	'password': password,
	    	'alias': alias
			}
		headers = {"Content-Type":"application/json"}
		response = requests.post(ENDURL, data=json.dumps(params),auth=HTTPBasicAuth(token_id, token_pass), headers=headers)
		print response.text
		#print response.status_code
		if response.status_code==201:
		    print '%s endpoint created successfull'%(username)
		    code='success'
		return code

#./sipp -sf UAC_UE1.xml -i 10.0.2.15 -p 5060 52.9.254.123:5060 -m 1 -trace_msg
#usage sipp_client_uas 1.xml sipp_client_uac 2.xml
	def startsipp(self,*scripts):
	    listtorun=list(scripts)
	    returncodes =[]
	    subprocessid=[]
	    storepid=[]
	    sipppids=[]
	    onlybash=[]
	    counter=0
	    xmlname=[]
            alloutputs=[]
	    cumulativereturncode=1
	    sipp_client_path='/root/Plivo/'
	    for each in listtorun:
	     if(each.find('xml')!=-1):
		continue
	     else:  
              print 'GOING TO START SIPP NOW ...'
              uacproc = 0
              print 'Running the command nohup %s%s %s &' %(sipp_client_path,listtorun[counter],listtorun[counter+1])
              uacproc = subprocess.Popen('%s%s %s' %(sipp_client_path,listtorun[counter],listtorun[counter+1]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
              subprocessid.append(uacproc)
              storepid.append(str(uacproc.pid))
              onlybash.append(listtorun[counter + 1])
              xmlname.append(listtorun[counter + 1])
              time.sleep(1)
              os.system('pgrep -P %s > ./Pid.txt' %(str(uacproc.pid)))
              objectread = open(r'./Pid.txt', 'r')
              readingpid = objectread.readlines()
              objectread.close()
              counter = counter + 2
	      try:
               removingendline = readingpid[0].split('\n')
               sipppids.append(removingendline[0])
              except Exception as e:
	       print 'Exception found during getting the PID =%s'%(e.message)
            print 'All the Sipp Process ID\'s are %s' %(str(sipppids))
            print 'Started all the scipts now going to wait for all of them to end'
            while ((len(subprocessid)) != 0): 
                 counter = 0
                 for each in subprocessid:
                   x = ''
                   x = each.poll()
                   if (x == None):
                      pass
                      time.sleep(1)
                   else:
                      returncodes.append(x)
                      if (int(x) > 0):
                          print 'The script %s has failed with the error code as %s' %(onlybash[counter], str(x))
                      del subprocessid[counter]
                      del onlybash[counter]
                      break
                   counter = counter + 1   
            checkcounter = 0             
            time.sleep(2)
	    for i in range(0, len(storepid)):
                  output = ''
                  outputerror =''
                  actualscriptname = []
                  actualscriptname = xmlname[i].split('.xml')
		  print actualscriptname 
                  print 'Reading the trace screen file -> %s%s_%s_screen.log' %(sipp_client_path,str(actualscriptname[0]), str(sipppids[i]))
                  if (int(returncodes[i]) == 0):
                     try: 
                        objectread = open(r'%s%s_%s_screen.log' %(sipp_client_path, str(actualscriptname[0]), str(sipppids[i])), 'r')
                     except IOError:
                        print 'There is some problem in opening the sipp log file'
                     output = objectread.read()
                     objectread.close()
                     alloutputs.append(output) 
                     print '\n#####################################   THIS IS THE OUTPUT FOR SIPP NO %s ###############################\n\n%s\n\n' %(str(i), str(output)) 
                  elif (int(returncodes[i]) > 0):
                     print 'The sipp script fails hence reading both the screen as well as error file'
                     try:
                        objectread = open(r'%s%s_%s_screen.log' %(sipp_client_path, str(actualscriptname[0]), str(sipppids[i])), 'r')
                     except IOError:
                        print'There is some problem in opening the sipp log file'
                     output = objectread.read()
                     objectread.close()
                     alloutputs.append(output)
                     try: 
                        objectread = open(r'%s%s_%s_errors.log' %(sipp_client_path, str(actualscriptname[0]), str(sipppids[i])), 'r')
                     except IOError:
                        print 'There is some problem in opening the sipp log file'
                     outputerror = objectread.read()
                     objectread.close()
                     alloutputs.append(outputerror)

                     print '\n#####################################   THIS IS THE OUTPUT FOR SIPP NO %s   #############################\n%s\n%s\n################################################ OUTPUT  ##############################################\n....' %(str(i), str(output), str(outputerror))
            for each in returncodes:
                   if (int(each) == 0):
                       pass
                   else:
                      checkcounter = checkcounter + 1
            if (int(checkcounter) == 0):
                  cumulativereturncode = 0
		  print 'Setting cumulativereturncode to 0'
            else:
                  cumulativereturncode = 1     
		  print 'Setting cumulativereturncode to 1'
 	    if (cumulativereturncode==0):
		print 'TEST PASSED'
	    else:
		print 'TEST FAILED'


################
obj=plivo()
######Created endpoint 1 using RESTAPI #######
#print obj.create_endpoint('testuser1', 'test123', 'TEST')
######Created endpoint 2 using RESTAPI #######
#print obj.create_endpoint('testuser2', 'test123', 'TEST')
##########Register and invite ######
#obj.startsipp('sipp_client_uac','UAC_UE1.xml','sipp_client_uas','UAS_UE2.xml')
#####Only Register############
obj.startsipp('sipp_client_uac','UAC_Register.xml','sipp_client_uas','UAS_Register.xml')
