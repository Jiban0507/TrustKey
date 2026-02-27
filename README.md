# 🔐 TrustKey – Zero Knowledge Proof Based Identity Verification

TrustKey is a demo‑ready project built for secure identity verification using **Zero‑Knowledge Proofs (ZKP)**.  
It ensures that sensitive data like **Date of Birth, Mobile Number, Aadhaar Number** are never revealed directly — only **proof results** are shared.

---

## 🚀 Features

- **Age Proof**  
  - Verifies user’s age category (Child, Teenager, Adult, Senior) without exposing exact DOB.  
  - Supports multiple formats: `DD-MM-YYYY` and `YYYY-MM-DD`.  
  - Future age prediction utility.  

- **Mobile Proof**  
  - Validates mobile numbers with country code.  
  - Checks operator prefix and format.  

- **Aadhaar Proof (India)**  
  - Validates Aadhaar number format.  
  - Secure route with **AES encryption** ensures Aadhaar never leaves backend in plain text.  
  - Includes **`aadhaar_generator.py`** → a mock utility that generates random Aadhaar numbers for demo/testing.  
    - This ensures judges can test Aadhaar verification without using real Aadhaar data.  
    - Numbers are randomly generated and follow Aadhaar format rules, but are not linked to any real identity.  

- **Zero‑Knowledge Range Proofs**  
  - Verify if age lies within a given range (e.g., 18–30) without revealing actual age.  

- **Frontend UI**  
  - Modern form design with gradient background, hover effects, and card‑style result page.  
  - Clear separation of proofs: Age, Future Age, Mobile, Aadhaar, Status.  
  - Country dropdown powered by `countries.js` for global scalability.  

---

## 📂 Project Structure

```
TrustKey/
│
├── Backend/
│   ├── app.py                # Flask backend server
│   ├── utils/
│   │   ├── age_utils.py      # Age calculation & ZKP proofs
│   │   ├── mobile_utils.py   # Mobile number validation
│   │   ├── aadhaar_utils.py  # Aadhaar validation
│   │   ├── crypto_utils.py   # AES encryption/decryption
│   │   └── aadhaar_generator.py # Mock Aadhaar generator (demo only, safe testing)
│   └── requirements.txt      # Python dependencies
│
├── Frontend/
│   ├── index.html            # Verification form
│   ├── result.html           # Result page (card style)
│   ├── style.css             # Form design
│   ├── result.css            # Result page design
│   ├── script.js             # Frontend logic
│   └── countries.js          # Country codes & flags
│
└── README.md                 # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/Jiban0507/TrustKey.git
cd TrustKey
```

### 2. Backend Setup
```bash
cd Backend
pip install -r requirements.txt
python app.py
```
Backend runs on: **`http://127.0.0.1:5000`**

### 3. Frontend Setup
```bash
cd Frontend
python -m http.server 5500
```
Frontend runs on: **`http://127.0.0.1:5500/index.html`**

---

## 🔎 Demo Flow

1. User enters **DOB, Future Year, Mobile Number, Aadhaar** in form.  
2. Data sent to backend → processed by **ZKP utilities**.  
3. Backend returns **only proof results** (no raw data).  
4. Frontend displays results in **card‑style format**.  

### Example Response
```json
{
  "dob_proof": "Proof Verified: User is Young Adult (18-29)",
  "future_age_proof": "Proof Verified: In 2030, user will be 24 years old.",
  "mobile_proof": "Proof Verified: Valid Indian Mobile Number",
  "aadhaar_proof": "Proof Verified: Valid Aadhaar Number",
  "status": "All Proofs Verified"
}
```

---

## 🛡️ Security Highlights

- **Zero Knowledge Proofs** → Judges see only verification results, not sensitive data.  
- **AES Encryption** → Aadhaar numbers are encrypted before processing.  
- **Granular Validation** → Every possible input error handled with clear feedback.  
- **Mock Aadhaar Generator** → Safe demo utility for testing without real Aadhaar numbers.  

---

## 🎨 UI/UX Highlights

- Gradient background with hover glow effects.  
- Card‑style result page with unique hover animation.  
- Clear separation of proofs for demo clarity.  
- Responsive design for desktop & mobile.  
- Global country code support via `countries.js`.  

---

## 👨‍💻 Author

- **Jiban Maji**  
- GitHub: [github.com/Jiban0507](https://github.com/Jiban0507)  
- Built for **National Hackathon Demo** with focus on clarity, accessibility, and professional polish.  

---

## 🏆 Hackathon Judge Notes

- **Data Privacy** → Judges will see proof results only, not sensitive data.  
- **Demo Flow** → Easy to run: Backend (`python app.py`) + Frontend (`http.server`).  
- **Professional Docs** → Clear structure, flow diagram, and authorship highlighted.  
- **Expandability** → Can add more proofs (Passport, Voter ID) with same ZKP logic.  

---

## 📊 Flow Diagram

```
User Input (DOB, Mobile, Aadhaar)
        ↓
Backend (ZKP Logic + Encryption)
        ↓
Only Proof Results Sent
        ↓
Frontend (Card Style Result Page)
```

---

## ✅ License

This project is for **educational & hackathon demo purposes**.  
Feel free to fork and expand with new ZKP utilities.  
