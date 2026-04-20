
import os, sys
from pathlib import Path
_project_root = Path(__file__).resolve().parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))
from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]
load_dotenv()
import torch
from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.policies.factory import make_pre_post_processors
from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy
hf_token = os.getenv("HF_TOKEN")

def load_dataset(path:str):
    from lerobot.datasets.lerobot_dataset import LeRobotDataset
    return LeRobotDataset(path)

def get_device()->str:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_policy(model_id:str="lerobot/smolvla_base"):
    device = get_device()
    policy = SmolVLAPolicy.from_pretrained(model_id, token=hf_token).to(device).eval()
    preprocess, postprocess = make_pre_post_processors(
        policy.config,
        model_id,
        preprocessor_overrides={"device_processor": {"device": str(device)}},
    )
    return policy, preprocess, postprocess


if __name__ == "__main__":
    print(get_device())
    