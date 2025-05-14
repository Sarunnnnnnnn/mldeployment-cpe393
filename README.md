# 🧠 mldeployment-cpe393

## 📦 Model Export

Train และบันทึกโมเดล:
```bash
python3 train.py
```
> ไฟล์ `model.pkl` จะถูกสร้างในโฟลเดอร์ `app`

---

## 🐳 Docker Deployment

1. ไปที่โฟลเดอร์โปรเจกต์:
```bash
cd path/to/your/project
```

2. สร้าง Docker image:
```bash
docker build -t ml-model .
```

3. รัน Docker container:
```bash
docker run -p 9000:9000 ml-model
```

---

## 📬 วิธีใช้งาน API ด้วย Postman (หรือเครื่องมืออื่นที่รองรับ HTTP)

### 🧪 Endpoint: `/predict`
**Method:** `POST`  
**URL:** `http://localhost:9000/predict`  
**Request Body (JSON):**
```json
{
  "features": [
    [5.1, 3.5, 1.4, 0.2]
  ]
}
```

**Expected Response:**
```json
{
  "predictions": [0],
  "confidences": [1.0]
}
```

---

### ✅ Health Check
**Method:** `GET`  
**URL:** `http://localhost:9000/health`  

**Expected Response:**
```json
{
  "status": "ok"
}
```

---

### 🏡 Endpoint: `/predict_housing`
**Method:** `POST`  
**URL:** `http://localhost:9000/predict_housing`  
**Request Body (JSON):**
```json
{
  "features": [4000, 3, 2, 2, 1, 0, 1, 0, 1, 1, 1, 0, 1]
}
```

**Expected Response:**
```json
{
  "prediction": [3.7481129311345285e-13]
}
```
