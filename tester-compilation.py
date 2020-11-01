#!/usr/bin/python3 
import py_compile 
import tempfile 
import subprocess 
import asyncio 
import sys 

_, origine = tempfile.mkstemp() 
_, destination = tempfile.mkstemp() 

with open( origine, "w+b") as f:
    f.write(b"import os ; print( os.environ )")
    f.seek(0) 

py_compile.compile( 
	origine, 
	destination, 
	doraise=True 
)  

# with open( origine, "r") as f: 
# 	print( f.read() )

# with open( destination, "rb") as f: 
# 	print( f.read() )

async def get_date():
    code = 'import datetime; print(datetime.datetime.now())'

    # Create the subprocess; redirect the standard output
    # into a pipe.
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE
    )

    # Read one line of output.
    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()

    # Wait for the subprocess exit.
    await proc.wait()
    return line



async def e( d ): 
	cmd = sys.executable 
	proc = await asyncio.create_subprocess_exec( 
		"docker", 
			"run", 
			"-v", d+":/script.pyc", 
			"-e", "NOTHUS=1", 
			"python3-conteneur", 
				"python3", 
					"-I", 
					"-u", 
					"-X", "utf8", 
					"/script.pyc", 
		stdin=None, 
		env={ 
			# "PYTHONHOME": "/usr/lib/:/usr/include:/usr/bin", 
			# "PYTHONPATH": "/usr/lib/:/usr/include:/usr/bin", 
		}, 
		#stdout=asyncio.subprocess.PIPE, 
		#stderr=asyncio.subprocess.PIPE 
	) 

	stdout, stderr = await proc.communicate() 
	print("-->", stdout)

	print(f'[{cmd!r} exited with {proc.returncode}]')
	if stdout:
		print(f'[stdout]\n{stdout.decode()}')
	if stderr:
		print(f'[stderr]\n{stderr.decode()}')  

async def main(): 
	loop = asyncio.get_event_loop()

	taches = []
	for i in range(0, 10): 
		taches.append( loop.create_task( e( destination ) ) ) 

	await asyncio.wait( taches )

loop = asyncio.get_event_loop()
loop.run_until_complete( main() )
loop.close()



#print( asyncio.run( get_date() ) )  

#exit( 0 ) 
