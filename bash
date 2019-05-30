Msfdb run - start db and run msfconsole

You can use this: $(!!) to recompute (not re-use) the output of the last command.
  Example: cp `!!` .
  
  when ifconfig is not available, use ip addr, or sbin/ifconfig

Script to check every SMB vulnerability 
for vul in $(find / -name smb*vuln*.nse | cut -d"/" -f 6); do nmap -v -p 139,445 --script=$vul -iL smb_server_all.txt -oN smb_vulns_$vul.txt; done 
