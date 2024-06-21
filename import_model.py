import os
from huggingface_hub import HfApi, hf_hub_download

def download_checkpoint_folder(repo_id, checkpoint_folder, local_dir):
    # Initialize the HfApi
    api = HfApi()
    
    # List all files in the repository
    repo_files = api.list_repo_files(repo_id)
    
    # Filter files to only include those in the specified checkpoint folder
    checkpoint_files = [file for file in repo_files if file.startswith(checkpoint_folder)]
    
    # Download each file in the checkpoint folder
    for file_path in checkpoint_files:
        file_name = file_path.split('/')[-1]
        local_file_path = os.path.join(local_dir, file_name)
        hf_hub_download(repo_id=repo_id, filename=file_path, local_dir=local_dir)
        print(f"Downloaded: {file_path} to {local_file_path}")


# Parameters
repo_id = "LmPa/gemma2b-newsplit-dedup"  # Replace with your repo ID
checkpoint_folder = "checkpoint-9000"  # Replace with your checkpoint folder
local_dir = "checkpoints"  # Replace with your local directory

# Download the entire checkpoint folder
download_checkpoint_folder(repo_id, checkpoint_folder, local_dir)