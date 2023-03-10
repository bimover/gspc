# gspc
conversion of .gspc-files to .xyz-files  
  
this python module can convert the graphisoft archicad native file format for point clouds (.gspc) to a more versatile ascii point cloud file (.xyz)  
  
the module can be used from terminal with a single parameter for the .gspc input and two optional parameters  
-o for the .xyz output  
without the -o parameter the .xyz file is stored next to the input file  
-p for the precision (n of decimal places for rounding)  
without the -p parameter the values are stored with full precision, resulting in a larger file size  

```
python gspc.py inputfile.gspc -o outputfile.xyz -p 2
```
