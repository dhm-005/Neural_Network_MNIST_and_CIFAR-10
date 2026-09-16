# Mnist_NN

Notebook huấn luyện và so sánh 5 mô hình Deep Learning trên bộ dữ liệu MNIST:

* CNN thủ công bằng NumPy
* CNN PyTorch
* CNN TensorFlow
* RNN TensorFlow
* LSTM TensorFlow

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
├── train_cnn.ipynb
├── train_nn.ipynb
├── requirements.txt
├── README.md
└── ...
```

Notebook sẽ đọc dữ liệu từ thư mục `MNIST/` khi thực hiện huấn luyện.

## Huấn luyện mô hình

Mở file `.ipynb` bằng VS Code và chọn kernel `mnist-env`.

Notebook thực hiện:

* Khảo sát và trực quan hóa dữ liệu
* Tiền xử lý và chuẩn hóa dữ liệu
* Huấn luyện 5 mô hình Deep Learning
* Đánh giá và so sánh kết quả các mô hình
