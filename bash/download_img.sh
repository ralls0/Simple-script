imgdir=$1
urllist=$2

mkdir $imgdir
while read p;
do
  wget $p -P $imgdir
done < $urllist
echo "Finish downloading"

