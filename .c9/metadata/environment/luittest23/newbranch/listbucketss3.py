{"filter":false,"title":"listbucketss3.py","tooltip":"/luittest23/newbranch/listbucketss3.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":3},"action":"remove","lines":["\"\"\"","Your module description","\"\"\""],"id":1},{"start":{"row":0,"column":0},"end":{"row":19,"column":25},"action":"insert","lines":["#%%","","# list S3 Buckets","","import boto3","","s3 = boto3.client('s3')","","#%%","","response = s3.list_buckets()","","#%%","","buckets = response[\"Buckets\"]","","#%%","","for bucket in buckets:","    print(bucket[\"Name\"])"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":19,"column":25},"end":{"row":19,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1693960276065,"hash":"debcf413beb5ad2a7b6ed5b4179eee88384e176a"}