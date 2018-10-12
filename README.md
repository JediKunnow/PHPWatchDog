# PHPWatchDog
Python 2.7 script to monitor Webserver pages avaiability. Supports SMTP mail alerts avaliable.

<center><h2>Documentation:</h2></center>
<center><h3>Features</h3></center>
<ul>
  <li>Check avaliabilty of web pages using requests.</li>
  <li>Support SMTP to send alert emails to the admin</li>
  <li>Multiple pages, even fully websites can be monitored by one process.</li>
  <li>The delay time between each check can be easy configured.</li>
  <li>JSON configuration file, user-friendly enough.</li
</ul>
    <center><h3>Structure:</h3></center>
  <ul>
    <li><strong>PHPWatchDog/</strong> - Main folder</li>
    <li><strong>PHPWatchDog/PHPWatchDog.cfg</strong> - Configuration file</li>
    <li><strong>PHPWatchDog/PHPWatchDog.py</strong> - Python script</li>
    <li><strong>PHPWatchDog/PHPWatchDog.log</strong> - Log file</li>
    <li><strong>PHPWatchDog/PHPWD.sh</strong> - Persistent start on Unix / Linux </li>
  </ul>
    
   <br><br><strong>The file is JSON formatted. Please <a target="_blank" href="https://www.w3schools.com/js/js_json_syntax.asp">read more about it</a> if you don't know JSON Syntax.</strong><br>
  <table>
  <tr><td align="middle" colspan="2"><strong>Configuration File</strong></td></tr>
    <tr>
      <th>Property name</th>
      <th>Description</th> 
    </tr>
    <tr>
      <td>services</td>
      <td>list of addresses of the web pages you want to monitor. Ex: https://github.com</td>
    </tr>
    <tr>
      <td>log</td>
      <td>log file path</td>
    </tr>
    <tr>
      <td>delay</td>
      <td>delay between each check, it must be expressed in seconds. Ex: 180 /* 3 minutes */</td>
    </tr>
    <tr>
      <td><a href="#smtp">smtp</td>
      <td>SMTP configuration array ( see below ) </td>
    </tr>
    <tr>
      <td>debug</td>
      <td>If "True" debug messages will be prompted on the console.</td>
    </tr>
  </table>
    
  <table id="smtp">
    <tr><td colspan="2" align="middle"><strong>SMTP Array description</strong></td></tr>
  <tr><th>Property name</th><th>Description</th></tr>
  <tr>
    <td>enable</td>
    <td>If "True" alerts emails will be sent to the address(es) specified.</td>
  </tr>
  <tr>
    <td>auth</td>
    <td>If "True" Authentication will be enabled.</td>
  </tr>
  <tr>
    <td>user</td>
    <td>User for the smtp auth</td>
  </tr>
  <tr>
    <td>psw</td>
    <td>Password for the smtp auth</td>
  </tr>
  <tr>
    <td>addr</td>
    <td>Address of smtp server</td>
  </tr>
  <tr>
    <td>port</td>
    <td>Port of smtp server</td>
  </tr>
  <tr>
    <td>sender_address</td>
    <td>The email address from which emails will be sent</td>
  </tr>
  <tr>
    <td>recipient_addresses</td>
    <td>Array of addresses to send the email to. If you need to send the email to only one address, use an array with one element.</td>
    </tr>
    <tr>
      <td>subject</td>
      <td>The subject of the email</td>
    </tr>
    <tr>
      <td>ssl</td>
      <td>If "True" SSL will be enabled. If you're using gmail set it on "True"</td>
    </tr>
    <tr>
      <td>msg</td>
      <td>The email message to send to the user. If you want to edit this be careful about the binding values (ex: %s)</td>
    </tr>
    <tr>
      <td>debug</td>
      <td>If "True" print libsmtp debug on console.</td>
    </tr>
  </table>
