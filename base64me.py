import sys
import base64

for ttyl_input in sys.stdin:
	sys.stdout.buffer.write(base64.b64decode(ttyl_input))
