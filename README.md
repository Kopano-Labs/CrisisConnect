# ⚡ CrisisConnect — Adaptive Crisis Response PWA

> **Mission-grade web application that adapts across 6 dimensions to help the right person make the right decision under bad conditions.**

[![Live](https://img.shields.io/badge/Live-crisisconnect.kopanolabs.com-ff3d57?style=for-the-badge)](https://crisisconnect.kopanolabs.com)
[![Kopano Labs](https://img.shields.io/badge/Kopano%20Labs-Sovereign%20Product%20Studio-0a0e1a?style=for-the-badge)](https://kopanolabs.com)
[![License](https://img.shields.io/badge/License-Proprietary-333?style=for-the-badge)]()

---

## What Is CrisisConnect?

CrisisConnect is not a responsive reporting app. It is an **adaptive operations client** built for disaster response in African conditions — where bandwidth is unreliable, devices are constrained, power is intermittent, and trust in data varies.

A normal PWA asks: *"Can this website be installed and work offline?"*

CrisisConnect asks: **"Can this system still help the right person make the right decision under bad conditions?"**

---

## 6 Dimensions of Adaptation

### 1. 📡 Connectivity Adaptation
| Mode | Behavior |
|------|----------|
| **Online Live** | Real-time incident updates, map sync, dispatch, chat |
| **Degraded** | Text-first UI, compressed payloads, reduced polling |
| **Offline Field** | Queued forms, cached maps/contacts/protocols, store-and-forward |
| **Intermittent Sync** | Conflict-aware merge when signal returns |

### 2. 👤 Role Adaptation
| Role | Surface |
|------|---------|
| **Citizen** | Report incident, request help, receive verified instructions |
| **Operator/Dispatcher** | Triage queue, SLA timers, escalation actions |
| **Field Responder** | Navigation, case notes, offline checklist, status updates |
| **Command Layer** | Heatmaps, resource allocation, bottlenecks, comms integrity |

### 3. 🚨 Urgency Adaptation
| Mode | UX Changes |
|------|------------|
| **Normal** | Full dashboards, history, analytics |
| **Active Incident** | One-tap actions, large buttons, fewer choices, pinned protocol |
| **Mass Incident** | Batching, surge workflows, broadcast tools, 56px+ tap targets |

### 4. 📱 Device Adaptation
- Cheap Android phones → reduced data density, battery-conscious
- Desktop ops centers → full dashboard, multi-panel
- Tablets in vehicles → touch-optimized, landscape support
- Kiosk/public intake → simplified input flows

### 5. 🔒 Trust Adaptation
- **Verified** vs **Unverified** report badges
- Source confidence indicators
- Last-sync timestamps
- Stale-data warnings (30min threshold)
- Duplicate incident probability
- Chain-of-custody for edits

### 6. 🌍 Local Context Adaptation
- Region-specific protocol sets (SAPS, EMS, metro)
- Hazard-type workflow specialization (flood ≠ GBV ≠ fire)
- Language and locale support (en-ZA)
- Network cost profile awareness

---

## PWA Architecture

### Core PWA Layer
- ✅ Installable (Web App Manifest)
- ✅ Service Worker with app-shell caching
- ✅ Offline cache strategy (cache-first shell, network-first API)
- ✅ Background sync for offline queue
- ✅ Push notification support
- ✅ Resilient update flow

### Adaptive Runtime Layer
- ✅ Network-aware rendering
- ✅ Device capability detection (memory, cores, battery)
- ✅ Role-based UI composition
- ✅ Incident-state-based navigation
- ✅ Progressive feature loading
- ✅ Dynamic payload budgets

### Operational Resilience Layer
- ✅ Local-first writes
- ✅ Sync queue with retry policy
- ✅ Audit trail
- ✅ Data freshness indicators
- ✅ Stale-data warnings

### Human Factors Layer
- ✅ Stress-mode UI (mass incident → 56px+ buttons)
- ✅ Large tap targets
- ✅ Text-first critical flows
- ✅ High-contrast emergency states
- ✅ Minimal decision friction

---

## KPGS Ecosystem

CrisisConnect is one node in the Kopano Labs governance ecosystem:

| Node | URL | Status |
|------|-----|--------|
| **Kopano Labs** | [kopanolabs.com](https://kopanolabs.com) | ✅ Live |
| **KRRababalela** | [krrababalela.com](https://krrababalela.com) | ✅ Live |
| **KasiLink** | [kasilink.com](https://kasilink.com) | ✅ Live |
| **CrisisConnect** | [crisisconnect.kopanolabs.com](https://crisisconnect.kopanolabs.com) | ✅ Live |
| **FivesArena Blog** | [blog.fivesarena.com](https://blog.fivesarena.com) | ✅ Live |

---

## Tech Stack

- **Frontend:** Vanilla HTML/CSS/JS — no framework dependencies, maximum resilience
- **PWA:** Service Worker + Web App Manifest
- **Design:** Dark-mode-first, glassmorphism, Inter font family
- **Caching:** App-shell architecture with network-first API strategy
- **Hosting:** Vercel (edge network)

---

## Maturity Criteria

CrisisConnect is evaluated against these operational questions:

- [x] Does it degrade gracefully on weak networks?
- [x] Can a field user complete critical actions offline?
- [x] Does the interface change by user role?
- [x] Does the workflow compress during active incidents?
- [x] Can it preserve trust when data is stale or disputed?
- [x] Does it prioritize operational continuity over visual polish?

---

## Development

```bash
# Serve locally
npx serve .

# Or use any static file server
python -m http.server 8080
```

---

## License

Proprietary — Kopano Labs © 2026. All rights reserved.

Built with operational discipline by [Kopano Labs](https://kopanolabs.com).

**Chief Architect:** [Kholofelo Robyn Rababalela](https://krrababalela.com)
