import subprocess,sys
f,ct,key,d,sig,pol=sys.argv[1:7]
r=subprocess.run(['curl','-sS','-o','/dev/null','-w','%{http_code}','https://shopify-staged-uploads.storage.googleapis.com/','-F','Content-Type='+ct,'-F','success_action_status=201','-F','acl=private','-F','key='+key,'-F','x-goog-date='+d,'-F','x-goog-credential=merchant-assets@shopify-tiers.iam.gserviceaccount.com/'+d[:8]+'/auto/storage/goog4_request','-F','x-goog-algorithm=GOOG4-RSA-SHA256','-F','x-goog-signature='+sig,'-F','policy='+pol,'-F','file=@%s;type=%s'%(f,ct)],capture_output=True,text=True)
print(r.stdout,r.stderr)
