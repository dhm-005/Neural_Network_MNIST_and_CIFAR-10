from flask import Flask, render_template, request
from PIL import Image, ImageOps
from io import BytesIO
from pathlib import Path
import numpy as np
import base64
import joblib

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024

# Load model
model_path = Path(__file__).parent / "mnist_deployment.pkl"
model = joblib.load(model_path)


def preprocess_image(file):
    from PIL import Image, ImageOps
    import numpy as np

    # 1. Chuyển sang ảnh xám
    img = Image.open(file).convert("L")
    img = ImageOps.autocontrast(img)

    # 2. Đưa chữ số về màu trắng, nền đen
    if np.array(img).mean() > 127:
        img = ImageOps.invert(img)

    # 3. Loại bỏ phần nền, lấy vùng chữ số
    binary = img.point(lambda p: 255 if p > 30 else 0)
    bbox = binary.getbbox()

    if bbox is None:
        raise ValueError("Không tìm thấy chữ số trong ảnh.")

    img = img.crop(bbox)

    # 4. Giữ tỉ lệ, thu nhỏ vừa khung 20x20
    img.thumbnail((20, 20), Image.Resampling.LANCZOS)

    # 5. Tạo ảnh 28x28, nền đen
    canvas = Image.new("L", (28, 28), 0)

    # 6. Căn giữa chữ số
    x = (28 - img.width) // 2
    y = (28 - img.height) // 2
    canvas.paste(img, (x, y))

    # 7. Chuẩn hóa pixel về [0, 1]
    X = np.array(canvas, dtype=np.float32) / 255.0

    # 8. Thêm batch và channel dimension
    X = X.reshape(1, 28, 28, 1)

    return X


@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    prediction = None
    uploaded_image = None
    error = None

    if request.method == "POST":
        file = request.files.get("image")

        if file is None or file.filename == "":
            error = "Vui lòng chọn một ảnh để dự đoán."
        else:
            try:
                # Đọc ảnh và tạo bản xem trước
                raw = file.read()
                img_preview = Image.open(BytesIO(raw)).convert("RGB")

                preview_buffer = BytesIO()
                img_preview.save(preview_buffer, format="PNG")
                uploaded_image = (
                    "data:image/png;base64,"
                    + base64.b64encode(
                        preview_buffer.getvalue()
                    ).decode("utf-8")
                )

                # Tiền xử lý và dự đoán
                X = preprocess_image(BytesIO(raw))
                probabilities = model.predict(X, verbose=0)[0]

                prediction = int(np.argmax(probabilities))

                # Xác suất của từng nhãn từ 0 đến 9
                results = [
                    {
                        "label": i,
                        "probability": round(
                            float(probabilities[i]) * 100, 2
                        )
                    }
                    for i in range(10)
                ]

                # Sắp xếp từ xác suất cao xuống thấp
                results.sort(
                    key=lambda item: item["probability"],
                    reverse=True
                )

            except Exception as e:
                error = (
                    "Không thể xử lý ảnh này. "
                    "Vui lòng thử ảnh khác có chứa một chữ số rõ ràng."
                )
                print("Lỗi xử lý ảnh:", e)

    return render_template(
        "index.html",
        results=results,
        prediction=prediction,
        uploaded_image=uploaded_image,
        error=error
    )


@app.errorhandler(413)
def file_too_large(e):
    return render_template(
        "index.html",
        results=None,
        prediction=None,
        uploaded_image=None,
        error="Ảnh quá lớn. Vui lòng chọn ảnh không quá 8 MB."
    ), 413


if __name__ == "__main__":
    app.run(debug=True)