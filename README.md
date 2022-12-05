## Environment
Чтобы установить окружение выполните следующие команды в консоли

```
git clone https://github.com/lenker0/DeepLabV3-railway.git
cd DeepLabV3-railway
pip install -r req.txt
```
## Dataset (preproc)

https://drive.google.com/file/d/1-1KhLyYrfBWBg763Q7jaAQGCyChrC5Lv/view?usp=sharing

## Train

```
python train.py --epochs=num_epochs --data_dir=/path_to_dataset/train_data --save_dir=/path_to_save_weights/
```
p.s добавь слэш после директорий :) <br>
/bla/bla/bla```/```

## Evaluate

``` 
python evaluate.py --data_dir=/path_to_dataset/test_data --weight=/path_to_weight/DeepLabV3Plus_bestloss.pth
```

