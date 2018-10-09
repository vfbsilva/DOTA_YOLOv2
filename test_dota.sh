file_in=P0197
format=.png
dir=./images/
>results.txt
./darknet detector test cfg/dota.data cfg/yolo-dota.cfg yolo-dota.cfg_450000.weights ${dir}${file_in}${format} -thresh 0.1
python parse_results.py ${dir}$file_in${format}  results.txt ./croped/${file_in}
#./darknet detector test cfg/dota.data cfg/yolo-dota.cfg dota-backup/yolo-dota.cfg_450000.weights ../dota_data/YOLO/test/images/P0017__1__0___0.jpg -thresh 0.1
