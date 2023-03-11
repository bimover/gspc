import argparse
import struct
import os

#parsing arguments
parser = argparse.ArgumentParser(description='converts graphisoft point cloud (.gspc) to ascii point cloud (.xyz)')
parser.add_argument('gspc', help='input .gspc file')
parser.add_argument('-o', '--xyz', nargs='?', help='output .xyz file')
parser.add_argument('-p', '--prc', default=-1, type=int, help='rounding output to n decimal places')
args = parser.parse_args()

#set path for output file
gspcFile = args.gspc
if args.xyz is None:
    root, suffix = os.path.splitext(gspcFile)
    xyzFile = root + ".xyz"
else:
    xyzFile = args.xyz

#settings for binary head
structHeadFmt = '<4si6f' #byte order = little endian. 4x characters for signature, 1x integer, 6 floats for coordinates
structHeadLen = struct.calcsize(structHeadFmt)
structHeadUnpack = struct.Struct(structHeadFmt).unpack_from

#settings for binary body
structBodyFmt = '<3f3B' #byte order = little endian. 3x floats for coordinates, 3 chars for color
structBodyLen = struct.calcsize(structBodyFmt)
structBodyUnpack = struct.Struct(structBodyFmt).unpack_from

def readGSPC(file):
    pc = []
    with open(file, "rb") as f:
        head, version, firstX, lastX, firstY, lastY, firstZ, lastZ = structHeadUnpack(f.read(structHeadLen))
        while True:
            data = f.read(structBodyLen)
            if not data: break
            s = structBodyUnpack(data)
            point = []
            #compute the point values (add to the values of the first point)
            point.extend((s[0] + firstX, s[1] + firstY, s[2] + firstZ, s[3], s[4], s[5]))
            pc.append(point)
    #optionally round input to reduce the filesize of the output
    if not args.prc < 0:
        for i in pc:
            for j in range(3):
                i[j] = round(i[j], args.prc)
    return pc

def writeXYZ(pc):
    with open(xyzFile, "w") as f:
        f.write("X Y Z R G B")
        for i in pc:
            f.write("\n{} {} {} {} {} {}".format(i[0], i[1], i[2], i[3], i[4], i[5]))

if __name__ == '__main__':
    writeXYZ(readGSPC(gspcFile))