"""
zt_tunnelupdate.py

This script updates the configuration of an existing Cloudflare Tunnel by appending a new
hostname-to-service ingress rule. The script uses the official Cloudflare Python SDK.

Author: Oluyemi Oshunkoya
"""

import os
from cloudflare import Cloudflare
from cloudflare.types.zero_trust.tunnels.cloudflared.configuration_get_response import (
    Config,
    ConfigIngress,
    ConfigIngressOriginRequest,
    ConfigWARPRouting,
)

# Configuration - Replace these values with your actual credentials and parameters
tun_id = "tunnel-id"
acct_id = "acct-id"
api_token = "api-token"  # Consider using environment variables for security

# Service details to map
protocol = "http"  # or "https"
ip_address = "10.1.1.5"
port = 8089
host = "trial"
domain = "domain.com"

# Construct full service URL and FQDN
service_url = f"{protocol}://{ip_address}:{port}"
host_fqdn = f"{host}.{domain}"

# Initialize Cloudflare API client
client = Cloudflare(api_token=api_token)

# Step 1: Fetch current tunnel configuration
current_configuration = client.zero_trust.tunnels.cloudflared.configurations.get(
    tunnel_id=tun_id,
    account_id=acct_id,
)

# Step 2: Dump current config to a dict using field aliases
payload_level = current_configuration.model_dump(by_alias=True)
payload = payload_level['config']

# Step 3: Separate current ingress rules
named_rules = [r for r in payload["ingress"] if r.get("hostname")]
fallback_rule = next((r for r in payload["ingress"] if not r.get("hostname")), None)

# Step 4: Construct new ingress rule based on protocol
new_rule = {
    "hostname": host_fqdn,
    "service": service_url
}
if protocol == "https":
    new_rule["originRequest"] = {"noTLSVerify": False}

# Step 5: Reassemble ingress rules with new rule inserted before fallback
payload["ingress"] = named_rules + [new_rule]
if fallback_rule:
    payload["ingress"].append(fallback_rule)

# Step 6: Push updated configuration to Cloudflare
response = client.zero_trust.tunnels.cloudflared.configurations.update(
    account_id=acct_id,
    tunnel_id=tun_id,
    config=payload
)

# Confirmation
print(f"Ingress rule for {host_fqdn} successfully added.")
