import sys
import os

# Add parent directory to path so we can import run.py from the core language
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from run import run_file

from intent_engine.parser import parse_intent
from intent_engine.graph import generate_graph
from intent_engine.verifier import verify_graph
from intent_engine.generator import generate_app

def main():
    print("Welcome to Aayu: Intent Driven App Generator")
    print("-" * 50)
    
    if len(sys.argv) > 1:
        user_intent = " ".join(sys.argv[1:])
    else:
        user_intent = input("Enter your intent (e.g. 'Create a Library Management System'): ")
        
    print(f"\n[1/5] Analyzing Intent: '{user_intent}'")
    try:
        app_type = parse_intent(user_intent)
        print(f"      Identified App Type: {app_type}")
        
        print(f"[2/5] Designing Architecture Graph...")
        graph = generate_graph(app_type)
        print(f"      Found {len(graph['entities'])} entities and {len(graph['tasks'])} tasks.")
        
        print(f"[3/5] Verifying Graph...")
        verify_graph(graph)
        print("      Verification passed.")
        
        print(f"[4/5] Generating Aayu Source Code...")
        # Get absolute path for generator to put files correctly relative to this script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(base_dir, "generated_apps")
        main_aayu_path = generate_app(app_type, graph, output_base_dir=output_dir)
        print(f"      Code generated at: {main_aayu_path}")
        
        print(f"[5/5] Executing Application...")
        print("-" * 50)
        # Execute the generated file using Aayu interpreter
        run_file(main_aayu_path)
        print("-" * 50)
        print("Execution complete.")
        
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
