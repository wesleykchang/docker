import argparse
from dataclasses import asdict
import yaml

import boilerplate
from containers import containers


compose = boilerplate.compose_boilerplate.copy()

parser = argparse.ArgumentParser()
parser.add_argument('containers', nargs='+', help='list of desired containers')
args = parser.parse_args()

desired_containers = tuple(args.containers)
target_containers = tuple(
    filter(lambda c: c.container_name in desired_containers, containers)
)
volumes = dict()

for container in target_containers:        
    compose['services'][container.container_name] = {}
    compose["services"][container.container_name] = asdict(container)

    volume = container.volume_declaration()

    for vol in volume:
        volumes[vol] = None

compose["volumes"] = volumes

# Force yaml to interpret None as empty string - this is needed for the volumes
yaml.SafeDumper.add_representer(
    type(None),
    lambda dumper, value: dumper.represent_scalar(u'tag:yaml.org,2002:null', '')
  )


with open("docker-compose.yaml", "w") as f:
    yaml.safe_dump(compose, f, sort_keys=False, default_flow_style=False)
