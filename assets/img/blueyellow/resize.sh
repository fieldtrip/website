for size in 50 75 100 128 150 160 200 ; do 
convert fieldtriplogo-blueyellow-high-transparent.png -resize $size -transparent white fieldtriplogo-$size.png
done
