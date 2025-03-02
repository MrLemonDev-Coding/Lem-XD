import base64

def obfuscate_python(file_path, output_path):
    """Obfuscates Python code using base64 encoding."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        encoded_code = base64.b64encode(code.encode()).decode()
        obfuscated_code = f"import base64\nexec(base64.b64decode({encoded_code!r}).decode())"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print(f"[+] Obfuscated code saved to {output_path}")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    input_file = input("Enter Python file to obfuscate: ").strip()
    output_file = input("Enter output name (like obfuscated.py): ").strip()
    
    obfuscate_python(input_file, output_file)
