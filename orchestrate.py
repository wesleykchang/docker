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
volumes = list()

for container in target_containers:        
    compose['services'][container.container_name] = {}
    compose["services"][container.container_name] = asdict(container)
    volumes.extend(container.volume_declaration())

compose["volumes"] = volumes

with open("docker-compose.yaml", "w") as f:
    yaml.dump(compose, f, sort_keys=False)
