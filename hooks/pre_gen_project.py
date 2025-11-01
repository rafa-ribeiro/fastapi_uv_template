import subprocess

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)


print("Running pre-gen-project hook...")
# You can add any setup or initialization code here that needs to run before the project is generated

# python_version = '{{cookiecutter.min_python_version}}'
# print(f"Setting up Python {python_version} environment...")
# # run(f"uv venv --python {python_version}")
#
# print("Installing dependencies...")
# # run("uv sync")
#
# print("Activating virtual environment... -> Command: source .venv/bin/activate")
# # run("source .venv/bin/activate")

print("Pre-gen-project hook completed.")
