from boilerplate import Container, IP, Port, Usb, parse_port


mux = Container(
    container_name='mux',
    image='nodeforwarder',
    ip=IP.mux.value,
    ports=[parse_port(Port.mux)],
    environment=[
        f'serial_port=/dev/ttyUSB{Usb.mux.value}',
        f'internet_port={Port.mux.value}',
        'baud_rate=9600'
    ],
    volumes=['/dev/:/dev/']
)

    
picoscope = Container(
    container_name='pico',
    image='pico',
    ip=IP.picoscope.value,
    ports=[parse_port(Port.picoscope)],
    volumes=[
        '/dev/:/dev/',
        'picoscope:/picoscope/'
    ],
)
    

pithy = Container(
    container_name='pithy',
    image='pithy',
    ip=IP.pithy.value,
    ports=['8001:8080', '8888:8888', '8004:8081'],  # Edge case so just doing manually
    volumes=[
        'docker.sock:/var/run/docker.sock',
        'code:/pithy/code/',
        'history:/pithy/code_stamped/',
        'passwd:/pithy/assets/',
        'files:/pithy/files/',
        'images:/pithy/images/',
        'drops:/pithy/drops/',
        '/home/lab/acoustics:/pithy/acoustics'
    ],
)
    

printer = Container(
    container_name='printer',
    image='nodeforwarder',
    ip=IP.printer.value,
    ports=[parse_port(Port.printer)],
    environment=[
        f'serial_port=/dev/ttyUSB{Usb.printer.value}',
        f'internet_port={IP.printer.value}',
        'baud_rate=115200'
    ],
    volumes=['/dev/:/dev/']

)


pulser = Container(
    container_name='pulser',
    image='nodeforwarder',
    ip=IP.pulser.value,  
    ports=[parse_port(Port.pulser)],
    environment=[
        f'serial_port=/dev/ttyUSB{Usb.pulser.value}',
        f'internet_port={IP.pulser.value}',
        'baud_rate=9600'
    ],
    volumes=['/dev/:/dev/'] 
)


remotecontrol = Container(
    container_name='remotecontrol',
    image='remotecontrol',
    ip=IP.remotecontrol.value,
    ports=[parse_port(Port.remotecontrol)],
)
    

sfogliatella = Container(
    container_name='sfogliatella',
    image='sfogliatella',
    ip=IP.sfogliatella.value,
    ports=[parse_port(Port.sfogliatella)],
    volumes=['sfogliatella:/sfogliatella/']
)


unplugged = Container(
    container_name='unplugged',
    image='unplugged',
    ip=IP.unplugged.value,
    ports=[parse_port(Port.unplugged)],
)

ustreamer = Container(
    container_name='ustreamer',
    image='ustreamer',
    ip=IP.ustreamer.value,
    ports=[parse_port(Port.ustreamer)],
    volumes=['/dev/:/dev/']
)
    

containers: tuple[Container, ...] = (
    mux,
    picoscope,
    pithy,
    printer,
    pulser,
    remotecontrol,
    sfogliatella, 
    unplugged,
    ustreamer
)