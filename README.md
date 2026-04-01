# Zero-Trust Network Access (ZTNA) Lab

A hands-on simulation of a Zero-Trust Network Access architecture built using 
WireGuard, Nginx mTLS, Docker, and Python. Aligned to NCSC Zero Trust 
Architecture principles and NIST SP 800-207.

## Architecture Overview
```
Client (WireGuard) → Identity Proxy (mTLS) → Policy Engine → Internal Services
```

Never Trust · Always Verify · Least Privilege

## Security Controls Implemented

- **Mutual TLS (mTLS)** — every client must present a valid certificate
- **Custom PKI** — self-hosted Certificate Authority using OpenSSL
- **Microsegmentation** — services isolated on internal Docker network
- **Least Privilege** — identity-based access policies per user
- **Time-based restrictions** — access limited to business hours only
- **WireGuard VPN** — encrypted transport layer

## Tech Stack

- WireGuard — encrypted tunnels
- Nginx — mTLS reverse proxy
- OpenSSL — Certificate Authority
- Docker & Docker Compose — containerised microsegmentation
- Python & Flask — policy engine

## Project Structure
```
ztna-lab/
├── ca/              # Certificate Authority files
├── certs/           # Server certificates
├── wireguard/       # WireGuard configs
├── nginx/           # Reverse proxy config
├── policy-engine/   # Python access policy engine
├── services/        # Backend microservices
└── docker-compose.yml
```

## Setup Instructions

### Prerequisites
- Ubuntu 22.04 or 24.04
- Docker & Docker Compose
- WireGuard
- OpenSSL
- Python 3.12

### Installation

1. Clone the repository:
```
git clone https://github.com/YourUsername/ztna-lab.git
cd ztna-lab
```

2. Generate certificates:
```
cd ca
openssl genrsa -out ca.key 4096
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt -subj "/CN=ZTNA-Lab-CA"
```

3. Start all containers:
```
docker-compose up -d
```

4. Verify all containers are running:
```
docker ps
```

## Test Results

### Test 1 — Authorised access (PASS)
```
curl -k --cert ca/client.crt --key ca/client.key https://localhost/service-a/
Response: {"message":"Welcome to Service A","service":"service-a","status":"running"}
```

### Test 2 — No certificate (FAIL as expected)
```
curl -k https://localhost/service-a/
Response: 400 Bad Request — No required SSL certificate was sent
```

### Test 3 — Direct service access bypass (FAIL as expected)
```
curl http://localhost:8080/
Response: Connection refused
```

### Test 4 — Direct service-b access bypass (FAIL as expected)
```
curl http://localhost:8081/
Response: Connection refused
```

## Frameworks Referenced

- [NCSC Zero Trust Architecture](https://www.ncsc.gov.uk/blog-post/zero-trust-architecture-design-principles)
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final)

## Potential Extensions

- Device posture checking
- OIDC/OAuth2 identity integration
- Log forwarding to SIEM
- Geo-based access restrictions
- Automated certificate rotation
