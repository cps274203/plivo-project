# plivo-project


1.	Create two endpoints(sip) in the created account.For help, screenshots of UI are attached.

Creation of two endpoints is also automated using RESTAPI. You just need to call below two object to create the endpoint:-
```sh
obj=plivo()
######Created endpoint 1 using RESTAPI #######
#print obj.create_endpoint('testuser1', 'test123', 'TEST')
######Created endpoint 2 using RESTAPI #######
#print obj.create_endpoint('testuser2', 'test123', 'TEST')
```

```sh
Program Output:-
[root@localhost ~]# python2.7 endpoint.py
{
  "alias": "TEST",
  "api_id": "78969e48-9677-11e6-8535-02a2d2e31b81",
  "endpoint_id": "16030689688102",
  "message": "created",
  "username": "testuser1161020034415"
}
testuser1 endpoint created successful
success
{
  "alias": "TEST",
  "api_id": "7e17dc56-9677-11e6-8ede-02ed609bd62b",
  "endpoint_id": "16762838484775",
  "message": "created",
  "username": "testuser2161020034424"
}
testuser2 endpoint created successful
success
[root@localhost ~]#
```

Python code:-endpoint.py
`
import requests,json
from requests.auth import HTTPBasicAuth

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
		    print '%s endpoint created successful'%(username)
		    code='success'
		return code



################
obj=plivo()
print obj.create_endpoint('testuser1', 'test123', 'TEST')
print obj.create_endpoint('testuser2', 'test123', 'TEST')

`

2.	Register these two SIP endpoints.
I have created a sipp scripts and automated it using python. 
Sipp scripts:- UAC_Register.xml and UAS_Register.xml

We just need to call the below object to run the scenario
`
Python code:-endpoint.py
###############
obj=plivo()
#####Only Register############
obj.startsipp('sipp_client_uac','UAC_Register.xml','sipp_client_uas','UAS_Register.xml')
`

########
```sh
Program output:-
[root@localhost Plivo]# python2.7 endpoint.py
GOING TO START SIPP NOW ...
Running the command nohup /root/Plivo/sipp_client_uac UAC_Register.xml &
GOING TO START SIPP NOW ...
Running the command nohup /root/Plivo/sipp_client_uas UAS_Register.xml &
All the Sipp Process ID's are ['7764', '7768']
Started all the scipts now going to wait for all of them to end
['UAC_Register', '']
Reading the trace screen file -> /root/Plivo/UAC_Register_7764_screen.log

#####################################   THIS IS THE OUTPUT FOR SIPP NO 0 ###############################

------------------------------ Scenario Screen -------- [1-9]: Change Screen --
  Timestamp: Sat Oct 22 03:13:49 2016

  Call-rate(length)   Port   Total-time  Total-calls  Remote-host
  10.0(0 ms)/1.000s   5062       8.69 s            1  52.9.254.123:5060(UDP)

  Call limit reached (-m 1), 0.000 s period  0 ms scheduler resolution
  0 calls (limit 240)                    Peak was 1 calls, after 0 s
  0 Running, 2 Paused, 0 Woken up
  0 dead call msg (discarded)            1 out-of-call msg (discarded)
  1 open sockets

                                 Messages  Retrans   Timeout   Unexpected-Msg
       Pause [   4000ms]         1                             0
    REGISTER ---------->         1         0         0
         401 <----------         1         0         0         0
    REGISTER ---------->         1         0         0
         200 <----------  E-RTD1 1         0         0         0
         200 <----------         0         0         0         0
       Pause [   4000ms]         1                             0
------- Waiting for active calls to end. Press [q] again to force exit. -------

----------------------------- Statistics Screen ------- [1-9]: Change Screen --
  Start Time             | 2016-10-22   03:13:41.2740821477086221.274082
  Last Reset Time        | 2016-10-22   03:13:49.9739191477086229.973919
  Current Time           | 2016-10-22   03:13:49.9743651477086229.974365
-------------------------+---------------------------+--------------------------
  Counter Name           | Periodic value            | Cumulative value
-------------------------+---------------------------+--------------------------
  Elapsed Time           | 00:00:00:000000           | 00:00:08:700000
  Call Rate              |    0.000 cps              |    0.115 cps
-------------------------+---------------------------+--------------------------
  Incoming call created  |        0                  |        0
  OutGoing call created  |        0                  |        1
  Total Call created     |                           |        1
  Current Call           |        0                  |
-------------------------+---------------------------+--------------------------
  Successful call        |        0                  |        1
  Failed call            |        0                  |        0
-------------------------+---------------------------+--------------------------
  Response Time 1        | 00:00:00:000000           | 00:00:04:474000
  Call Length            | 00:00:00:000000           | 00:00:08:475000
------- Waiting for active calls to end. Press [q] again to force exit. -------

---------------------------- Repartition Screen ------- [1-9]: Change Screen --
  Average Response Time Repartition 1
           0 ms <= n <        10 ms :          0
          10 ms <= n <        20 ms :          0
          20 ms <= n <        30 ms :          0
          30 ms <= n <        40 ms :          0
          40 ms <= n <        50 ms :          0
          50 ms <= n <       100 ms :          0
         100 ms <= n <       150 ms :          0
         150 ms <= n <       200 ms :          0
                   n >=      200 ms :          1
  Average Call Length Repartition
           0 ms <= n <        10 ms :          0
          10 ms <= n <        50 ms :          0
          50 ms <= n <       100 ms :          0
         100 ms <= n <       500 ms :          0
         500 ms <= n <      1000 ms :          0
        1000 ms <= n <      5000 ms :          0
        5000 ms <= n <     10000 ms :          1
                   n >=    10000 ms :          0
------- Waiting for active calls to end. Press [q] again to force exit. -------




['UAS_Register', '']
Reading the trace screen file -> /root/Plivo/UAS_Register_7768_screen.log

#####################################   THIS IS THE OUTPUT FOR SIPP NO 1 ###############################

------------------------------ Scenario Screen -------- [1-9]: Change Screen --
  Timestamp: Sat Oct 22 03:13:50 2016

  Call-rate(length)   Port   Total-time  Total-calls  Remote-host
  10.0(0 ms)/1.000s   5060       8.57 s            1  52.9.254.123:5060(UDP)

  Call limit reached (-m 1), 0.000 s period  0 ms scheduler resolution
  0 calls (limit 240)                    Peak was 1 calls, after 0 s
  0 Running, 2 Paused, 0 Woken up
  0 dead call msg (discarded)            0 out-of-call msg (discarded)
  1 open sockets

                                 Messages  Retrans   Timeout   Unexpected-Msg
       Pause [   4000ms]         1                             0
    REGISTER ---------->         1         0         0
         401 <----------         1         0         0         0
    REGISTER ---------->         1         0         0
         200 <----------  E-RTD1 1         0         0         0
         200 <----------         0         0         0         0
       Pause [   4000ms]         1                             0
------- Waiting for active calls to end. Press [q] again to force exit. -------

----------------------------- Statistics Screen ------- [1-9]: Change Screen --
  Start Time             | 2016-10-22   03:13:42.3309221477086222.330922
  Last Reset Time        | 2016-10-22   03:13:50.9107661477086230.910766
  Current Time           | 2016-10-22   03:13:50.9109221477086230.910922
-------------------------+---------------------------+--------------------------
  Counter Name           | Periodic value            | Cumulative value
-------------------------+---------------------------+--------------------------
  Elapsed Time           | 00:00:00:000000           | 00:00:08:580000
  Call Rate              |    0.000 cps              |    0.117 cps
-------------------------+---------------------------+--------------------------
  Incoming call created  |        0                  |        0
  OutGoing call created  |        0                  |        1
  Total Call created     |                           |        1
  Current Call           |        0                  |
-------------------------+---------------------------+--------------------------
  Successful call        |        0                  |        1
  Failed call            |        0                  |        0
-------------------------+---------------------------+--------------------------
  Response Time 1        | 00:00:00:000000           | 00:00:04:448000
  Call Length            | 00:00:00:000000           | 00:00:08:451000
------- Waiting for active calls to end. Press [q] again to force exit. -------

---------------------------- Repartition Screen ------- [1-9]: Change Screen --
  Average Response Time Repartition 1
           0 ms <= n <        10 ms :          0
          10 ms <= n <        20 ms :          0
          20 ms <= n <        30 ms :          0
          30 ms <= n <        40 ms :          0
          40 ms <= n <        50 ms :          0
          50 ms <= n <       100 ms :          0
         100 ms <= n <       150 ms :          0
         150 ms <= n <       200 ms :          0
                   n >=      200 ms :          1
  Average Call Length Repartition
           0 ms <= n <        10 ms :          0
          10 ms <= n <        50 ms :          0
          50 ms <= n <       100 ms :          0
         100 ms <= n <       500 ms :          0
         500 ms <= n <      1000 ms :          0
        1000 ms <= n <      5000 ms :          0
        5000 ms <= n <     10000 ms :          1
                   n >=    10000 ms :          0
------- Waiting for active calls to end. Press [q] again to force exit. -------




Setting cumulativereturncode to 0
TEST PASSED
[root@localhost Plivo]#
```


3.	Make a call from one endpoint to second endpoint.
4.	Answer the call from second endpoint to first one.
5.	In both the case ie calling and receiving(and intermediate state like calling, ringing etc) all data and state should be printed to the console or log.
6.	Once the call is done, print all the call details like caller, recipient, duration etc.

When I am making a call (Endpoint 1 to Endpoint 2), it say “SIP/2.0 480 Temporarily Unavailable for the End point 2  user”.
Even I tried using two real softphone (Xlite and linphone).I observed the same behaviour. 
Note: I am using my office laptop to automated the callflow, and may be due to IT/admin issue , calls are not getting connected. However register is successful.
 
Once I have the successful call ( End to End call), I can easily get the caller , recipient, duration etc. and I can print the same after the the sip logs file.
XML for End_point1(who is dialing):- UAC_UE1.xml
XML for End_point2(who is receiving):- UAS_UE2.xml

The logic is already implemented in endpoint.py, We just need to call the below object:-
`
Python code:-endpoint.py
################
obj=plivo()
##########Register and invite ######
obj.startsipp('sipp_client_uac','UAC_UE1.xml','sipp_client_uas','UAS_UE2.xml') 
