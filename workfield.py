import boto3

class Vista:

    def region(self):
        client = boto3.client('ec2')
        response = client.describe_regions(
            #AllRegions = True
        ).get('Regions')
        regions = [] #this list should be populated from frontend
        for i in response:
            regions.append(i['RegionName'])
        return self.ec2(regions) # We need to select the API to call based on the input form user.
    def ec2(self, regions):
        instances = []
        for i in regions:
            print(i)
            client = boto3.client('ec2', region_name=i)
            response=client.describe_instances().get('Reservations')
            for i in response:
               instances.append(i['Instances'])
        return instances
    def vpc(self, regions):
        print('test')


com = Vista()
ec2 = com.region()
print(ec2)




