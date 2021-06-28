def pv_update(storage):
  import yaml

  file_name = "pv-ebs.yml"

  stream = open(file_name, 'r')
  data = yaml.load(stream,Loader=yaml.FullLoader)

  data['spec']['capacity']['storage'] = str(storage) + 'Gi'

  with open(file_name, 'w') as yaml_file:
     yaml_file.write( yaml.dump(data, default_flow_style=False))