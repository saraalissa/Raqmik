import subprocess,json,sys,time
# reads JSON list of [file, key, sig, policy, date]
items=json.load(open(sys.argv[1]))
for f,key,sig,pol,d in items:
    for k in range(4):
        r=subprocess.run(['python3','upp.py',f,'text/plain',key,d,sig,pol],capture_output=True,text=True).stdout.strip()
        if r.startswith('201'): break
        time.sleep(3)
    print(f,r)
