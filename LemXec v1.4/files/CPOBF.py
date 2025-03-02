import random
import re

def generate_random_name():
    """Generates a random variable/function name."""
    return "var_" + "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=6))

def obfuscate_cpp(file_path, output_path):
    """Basic C++ obfuscator: renames variables/functions randomly."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        variables = set(re.findall(r"\b[a-zA-Z_]\w*\b", code))  # Find all identifiers
        replacements = {var: generate_random_name() for var in variables}

        for original, obfuscated in replacements.items():
            code = re.sub(rf"\b{original}\b", obfuscated, code)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(code)

        print(f"[+] Obfuscated C++ code saved to {output_path}")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    input_file = input("Enter C++ file to obfuscate: ").strip()
    output_file = input("Enter output filename (like obfuscated.cpp): ").strip()

    obfuscate_cpp(input_file, output_file)
