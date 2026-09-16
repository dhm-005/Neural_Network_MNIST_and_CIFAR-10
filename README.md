# Mnist_NN

Notebook huấn luyện và so sánh các mô hình Deep Learning trên hai bộ dữ liệu **MNIST** và **CIFAR-10**.

## Mô hình sử dụng

### MNIST

* CNN thủ công bằng NumPy
* CNN PyTorch
* CNN TensorFlow
* RNN TensorFlow
* LSTM TensorFlow

### CIFAR-10

* CNN PyTorch
* CNN TensorFlow

## Công nghệ sử dụng

* Python
* Jupyter Notebook
* VS Code / Anaconda

## Cách chạy hệ thống

### 1. Clone repository

```bash
git clone https://github.com/dhm-005/Mnist_NN.git

cd Mnist_NN
```

### 2. Tạo môi trường

```bash
conda create -n mnist-env python=3.10

conda activate mnist-env
```

### 3. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### 4. Download dataset

#### 4.1. MNIST

Tải bộ dữ liệu MNIST từ Kaggle:

[MNIST Dataset trên Kaggle](https://www.kaggle.com/datasets/hojjatk/mnist-dataset?utm_source=chatgpt.com)

Sau khi tải và giải nén, lấy **4 file dữ liệu chính** sau:

```text
train-images.idx3-ubyte
train-labels.idx1-ubyte
t10k-images.idx3-ubyte
t10k-labels.idx1-ubyte
```

Tạo thư mục `MNIST` trong thư mục gốc của project và đặt 4 file trên vào thư mục này:

```text
Mnist_NN/
├── MNIST/
│   ├── train-images.idx3-ubyte
│   ├── train-labels.idx1-ubyte
│   ├── t10k-images.idx3-ubyte
│   └── t10k-labels.idx1-ubyte
├── cifar10/
├── train_cnn.ipynb
├── train_nn.ipynb
├── train_cifar.ipynb
├── requirements.txt
├── README.md
└── ...
```

#### 4.2. CIFAR-10

Tải bộ dữ liệu CIFAR-10 từ Kaggle:

[CIFAR-10 Dataset trên Kaggle](https://www.kaggle.com/datasets/ayush1220/cifar10/data)

Sau khi tải và giải nén, sử dụng hai thư mục `train` và `test` trong dataset.

Đặt hai thư mục này vào thư mục `cifar10` trong thư mục gốc của project:

```text
Mnist_NN/
├── cifar10/
│   ├── train/
│   │   ├── airplane/
│   │   ├── automobile/
│   │   ├── bird/
│   │   ├── cat/
│   │   ├── deer/
│   │   ├── dog/
│   │   ├── frog/
│   │   ├── horse/
│   │   ├── ship/
│   │   └── truck/
│   └── test/
│       ├── airplane/
│       ├── automobile/
│       ├── bird/
│       ├── cat/
│       ├── deer/
│       ├── dog/
│       ├── frog/
│       ├── horse/
│       ├── ship/
│       └── truck/
├── train_cifar.ipynb
└── ...
```

Notebook `train_cifar.ipynb` sẽ tự động đọc các class từ các thư mục con của `cifar10/train` và sử dụng chúng để tạo nhãn cho dữ liệu.

## Huấn luyện mô hình

Mở file `.ipynb` bằng VS Code và chọn kernel `mnist-env`.

### MNIST

* `train_cnn.ipynb`: Huấn luyện và so sánh các mô hình CNN, RNN và LSTM.
* `train_nn.ipynb`: Huấn luyện mô hình Neural Network thủ công.

Notebook thực hiện:

* Khảo sát và trực quan hóa dữ liệu
* Tiền xử lý và chuẩn hóa dữ liệu
* Huấn luyện các mô hình Deep Learning
* Đánh giá và so sánh kết quả các mô hình

### CIFAR-10

Mở file:

```text
train_cifar.ipynb
```

Notebook thực hiện:

* Khảo sát và trực quan hóa dữ liệu CIFAR-10
* Tiền xử lý và chuẩn hóa dữ liệu ảnh
* Huấn luyện CNN bằng PyTorch
* Huấn luyện CNN bằng TensorFlow
* Đánh giá và so sánh kết quả hai mô hình
