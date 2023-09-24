from boilerplate import Container, IP, Port, Usb, parse_port


mux = Container(
    container_name='mux',
    image='nodeforwarder',
    networks=IP.mux.value,
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
    networks=IP.picoscope.value,
    ports=[parse_port(Port.picoscope)],
    volumes=[
        '/dev/:/dev/',
        'picoscope:/picoscope/'
    ],
)
    

pithy = Container(
    container_name='pithy',
    image='pithy',
    networks=IP.pithy.value,
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
    networks=IP.printer.value,
    ports=[parse_port(Port.printer)],
    environment=[
        f'serial_port=/dev/ttyUSB{Usb.printer.value}',
        f'internet_port={Port.printer.value}',
        'baud_rate=115200'
    ],
    volumes=['/dev/:/dev/']

)


pulser = Container(
    container_name='pulser',
    image='nodeforwarder',
    networks=IP.pulser.value,  
    ports=[parse_port(Port.pulser)],
    environment=[
        f'serial_port=/dev/ttyUSB{Usb.pulser.value}',
        f'internet_port={Port.pulser.value}',
        'baud_rate=9600'
    ],
    volumes=['/dev/:/dev/'] 
)


remotecontrol = Container(
    container_name='remotecontrol',
    image='remotecontrol',
    networks=IP.remotecontrol.value,
    ports=[parse_port(Port.remotecontrol)],
)
    

sfogliatella = Container(
    container_name='sfogliatella',
    image='sfogliatella',
    networks=IP.sfogliatella.value,
    ports=[parse_port(Port.sfogliatella)],
    volumes=[
        'sfogliatella:/sfogliatella/',
        '/home/lab/squidward:/sfogliatella/data/'
    ]
)


unplugged = Container(
    container_name='unplugged',
    image='unplugged',
    networks=IP.unplugged.value,
    ports=[parse_port(Port.unplugged)],
)

ustreamer_vertical = Container(
    container_name='ustreamer_vertical',
    image='ustreamer',
    networks=IP.ustreamer_vertical.value,
    ports=[parse_port(Port.ustreamer_vertical)],
    volumes=['/dev/:/dev/'],
    environment=[
        f'device=/dev/video0',
        f'port={Port.ustreamer_vertical.value}',
    ],
)

ustreamer_horizontal = Container(
    container_name='ustreamer_horizontal',
    image='ustreamer',
    networks=IP.ustreamer_horizontal.value,
    ports=[parse_port(Port.ustreamer_horizontal)],
    volumes=['/dev/:/dev/'],
    environment=[
        f'device=/dev/video2',
        f'port={Port.ustreamer_horizontal.value}',
    ],
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
    ustreamer_vertical,
    ustreamer_horizontal
)