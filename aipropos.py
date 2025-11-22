try:
    import subprocess
    import os
    import sys
    from dotenv import load_dotenv
    from google import genai
    from google.genai import types
except:
    print("Required modules are not installed. Please install them and try again.\nSee aipropos --help for more information.")

ver = "1.1"

if not os.path.exists(".env"):
    env = open(".env", "w")
    env.write('TOKEN=""\naimodel="gemini-2.5-flash"')
    env.close()
if not os.path.exists("install.sh"):
    install = open("install.sh", "w")
    install.write('#!/bin/bash\nsudo apt update -y && sudo apt install python3-pip python3-venv -y\npython3 -m venv .venv\nsource .venv/bin/activate\npip3 install google-genai python-dotenv')
    install.close()

os_release = open("/etc/os-release").read()

# Arguments
if len(sys.argv) < 2:
    print("Usage: aipropos <description>")
    exit()

elif sys.argv[1] == "--reset-env" or sys.argv[1] == "-r":
    env = open(".env", "w")
    env.write(f'TOKEN=""\naimodel = "gemini-2.5-flash"\n')
    env.close()
    print("Configuration of .env file was set to default.")
    exit()

elif sys.argv[1] == "--configure" or sys.argv[1] == "-c":
    subprocess.run(["nano", '.env'])
    exit()

elif sys.argv[1] == "--version" or sys.argv[1] == "-v":
    print(f"aipropos v{ver}")
    exit()

elif sys.argv[1] == "--install" or sys.argv[1] == "-i":
    subprocess.run(["bash", "install.sh"])
    exit()

elif sys.argv[1] == "--install-lib" or sys.argv[1] == "-il":
    subprocess.run(["pip3", "install", "google-genai", "python-dotenv"])
    exit()

elif sys.argv[1] == "--system_spec" or sys.argv[1] == "-ss":
    print(f"System data (from /etc/os-release):\n{os_release}")
    exit()

elif sys.argv[1] == "--create_venv" or sys.argv[1] == "-cv":
    try:
        subprocess.run(["python3", "-m", "venv", ".venv"])
        print(f"Virtual environment '.venv' created successfully in {os.getcwd()}.")
    except Exception as error:
        print(f"Failed to create virtual environment: {error}")
    exit()

elif sys.argv[1] == "--build" or sys.argv[1] == "-b":
    subprocess.run(["bash", "build-deb.sh"])
    exit()

elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print(f"""aipropos - AI powered linux command search tool.\n\n
          Version: {ver}\n
          --help, -h          Show this help message\n
          --version, -v       Show program version\n
          --configure, -c     Open .env configuration file to enter API token 
                              or change language model (uses nano editor as default)\n
          --reset-env, -r     Reset .env file to default configuration\n
          --install, -i       Install required python libraries, pip3 and venv\n
          --install-lib, -il  Install only python libraries (If you have pip3 installed)\n
          --system_spec, -ss  Show system specifications from /etc/os-release\n
          --create_venv, -cv  Manually create python3 virtual environment in .venv directory.\n
          --build, -b         Build .deb package from aipropos sourcecode (build-deb.sh)\n
          Usage: aipropos <description>\n
          Remember to configure your .env file with your Google AI API token before using program.
          Artificial Intelligence may be incorrect or produce unexpected results, use commands with caution.
          Example: aipropos default package manager for ubuntu""")
    exit()

try:
    load_dotenv()
    ai_token = os.getenv('TOKEN')
    ai_model = f"{os.getenv('aimodel')}"
    ai_client = None

    if ai_token == "" or ai_token is None:
        raise Exception
except Exception:
    print("Can't load .env file or token, make sure it's properly configured.\nSee aipropos --help for more information.")
    exit()

desc = " ".join(sys.argv[1:])

try:
    ai_client = genai.Client(api_key=f"{ai_token}")
    response = ai_client.models.generate_content(
        model=f"{ai_model}", contents=desc, config=types.GenerateContentConfig(
            system_instruction=[f'You are searching a linux command that meets user description: {desc} and can work on a system with this specifications: {os_release}. Always answer in user language. Answer with a short command description and basic examples. Raw mode - Only plain text; no text formatting.']
        )
    )
    print(response.text)
    ai_client.close()
    exit()
except Exception as error:
    print(f"Something went wrong, possible cause:\n{error}\n\nMake sure you have entered a valid API token in the .env file.")
    exit()