import struct
import os

def test_unpack():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    with open(BASE_DIR+'/output', 'rb') as f:
        chunk = f.read(16)
        result = struct.unpack('dicccc', chunk)

        assert result == (7.5, 15, b'A', b'V', b'\x00', b'\x00')
