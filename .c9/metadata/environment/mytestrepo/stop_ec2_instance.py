{"filter":false,"title":"stop_ec2_instance.py","tooltip":"/mytestrepo/stop_ec2_instance.py","ace":{"folds":[],"scrolltop":63,"scrollleft":0,"selection":{"start":{"row":5,"column":0},"end":{"row":5,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"5dc9dda23b28abf7afc263e304baa1c07b0e998a","mime":"text/x-script.python","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"remove","lines":["\"\""],"id":1},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["\""]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["Y"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["o"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["u"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["r"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":[" "]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["m"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["o"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["d"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["u"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["l"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["e"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":[" "]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["d"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["e"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["s"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["c"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["r"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["i"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["p"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["t"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["i"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["o"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["n"]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"remove","lines":["\"\""]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["\""]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":16,"column":68},"action":"insert","lines":["import boto3","","ec2 = boto3.client('ec2')","","dev_tag = { \"Key\":\"Environment\", \"Value\":\"Dev\"}","","response = ec2.describe_instances()","","reservations = response['Reservations']","","for reservation in reservations:","    instances = reservation['Instances']","","    for instance in instances:","        if (dev_tag in instance['Tags'] and 'running' in instance['State']['Name']):","            print(instance['InstanceId'])","            ec2.stop_instances(InstanceIds=[instance['InstanceId']])"]}]]},"timestamp":1694019424007}