# This script will find any 'Uno' MIDI devices connected to the machine,
# and stream their input.

import subprocess
import sys
from pprint import pprint

# List all ports on which input devices are streaming
inputs = subprocess.Popen(['aconnect', '-i'], stdout=subprocess.PIPE)

# Find any device with 'Uno' in its name
device = subprocess.Popen(['grep', 'Uno'], stdin=inputs.stdout, stdout=subprocess.PIPE)

# Store the port the device is streaming on
output = subprocess.Popen(['cut', '-d', ' ', '-f', '2'], stdin=device.stdout, stdout=subprocess.PIPE)

# Close these output streams in case the 'port' subprocess exits before the previous subprocesses
device.stdout.close()
inputs.stdout.close()

# Strip whitespace, append ':0', and store the value
port = output.communicate()[0].strip() + '0';

# Let's listen on the port
stream = subprocess.Popen(['aseqdump', '-p', port], stdout=subprocess.PIPE)
for c in iter(lambda: stream.stdout.read(1), ''):
    pprint(c)
    sys.stdout.write(c)