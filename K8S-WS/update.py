def pv_update(pv_file,volume_id,storage):
  import yaml

  # file_name = "pv-ebs.yml"

  stream = open(pv_file, 'r')
  data = yaml.load(stream,Loader=yaml.FullLoader)

  data['spec']['capacity']['storage'] = str(storage) + 'Gi'
  data['spec']['awsElasticBlockStore']['volumeID'] = volume_id

  with open(pv_file, 'w') as yaml_file:
     yaml_file.write( yaml.dump(data, default_flow_style=False))


def pvc_update(pvc_file,storage):
  import yaml

  # file_name = "pvc-ebs.yml"

  stream = open(pvc_file, 'r')
  data = yaml.load(stream,Loader=yaml.FullLoader)

  data['spec']['resources']['requests']['storage'] = str(storage) + 'Gi'

  with open(pvc_file, 'w') as yaml_file:
     yaml_file.write( yaml.dump(data, default_flow_style=False))


'''
volume_id=subprocess.getoutput("""aws ec2 describe-volumes --filters Name=tag-value,Values="Terraform-Value" --query "Volumes[0].VolumeId" """)

pv_update("pv-ebs.yml",volume_id,5)
pvc_update("pvc-ebs.yml",5)
'''
