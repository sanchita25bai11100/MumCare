# MumCare — System Architecture

## 1. Architectural Overview

MumCare is designed as a modular, AI-assisted maternal care platform.

The architecture separates the user-facing application, backend services, intelligence layer, data layer, and healthcare integration layer.

```text
                         ┌──────────────────────┐
                         │       MUMCARE        │
                         │    Mobile / Web UI   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      API LAYER       │
                         │ Authentication       │
                         │ User Requests        │
                         │ Care Services        │
                         └──────────┬───────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
             ▼                      ▼                      ▼
      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
      │   CONTEXT    │      │ AI / NLP     │      │ CARE         │
      │   ENGINE     │      │   ENGINE     │      │ SERVICES     │
      │              │      │              │      │              │
      │ Profile      │      │ Chat         │      │ Reminders    │
      │ Timeline     │      │ Documents    │      │ Appointments │
      │ Symptoms     │      │ Extraction   │      │ Doctors      │
      │ Mood         │      │ Guidance     │      │ Escalation   │
      └──────┬───────┘      └──────┬───────┘      └──────┬───────┘
             │                     │                     │
             └─────────────────────┼─────────────────────┘
                                   ▼
                         ┌──────────────────────┐
                         │      DATA LAYER      │
                         │                      │
                         │ PostgreSQL / MongoDB │
                         │ Secure Documents     │
                         │ Care Events          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  EXTERNAL SERVICES   │
                         │                      │
                         │ Notifications        │
                         │ Calling / Chat       │
                         │ Cloud Infrastructure │
                         └──────────────────────┘
