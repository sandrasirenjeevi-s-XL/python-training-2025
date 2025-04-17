```markdown
# Python Training Environment Setup

## ✅ Prerequisites
- Oracle VirtualBox running Ubuntu VM  
- Local machine (host) with internet access  
- VM network mode: **Bridged Adapter** or **Port Forwarding** enabled for SSH access  

---

## 1. 💻 Install VS Code on Local Machine
- Download: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)  
- Install the following extensions:
  - `Remote - SSH` by Microsoft  
  - `Python` by Microsoft  
  - *(Optional)*: `Pylance`, `Jupyter`, `Black Formatter`

---

## 2. 🔐 Enable SSH on Ubuntu VM (Guest)
```bash
sudo apt update
sudo apt install openssh-server -y
sudo systemctl enable ssh
sudo systemctl start ssh
```

Get the VM's IP:
```bash
ip a
# or
hostname -I
```

---

## 3. 🛰️ SSH into Ubuntu VM from VS Code (Local)
1. Open VS Code  
2. Press `F1` → `Remote-SSH: Connect to Host...`  
3. Add SSH config in `~/.ssh/config`:
   ```bash
   Host my-vm
       HostName <VM_IP_ADDRESS>
       User <your-username>
       IdentityFile ~/.ssh/id_rsa
   ```
4. Connect to `my-vm`

Generate SSH key (if needed):
```bash
ssh-keygen -t rsa
```

---

## 4. 🧰 Install and Configure Git + GitHub (on VM)
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

- Add the public key to GitHub:  
  - Go to **GitHub → Settings → SSH and GPG keys**
  - Paste and save the key

---

## 5. 🐍 Install Python on Ubuntu VM
```bash
sudo apt install python3 python3-pip -y
```

---

## 6. 🧩 Install Python Support in VS Code (Remote Session)
While connected to the VM via VS Code:

- VS Code may prompt: **“Python interpreter required”** → Click Install  
- Or manually:
  - Press `F1` → `Python: Select Interpreter` → Select `python3`
- Ensure the Python extension is enabled  

Optional formatters/linters:
```bash
pip3 install pylint flake8 black autopep8
```

---

## 7. 🔄 Fork and Clone a GitHub Repository (on VM)
1. On GitHub:
   - Go to the repository and click `Fork`
2. On VM terminal:
```bash
git clone git@github.com:<your-username>/<repo>.git
cd <repo>
```

---

## 8. 🌿 Create a New Git Branch
```bash
git checkout -b <feature-branch-name>
```

---

You're now ready to roll with Python development remotely through VS Code and GitHub.
```
