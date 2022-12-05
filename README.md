## Environment
Чтобы установить окружение выполните следующие команды в консоли

```
git clone https://github.com/lenker0/DeepLabV3-railway.git
cd carTreck_hackaton
pip install -r req.txt
```
## Dataset (preproc)

https://drive.google.com/file/d/1-1KhLyYrfBWBg763Q7jaAQGCyChrC5Lv/view?usp=sharing

## Train

```
python train.py --epochs=num_epochs --data_dir=/path_to_dataset/ --save_dir=/path_to_save_weights/
```
p.s добавь слэш после директорий :) <br>
/bla/bla/bla```/```

