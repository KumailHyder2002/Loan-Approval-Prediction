# LoanPal — KNN Loan Approval Predictor

A full-stack FinTech web application that predicts loan approval outcomes using a **K-Nearest Neighbors classifier** (k=9). Built with Next.js 15 and Tailwind CSS, the UI exposes the model's reasoning in real time — showing which historical peers the applicant most closely resembles and why.

## What It Does

A user fills in a **3-step eligibility form** (Personal Demographics → Financial Profile → Loan Details). On submission, the app:

1. Scales the input features using pre-fitted `StandardScaler` parameters
2. Runs a KNN lookup against the training set to find the 9 nearest historical applicants
3. Returns an **approval / rejection recommendation** with a confidence score
4. Renders the 9 nearest neighbours in an **interactive scatter plot** (Credit × Income space)
5. Lists each peer in a **Historical Peers Analysis table** with their distance, income, loan amount, credit status, and outcome

The entire model runs **client-side in the browser** — no backend required at runtime.

---

## Model Performance

| Metric | Value |
|--------|-------|
| Algorithm | K-Nearest Neighbors (k=9) |
| Train Accuracy | ~82% |
| Test Accuracy | ~80% |
| F1 Score | 0.89 |
| Precision | 0.85 |
| Training records | 491 (80% of 614) |
| Test records | 123 (20% of 614) |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Framework | Next.js 15 (App Router) |
| UI Library | React 19 |
| Styling | Tailwind CSS 3 + CSS custom properties |
| Language | TypeScript |
| Fonts | Outfit (headlines), Inter (body/data) |
| Icons | Material Symbols Outlined |
| ML Pipeline | Python 3, scikit-learn, pandas, NumPy |
| Notebook | Jupyter / Google Colab |

---

## Project Structure

```
loanpal/
├── src/
│   └── app/
│       ├── layout.tsx          # Root layout, font imports, metadata
│       ├── page.tsx            # Main dashboard (loan predictor view)
│       └── globals.css         # Design tokens, glass-card utility, animations
├── ml/
│   ├── KNN_Loan_Approval.ipynb # End-to-end model training notebook
│   ├── extract_data.py         # Preprocessing + exports knn_data.json
│   └── data.csv                # Raw dataset (614 loan records, 13 features)
├── public/                     # Static assets
├── DESIGN.md                   # Full design system specification
├── tailwind.config.ts          # Tailwind theme — Material You colour tokens
├── next.config.mjs
├── tsconfig.json
└── package.json
```

---

## Getting Started

### Prerequisites
- Node.js 18+
- npm

### Run the app

```bash
git clone https://github.com/your-username/loanpal.git
cd loanpal
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

### Re-run the ML pipeline (optional)

The app ships with pre-exported model data (`ml/knn_data.json`). To regenerate it:

```bash
cd ml
pip install pandas numpy scikit-learn
python extract_data.py
```

This re-preprocesses `data.csv`, retrains the KNN model, and overwrites `knn_data.json` with updated scaler parameters and training vectors.

---

## ML Pipeline

### Dataset
- **Records:** 614 loan applications
- **Features:** 12 (after dropping `Loan_ID`)
- **Target:** `Loan_Status` — `Y` (Approved) or `N` (Rejected)

### Preprocessing steps (`extract_data.py`)
1. Drop `Loan_ID` (non-predictive identifier)
2. Impute numeric nulls → **column median**
3. Impute categorical nulls → **column mode**
4. Label-encode all categorical columns (storing class mappings for reverse lookup)
5. 80/20 stratified train-test split (`random_state=42`)
6. **StandardScaler** fit on training set only; transform applied to both splits
7. Export scaler mean/scale, training vectors, and label mappings to `knn_data.json`

### Features

| Feature | Type | Notes |
|---------|------|-------|
| Gender | Categorical | Male / Female |
| Married | Categorical | Yes / No |
| Dependents | Categorical | 0 / 1 / 2 / 3+ |
| Education | Categorical | Graduate / Not Graduate |
| Self_Employed | Categorical | Yes / No |
| ApplicantIncome | Numeric | Monthly income (applicant) |
| CoapplicantIncome | Numeric | Monthly income (co-applicant) |
| LoanAmount | Numeric | Loan amount (thousands) |
| Loan_Amount_Term | Numeric | Term in months |
| Credit_History | Numeric | 1 = good history, 0 = bad |
| Property_Area | Categorical | Urban / Semiurban / Rural |

### Hyperparameter selection
`n_neighbors=9` selected via elbow-method analysis — see `ml/KNN_Loan_Approval.ipynb` for the k vs. accuracy curve.

---

## UI Features

- **3-step eligibility form** — Personal Demographics → Financial Profile → Loan Details, with step indicator and Continue / Back navigation
- **Approval / Rejection hero card** — confidence score (92% approved, 41% rejected), colour-coded left border
- **Mock toggle** — instantly switch between approval and rejection states for demo / presentation
- **Nearest Neighbours scatter plot (K=9)** — 2D projection in Credit × Income space; current applicant as amber centre dot, approved peers in green, declined in red
- **Historical Peers Analysis table** — 9 rows ranked by Euclidean distance, showing income, loan amount, credit status, and final outcome per peer
- **Engine status panel** — contextual description of what the classifier is evaluating
- **Dark / light mode toggle**
- **Responsive** — full desktop nav collapses gracefully on smaller screens

---

## Design System

See [`DESIGN.md`](./DESIGN.md) for the complete specification.

**Aesthetic:** Modern Minimalism + Glassmorphism. Dark-mode-first "command centre" feel designed to instil analytical precision and technological confidence.

**Colour roles (Material You):**

| Role | Hex | Usage |
|------|-----|-------|
| `primary` | `#4edea3` | Approvals, confidence scores, primary CTA |
| `secondary` | `#adc6ff` | Interactive elements, neutral AI states |
| `tertiary` | `#ffb2b7` | Rejections, risk alerts, declined peers |
| `background` | `#0e1511` | Deep slate foundation |

**Glass cards:** `backdrop-filter: blur(12px)` + `1px rgba(255,255,255,0.1)` border edge.

**Typography:** Outfit for display and headlines; Inter for all body text and tabular financial data.

**Motion:** All state transitions use `200ms cubic-bezier(0.4, 0, 0.2, 1)`.

---

## License

MIT
