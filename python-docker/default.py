
import os 

print( "------" ) 

print("coucou !")

print( "------" ) 

print( os.environ ) 

print( "------" ) 

import os
mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
mem_gib = mem_bytes/(1024.**3) 

print( mem_gib )

print( "------" ) 

table = []
while True: 
	table.append( "a"*1000000 ) 
	print(len(table)) 

print( "------" ) 

print("fin !")

