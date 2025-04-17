```markdown
# 🐍 Python Training Environment Setup

## ✅ Prerequisites
- Oracle VirtualBox running Ubuntu VM
- Host machine with internet access
- VM network mode: **Bridged Adapter** or **Port Forwarding** (for SSH access)

---

## 1. 💻 Install VS Code on Local Machine
- Download: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
- Install Extensions:
  - `Remote - SSH` (Microsoft)
  - `Python` (Microsoft)
  - *(Optional)*: `Pylance`, `Jupyter`, `Black Formatter`

---

## 2. 🔐 Enable SSH on Ubuntu VM (Guest)
```bash
sudo apt update
sudo apt install openssh-server -y
sudo systemctl enable ssh
sudo systemctl start ssh
```

Find the VM IP:
```bash
ip a
# or
hostname -I
```

---

## 3. 🛰️ SSH into VM from VS Code
1. Open VS Code  
2. `F1` → `Remote-SSH: Connect to Host...`  
3. Configure `~/.ssh/config`:
   ```bash
   Host my-vm
       HostName <VM_IP_ADDRESS>
       User <your-username>
       IdentityFile ~/.ssh/id_rsa
   ```
4. Connect to `my-vm`

Generate key pair (if needed):
```bash
ssh-keygen -t rsa
```

---

## 4. 🧰 Install Git & Configure GitHub (on VM)
```bash
sudo apt install git -y
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Generate GitHub SSH key:
```bash
ssh-keygen -t ed25519 -C "you@example.com"
cat ~/.ssh/id_ed25519.pub
```

Add the public key to GitHub:  
- Go to **GitHub → Settings → SSH and GPG keys**  
- Paste the key

---

## 5. 🐍 Install Python on Ubuntu VM
```bash
sudo apt install python3 python3-pip -y
```

---

## 6. 🧩 Enable Python in VS Code (Remote)
While connected via VS Code:
- VS Code may prompt: **"Python interpreter required"** → Click Install
- Or:
  - `F1` → `Python: Select Interpreter` → Choose `python3`

Optional tools:
```bash
pip3 install pylint flake8 black autopep8
```

---

## 7. 🔄 Fork and Clone GitHub Repository (on VM)
1. On GitHub:
   - Fork the target repository
2. On VM:
```bash
git clone git@github.com:<your-username>/<repo>.git
cd <repo>
```

---

## 8. 🌿 Create a Git Feature Branch
```bash
git checkout -b <feature-branch-name>
```

---

## 🎯 You’re Ready to Develop
VS Code + Remote SSH + GitHub + Python. You're good to go.
```
