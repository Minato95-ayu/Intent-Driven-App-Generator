# Aayu Language & Intent-Driven App Generator 🚀

**Aayu** is a brand new, highly readable, intent-driven programming language designed to bridge the gap between human thought and executable code. 

With the latest **P11 Update**, Aayu is no longer just a language—it is a complete **Intent-Driven Software Creation System**.

## 🧠 How it Works

Aayu follows a clean, modern compilation and generation pipeline:

```text
Human Intent
      ↓
Intent Parser (App Type Identified)
      ↓
Architecture Graph (Entities & Tasks)
      ↓
Aayu Code Generator
      ↓
Aayu Runtime Execution
      ↓
Output
```

The core language features a custom lexer, parser, and interpreter, enabling structured records, variable declarations, loops, error handling, and tasks (functions) in a natural English-like syntax.

---

## 📂 Projects & Capabilities

### 1. Intent Driven App Generator (P11)
Located in the `project_11_app_generator/` folder, this system takes a single natural language prompt and generates a fully functioning application in pure Aayu.

**Supported App Types (Version 1):**
- Library Management System
- Student Portal
- Blog CMS

#### Example Intent:
```bash
python project_11_app_generator/main.py "Create a Blog CMS"
```
**What happens under the hood:**
1. Recognizes the "Blog CMS" intent.
2. Designs the architecture graph (`User`, `Post`, `Comment` entities and `publish`, `moderate` tasks).
3. Automatically generates the `.aayu` files dynamically.
4. Executes the generated code via the Aayu runtime.

### 2. Pure Aayu Projects
You can also write pure Aayu code manually! The generated apps serve as a great showcase of the language's capabilities:
- Modularized code using Aayu's `use` keyword.
- `record` declarations for entities.
- Custom `task` blocks for logic.

#### Example: `student.aayu`
```aayu
record Student.
    name
    age
end.
```

#### Example: `main.aayu`
```aayu
use student.
use course.
use grade.

show "Student Portal Generated".
```

---

## 🚀 Running the Project

Ensure you have Python installed to run the interpreter.

### To use the App Generator:
```bash
python project_11_app_generator/main.py "Create a Library Management System"
```

### To run a specific Aayu file:
```bash
python run.py project_11_app_generator/generated_apps/library/main.aayu
```

---

## 🛠️ Future Roadmap (Phase 2 & P12)

Aayu is rapidly evolving! The next steps for the language include:
1. **Expanding App Generation:** Adding support for custom apps like "Hostel Management System" or "Adumate Service App" (P12).
2. **Aayu Specification v1.0:** Freezing the syntax and features.
3. **VS Code Extension:** Adding official syntax highlighting and IntelliSense for `.aayu` files.
4. **GitHub Linguist PR:** Registering Aayu as an official GitHub language!