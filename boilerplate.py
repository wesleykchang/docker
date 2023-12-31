"""Enums to enforce unique usb IDs, IPs, and ports."""

from aenum import Enum, unique
from dataclasses import dataclass, field
from typing import Union


DOCKERHUB_REPO = 'steingartlab/easi'
NETWORK_IP = '192.168.0'
NETWORK_NAME = 'acoustics-network'


@unique
class Usb(Enum):
    pulser = 0
    printer = 1
    mux = 2

@unique
class IP(Enum):
    mux = 21
    picoscope = 10
    pithy = 9
    printer = 22
    pulser = 11
    remotecontrol = 13
    sfogliatella = 12
    unplugged = 15
    ustreamer_horizontal = 14
    ustreamer_vertical = 16

@unique
class Port(Enum):
    """Pithy is not here bc it's a double edge case:
    1) multiple IPs bindings, and 2) doesn't do A:A binding but A:B.
    """

    mux = 9020
    picoscope = 5001
    printer = 9021
    pulser = 9002
    remotecontrol = 9003
    sfogliatella = 9696
    unplugged = 9001
    ustreamer_vertical = 8080
    ustreamer_horizontal = 8081


@dataclass
class Container:
    container_name: str
    image: str
    networks: Union[str, int]
    ports: list = field(default_factory=list)
    volumes: list = field(default_factory=list)
    environment: list = field(default_factory=list)
    privileged: bool = True
    tty: bool = True
    stdin_open: bool = True


    def __post_init__(self):
        self.image = f'{DOCKERHUB_REPO}:{self.image}'
        networks = {}
        networks[NETWORK_NAME] = {}
        networks[NETWORK_NAME]["ipv4_address"] = f'{NETWORK_IP}.{self.networks}'
        self.networks = networks

    def volume_declaration(self):
        """Parses volumes to be used in docker-compose.yaml.
        
        Note that it does not include volumes that are mounted from the host.

        Returns:
            list: list of volumes to be used in docker-compose.yaml
        """
        volumes = list()
        
        for volume in self.volumes:
            volume_containerside = volume.split(':')[0]

            if volume_containerside[0] == '/':
                if 'home' in volume_containerside:
                    volume_containerside = volume.split('/')[-2]
                    print(volume_containerside)
                else:
                    continue

            volumes.append(volume_containerside)

        return volumes

def parse_port(port: Port):
    return f'{port.value}:{port.value}'


compose_boilerplate = {
    "version": "3",
    "services": {},
    "volumes": {},
    "networks": {NETWORK_NAME: {"ipam": {"config": [{"subnet": f"{NETWORK_IP}.0/24"}]}}}
}

