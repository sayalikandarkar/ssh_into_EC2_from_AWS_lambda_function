import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        print("object",object)
        print("key",key)
        print("txt",response['Body'].read().decode('utf-8'))
        
        const region = event.Records[0].awsRegion;
        var s3FileCommand = 'aws s3 cp s3://' + bucket + '/' + key + ' ./' + key + ' --region ' + region;
        var ssh = new SSH({
            host: 'ec2-13-233-49-98.ap-south-1.compute.amazonaws.com',
            user: 'ec2-user',
            key: fs.readFileSync("sayali.pem")
        });
        ssh.exec('cd /home/ec2-user/sayali_2').exec('ls -al', {
         out: function(stdout) {
            console.log('ls -al got:');
            console.log(stdout);
            console.log('now launching command');
            console.log(s3FileCommand);
         }
        }).exec('' + s3FileCommand, {
         out: console.log.bind(console),
         exit: function(code, stdout, stderr) {
             console.log('operation exited with code: ' + code);
             console.log('STDOUT from EC2:\n' + stdout);
             console.log('STDERR from EC2:\n' + stderr);
             context.succeed('Success!');
         }
        }).start();

        return response['ContentType']

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
            