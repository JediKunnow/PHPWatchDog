# -*- coding: utf-8 -*-
"""
@Author: Kunnow
@Description: PHP Service WatchDog
@date: 12/10/18
@license: GNU General Public License v3.0
@version 1.0.0

"""

import urllib
import json
import smtplib
import sched, time
import datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class PHPWatchDog:
    
    config_path = "PHPWatchDog.cfg";
    log_path = "PHPWatch.log"; # Default one if not specified in configs
    error = False;
    delay = float();
    debug = bool();
    
    def __init__(self):
        self.cfg = dict();
        self.services = dict();
        if not self._LoadConfig():
            self.error = True;
        
    
    def _LoadConfig(self):
        try:
            with open(self.config_path,'r') as json_file:
                
                self.cfg = json.load(json_file);
                
                if self.cfg['log'] == "True":
                    self.log_path = self.cfg['log'];
                    
        except Exception as e:
            self.printLog("[ERROR] Can't open config file. Exception: "+ str(e));
            return False;
        
        self.delay = float(self.cfg['delay']);
        self.services = self.cfg['services'];
        self.debug = self.cfg['debug'] == "True";
        return True;
                
    def _SendEmail(self,address,name):
        
        if self.cfg['smtp']['enable'] == "False":
            return;

        sender = self.rmComma(self.cfg['smtp']['sender_address']);
        #making email msg
        msg = MIMEMultipart();
        msg['From'] = sender;
        msg['To'] = address;
        msg['Subject'] = self.cfg['smtp']['subject'] % name;
        msg.attach(MIMEText(self.cfg['smtp']['msg'] % (name,str(self.getTime()))));
    
        try:
                        
            if self.cfg['smtp']['ssl'] == "True":
                smtp_server = smtplib.SMTP_SSL(self.cfg['smtp']['addr'],int(self.cfg['smtp']['port']));
            else:
                smtp_server = smtplib.SMTP(self.cfg['smtp']['addr'],self.rmComma(str(self.cfg['smtp']['port'])));
                
            smtp_server.ehlo()
            
            if self.cfg['smtp']['auth'] == "True":        
                smtp_server.login(self.cfg['smtp']['user'], self.cfg['smtp']['psw']);
            if self.cfg['smtp']['debug'] == "True":
                smtp_server.set_debuglevel(1);
            smtp_server.sendmail(sender,address,msg.as_string());
            smtp_server.quit();
            
            self.printLog("[SMTP] Email sent TO: { " + address + " } FROM: { "+self.cfg['sender_address'] + " }");
            print("\n[SMTP] Email sent TO: { " + address + " } FROM: { "+ address + " }");
        except:
            return;
            
    def _ServiceOnline(self,srv,name):
        
        try:
            result = urllib.urlopen(srv).read();
            if len(result) == 0:
                return 0;
        except:
            print("\n[ERROR][" + name + "] Can't check for service status. Please provide a valid service_url in the configuration file.");
            return -1;
        return 1;
    
    def test(self):
        if self.debug:
            print("\n[CHECK START]");
        self.printLog("[CHECK START]");
        for name,service in self.services.iteritems():
            self.printLog("\t["+name+"] New check on: " + service + " At: " + str(self.getTime()));
            if self.debug:
                print("\n["+name+"] New check on: " + service + " At: " + str(self.getTime()));
            sOnline = self._ServiceOnline(service,name);
            if sOnline == 0: # To do: make service_online return type int
			
                if self.cfg['smtp']['enable'] == "True":
                    for s in self.cfg['smtp']['recipient_addresses']:
                        self._SendEmail(s,name);
                        print("["+ name + "][PHP ERROR]PHP stop working or went through an exception.");
				
                if self.cfg['smtp']['enable'] == "True" and self.debug:
                    print("\n[SMTP]An email was sent to the user.");
				
                self.printLog("[RESULT] ERROR - PHP FAILURE");
                
            elif sOnline == 1:
                self.printLog("[RESULT] OK");
                if self.debug:
                    print("\n[RESULT] OK");
        if self.debug:	
            print("\n[CHECK END]");
        self.printLog("[CHECK END]");
                
    def getTime(self):
        return datetime.datetime.now();
    
    def printLog(self,msg):
        with open(self.log_path, 'a') as f:
                f.write("\n"+msg);

    def rmComma(self,stri):
        return stri.replace(",","");


sched = sched.scheduler(time.time, time.sleep)
php = PHPWatchDog();
if php.error:
    print("\n[ERROR]Cannot read the config file.");
    exit();

def start(sc):
    php.test();
    sched.enter(php.delay, 1, start, (sc,));

print("[START] PHPWatchDog started at [ " + str(php.getTime()) + " ]");
php.printLog("[START] PHPWatchDog started at [ " + str(php.getTime()) + " ]" );
php.test();
sched.enter(php.delay, 1, start, (sched,));
sched.run();
    
    

    
