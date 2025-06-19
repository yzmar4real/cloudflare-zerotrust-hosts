# 🔁 Cloudflare Tunnel Ingress Updater

A lightweight Python script to automate updating a Cloudflare Tunnel's ingress configuration by appending a new hostname-to-service mapping. Built using the official Cloudflare Python SDK.

---

## 📌 Use Case

This tool is ideal for:

- Quickly onboarding new services into a Cloudflare Tunnel
- Adding internal host-to-service mappings behind Zero Trust
- Ensuring fallback routes are preserved during config changes

---

## ⚙️ Features

- ✅ Pulls existing Cloudflare Tunnel configuration
- ➕ Appends a new ingress rule with proper hostname and service
- 🛡️ Auto-adds TLS verification settings if using HTTPS
- ♻️ Maintains existing fallback configuration

---

## 📂 Repository Structure

```
.
├── cloudflare_tunnel_update.py  # Main script
├── README.md                    # Documentation
└── requirements.txt             # Dependencies (optional)
```

---

## 🧰 Requirements

- Python 3.8+
- Cloudflare API Token with `Zero Trust:Edit` permissions
- Tunnel ID and Account ID
- `cloudflare` SDK (install via pip)

---

## 🚀 Installation

```bash
git clone https://github.com/your-username/cloudflare-tunnel-updater.git
cd cloudflare-tunnel-updater
pip install -r requirements.txt
```

---

## 🛠️ Configuration

Update the variables in the script before execution:

```python
tun_id = "your-tunnel-id"
acct_id = "your-account-id"
api_token = "your-cloudflare-api-token"

protocol = "http"  # or "https"
ip_address = "10.1.1.5"
port = 8089
host = "trial"
domain = "domain.com"
```

The script will construct a new service rule:

```plaintext
trial.domain.com --> http://10.1.1.5:8089
```

If HTTPS is selected, `noTLSVerify: False` is added to the `originRequest`.

---

## 🧪 Usage

Run the script:

```bash
python zt_tunnelupdate.py
```

It will:

1. Fetch current Cloudflare Tunnel configuration.
2. Append a new ingress entry.
3. Retain the fallback rule.
4. Push the updated configuration back to Cloudflare.

---

## 🔐 Security Tip

Use environment variables for secrets in production:

```python
import os
api_token = os.getenv("CF_API_TOKEN")
```

Set it before running:

```bash
export CF_API_TOKEN="your-token"
```

---

## 📈 Future Enhancements

- [ ] FastAPI Integrated version
- [ ] CloudFlare Access Policies Automation
- [ ] Additional Logging and Error Handling

---

## 🐳 Docker (Coming Soon)

I also plan to provide a Docker image for seamless deployment in CI/CD or cron-based automation.

---

## 📄 License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

**Your Name**  
GitHub: [@yzmar4real](https://github.com/yzmar4real)
