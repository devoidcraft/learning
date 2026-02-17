import os
import time
import random

# --- Configuration & Data ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

COMMANDS_DB = {
    "pwd": {
        "desc": "Print Working Directory. Shows you where you are.",
        "usage": "pwd",
        "category": "Navigation"
    },
    "ls": {
        "desc": "List. Shows files and folders in current directory.",
        "usage": "ls or ls -l (for details)",
        "category": "Navigation"
    },
    "cd": {
        "desc": "Change Directory. Moves you to a different folder.",
        "usage": "cd <folder_name> or cd .. (to go back)",
        "category": "Navigation"
    },
    "mkdir": {
        "desc": "Make Directory. Creates a new folder.",
        "usage": "mkdir <folder_name>",
        "category": "File Ops"
    },
    "touch": {
        "desc": "Creates an empty file.",
        "usage": "touch <file_name>",
        "category": "File Ops"
    },
    "rm": {
        "desc": "Remove. Deletes a file.",
        "usage": "rm <file_name>",
        "category": "File Ops"
    },
    "clear": {
        "desc": "Clears the terminal screen.",
        "usage": "clear",
        "category": "System"
    },
    "cat": {
        "desc": "Concatenate. Displays content of a file.",
        "usage": "cat <file_name>",
        "category": "File Ops"
    }
}

# --- Helper Functions ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    clear_screen()
    print(f"{Colors.HEADER}{'='*40}")
    print(f"{title.center(40)}")
    print(f"{'='*40}{Colors.ENDC}\n")

# --- Core Modes ---

def learn_mode():
    """Iterates through commands and explains them."""
    print_header("LEARNING MODE")
    print("Press Enter to step through commands, or 'q' to quit.\n")
    
    for cmd, info in COMMANDS_DB.items():
        print(f"{Colors.BLUE}Command:{Colors.ENDC} {Colors.BOLD}{cmd}{Colors.ENDC}")
        print(f"{Colors.GREEN}Description:{Colors.ENDC} {info['desc']}")
        print(f"{Colors.WARNING}Usage:{Colors.ENDC} {info['usage']}")
        print("-" * 40)
        
        user_in = input("Press Enter for next...")
        if user_in.lower() == 'q':
            return
        print()

def quiz_mode():
    """Randomly asks questions about commands."""
    print_header("QUIZ MODE")
    score = 0
    questions = list(COMMANDS_DB.items())
    random.shuffle(questions)
    
    # Let's ask 5 questions
    for i in range(min(5, len(questions))):
        cmd, info = questions[i]
        print(f"Question {i+1}: What command is used to: {Colors.BOLD}{info['desc']}{Colors.ENDC}?")
        ans = input(f"{Colors.BLUE}Your Answer > {Colors.ENDC}").strip().lower()
        
        if ans == cmd:
            print(f"{Colors.GREEN}Correct!{Colors.ENDC}\n")
            score += 1
        else:
            print(f"{Colors.FAIL}Wrong.{Colors.ENDC} The correct command was: {cmd}\n")
            
    print(f"Quiz Finished! Score: {score}/5")
    input("\nPress Enter to return to menu...")

def virtual_shell():
    """A safe playground that simulates a Linux environment."""
    print_header("VIRTUAL SHELL SIMULATOR")
    print("Type 'exit' to leave. Try: ls, pwd, mkdir test, touch file.txt")
    print("------------------------------------------------------------")
    
    # Simulated State
    virtual_fs = ["home", "docs", "images"] # Simple list simulating current folder
    current_path = "/home/user"
    
    while True:
        try:
            # mimic the prompt: user@linux:~$
            cmd_str = input(f"{Colors.GREEN}user@tutor:{Colors.BLUE}{current_path}{Colors.ENDC}$ ").strip()
            
            if not cmd_str:
                continue
                
            parts = cmd_str.split()
            base_cmd = parts[0]
            
            # --- Simulation Logic ---
            if base_cmd == "exit":
                break
                
            elif base_cmd == "pwd":
                print(current_path)
                
            elif base_cmd == "ls":
                # Print simulated files
                print("  ".join(virtual_fs))
                
            elif base_cmd == "mkdir":
                if len(parts) > 1:
                    new_dir = parts[1]
                    if new_dir not in virtual_fs:
                        virtual_fs.append(Colors.BLUE + new_dir + Colors.ENDC) # Color it blue like a folder
                    else:
                        print(f"mkdir: cannot create directory '{new_dir}': File exists")
                else:
                    print("mkdir: missing operand")
                    
            elif base_cmd == "touch":
                if len(parts) > 1:
                    new_file = parts[1]
                    virtual_fs.append(new_file)
                else:
                    print("touch: missing file operand")
                    
            elif base_cmd == "rm":
                if len(parts) > 1:
                    target = parts[1]
                    # Check if plain file or colored directory
                    if target in virtual_fs:
                        virtual_fs.remove(target)
                    elif (Colors.BLUE + target + Colors.ENDC) in virtual_fs:
                        # Simple simulation: usually rm doesn't remove dirs without -r
                        print(f"rm: cannot remove '{target}': Is a directory") 
                    else:
                        print(f"rm: cannot remove '{target}': No such file or directory")
                else:
                    print("rm: missing operand")
            
            elif base_cmd == "clear":
                clear_screen()
                print("Type 'exit' to leave.")

            elif base_cmd == "help":
                print("Available commands in simulator: ls, pwd, mkdir, touch, rm, clear, exit")
                
            else:
                print(f"{base_cmd}: command not found")
                
        except KeyboardInterrupt:
            break
            
# --- Main Menu ---

def main():
    while True:
        print_header("PYTHON LINUX TUTOR")
        print("1. Learn Commands")
        print("2. Take a Quiz")
        print("3. Virtual Shell (Safe Practice)")
        print("4. Exit")
        
        choice = input(f"\n{Colors.BLUE}Select an option (1-4): {Colors.ENDC}")
        
        if choice == '1':
            learn_mode()
        elif choice == '2':
            quiz_mode()
        elif choice == '3':
            virtual_shell()
        elif choice == '4':
            print("Goodbye! Happy Hacking.")
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()