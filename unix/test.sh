network="183.173.40"
sum=0
for sitenu in $(seq 1 254)
do
	ping -c 1 -w 1 ${network}.${sitenu} &> /dev/null && result=0 || result=1
	if [ "$result" == 0 ];then
		sum=$(($sum+1))
		echo "Server ${network}.${sitenu} is UP."
	fi
done
echo $sum

