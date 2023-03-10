# gspc
conversion of .gspc-files to .xyz-files

this python module can convert the graphisoft archicad native file format for point clouds (.gspc) to a more versatile ascii point cloud file (.xyz).

the module can be used from terminal with a single parameter for the .gspc input and a optional parameter -o for the .xyz output.
without the -o parameter the .xyz file is stored next to the input file

```
python gspc.py inputfile.gspc -o outputfile.xyz
```
