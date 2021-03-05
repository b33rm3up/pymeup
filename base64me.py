import sys
import base64

# 
# usage
# echo BASE64_STRING_HERE | python3 base64me.py
#

for ttyl_input in sys.stdin:
	sys.stdout.buffer.write(base64.b64decode(ttyl_input))
