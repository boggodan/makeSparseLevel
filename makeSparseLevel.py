import sys
import os
if (len(sys.argv)<2):
	print 'You need to call makeSparseLevel.py [xmlTilesetFile]'
	sys.exit('Please specify an input file name.')

filepath = sys.argv[1];

if os.path.exists(filepath)==False:
	sys.exit('No such input file')

f = open(filepath, 'rt')
outFile = open(filepath.split('.')[0]+'_sparse.xml', 'wt')

print 'Reading Tilemap'

while True:
	
	line = f.readline()
	if not line:
		print 'Finished sparsifying.' 
		break

	result = line.find('tile="-1"')
	if result == -1:
		print line 
		outFile.write(line)

f.close()
