f = open('numbers1.txt', 'w')

for i in range(1,21):
    #f.write( str(i*10) + '\n' )
    f.write( str(i*10) )
    f.write( '\n' )
    
f.close()