Test blind command injection
on target box
ping IP
on kali box
tcpdump -i tun0

Msfdb run - start db and run msfconsole

You can use this: $(!!) to recompute (not re-use) the output of the last command.
  Example: cp `!!` .
  
  when ifconfig is not available, use ip addr, or sbin/ifconfig

Script to check every SMB vulnerability 
for vul in $(find / -name smb*vuln*.nse | cut -d"/" -f 6); do nmap -v -p 139,445 --script=$vul -iL smb_server_all.txt -oN smb_vulns_$vul.txt; done 

Always use full path to execute something 

SNIFF SMB version ngrep -i -d tap0 's.?a.?m.?b.?a.*[[:digit:]]' & smbclient -L [IP] 