import subprocess

print("Run post-gen-project hook...")
# You can add any cleanup or finalization code here that needs to run after the project has been generated.


def run(cmd):
    subprocess.run(cmd, shell=True, check=True)


python_version = '{{cookiecutter.min_python_version}}'
print(f"Setting up Python {python_version} environment...")
run(f"uv venv --python {python_version}")

print("Installing dependencies...")
run("uv sync")

print("Activate your virtual env with -> source .venv/bin/activate")

print("Post-gen-project hook completed.")
