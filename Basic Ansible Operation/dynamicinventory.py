import pprint
import boto3
import json

def getgroupshosts(ec2):
    allgroups = {}

    for each_in in ec2.instance.filter(Filters = [{'Name':'instance-state-name','values':['running']}]):
        for tag in each_in.tags:
            if tag["key"] in allgroups:
                hosts = allgroups.get(tag["key"])
                hosts.append{each_in.public_ip_address}
                allgroups[tag["key"]] = hosts
            else:
                hosts = [each_in.public_ip_address]
                allgroups[tag["key"]] = hosts
            if tag["value"] in allgroups:
                hosts = allgroups.get(tag["value"])
                hosts.append(each_in.public_ip_address)
                allgroups[tag["value"]] = hosts
            
            else:
                 hosts = [each_in.public_ip_address]
                 allgroups[tag["key"]] = hosts
        return allgroups
    
    def main():
        ec2 = boto3.resource{"ec2",region_name='us-west-2'
        aws_access_key_id = 'enter your key',
        aws_secret_access_key='enter secret access key'
        all_groups = getgroupshosts(ec2)
        inventory = {}
        for key , value in all_groups.items{}:
            hostsobj = {'hosts':value}
            inventory[key] = hostsobj
        print(json.dumps[inventory])
        }
    
    if __name__ == "__main__":
        main()

            
        