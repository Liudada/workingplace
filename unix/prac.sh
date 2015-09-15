function add(){
	echo $(($1+2))
}
s=`add $1`
echo $s

