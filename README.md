# **📌 Text-to-ER Diagram Generator**

![ER Diagram Generator](test.png)

## **🚀 Overview**
The **Text-to-ER Diagram Generator** is an AI-powered tool that converts natural language descriptions into **Entity-Relationship (ER) diagrams**. It provides a seamless user experience with a **Streamlit-based UI**, allowing users to visualize and export ER diagrams in multiple formats such as **PNG, PPTX, and DOT**.

## **✨ Features**
✅ Generate ER diagrams from text-based descriptions.  
✅ Export diagrams as **PNG (image), PPTX (PowerPoint), and DOT (Graphviz)**.  
✅ User-friendly **Streamlit web interface**.  
✅ **Ollama LLM integration** for entity & relationship extraction.  
✅ Works both **via UI and command-line interface (CLI)**.

---

## **📖 How It Works?**
1️⃣ **Enter a natural language description** of entities & relationships.  
2️⃣ **Click "Generate ER Diagram"** in the UI.  
3️⃣ **View the generated ER diagram** directly in the app.  
4️⃣ **Export as PNG, PPTX, or DOT** for further use.  

---

## **🛠️ Technologies Used**
🔹 **Python 3.8+** – Core programming language.  
🔹 **Streamlit** – Interactive web UI.  
🔹 **Graphviz** – ER diagram generation.  
🔹 **Ollama LLM** – AI-based text parsing.  
🔹 **Pillow** – Image processing.  
🔹 **python-pptx** – Export diagrams to PowerPoint.  

---

## **📥 Installation & Setup**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/vedant713/text-to-er-diagram.git
cd text-to-er-diagram
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Application**
```bash
streamlit run app.py
```

### **4️⃣ Generate an ER Diagram**
- Enter a **natural language description** (e.g., _"A hotel has many rooms. A customer makes bookings."_).  
- Click **Generate ER Diagram**.  
- **View & download** the generated diagram.

---

## **💻 Command-Line Usage**
This project also supports a **CLI mode** for diagram generation.

```bash
python main.py input.txt -o output
```
- `input.txt` → Text file containing ER description.  
- `-o` or `--output` → Specify the output filename.

---

## **📂 File Structure**
```plaintext
.
├── app.py                  # Streamlit app entry point
├── main.py                 # Command-line interface
├── parser.py               # LLM integration & parsing logic
├── diagram_generator.py    # Diagram generation logic
├── model.py                # Data models for entities & relationships
├── test_diagram_generator.py # Unit tests
├── requirements.txt        # Project dependencies
├── README.md               # Documentation
└── examples/
    ├── test.dot            # Sample DOT file
    └── test.png            # Sample PNG output
```

---

## **📜 Export Options**
✅ **PNG** – Standard image format.  
✅ **PPTX** – PowerPoint slides for presentations.  
✅ **DOT** – Graphviz file for further modifications.

---

## **📷 Sample Output**

**Input:**  
```
A hotel has many rooms. A customer makes bookings.
```

**Output (ER Diagram Preview):**  
![Sample Diagram](test.png)

---

## **🤝 Contributing**
Contributions are welcome! If you’d like to improve the project, **submit a pull request** or **open an issue**.

---

## **📜 License**
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

🚀 **Developed by [vedant713](https://github.com/vedant713)**
