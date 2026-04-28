import base64
import sys
import os
import zlib
import marshal
# Coded by heaven
def create_file(existing_file):
    output_file = f"heaven_{existing_file}"

    with open(existing_file, "r", encoding="utf-8") as f:
        source_code = f.read()
        
    bytecode = compile(source_code, existing_file, 'exec')
    marshalled = marshal.dumps(bytecode)
    compressed = zlib.compress(marshalled)
  
    package = base64.b64encode(compressed).decode()

    loader_template = f"""import base64
import zlib
import marshal
import sys

def heaven():
    try:
        raw = base64.b64decode("{package}")
        decompressed = zlib.decompress(raw)
        code_obj = marshal.loads(decompressed)
        
       
        exec_globals = globals().copy()
        exec_globals['__name__'] = '__main__'
        
        exec(code_obj, exec_globals)
        
    except Exception as e:
        
        import traceback
        print("An error occurred while running the obfuscated code:")
        traceback.print_exc()

if __name__ == "__main__":
    heaven()
"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(loader_template)
        
    print(f"Success: {existing_file} -> {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python obfuscator.py <target_file>")
    else:
        target_file = sys.argv[1]
        if os.path.exists(target_file):
            create_file(target_file)
        else:
            print(f"Error: {target_file} not found.")