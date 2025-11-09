## Project Overview

This project is a full-stack, community-driven platform developed in Django (backend) and React (frontend). Its focus is to enable residents within housing societies to create communities, post listings (such as items for sale or services), and communicate securely. The build is structured for rapid prototyping, weekly deliverables, and clean handoff, making it ideal for capstone demonstrations or as a robust starting point for MVP launches.[1][2]

## Key Features

- **User Authentication**: Secure registration and login with JWT, supporting optional email verification.
- **Community Management**: Users can create and join communities with access codes for privacy.
- **Listing System**: CRUD operations on listings, supporting media uploads and advanced search/filters.
- **Messaging and Notifications**: Direct messaging with real-time-like UI and email alerts via Celery and SendGrid.
- **Modern Frontend**: Responsive and intuitive UI using React, TailwindCSS, and Vite.
- **Admin Interface**: Django admin panel for efficient backend management.
- **Efficient Deployment**: Production-ready deployment practices using Render and Vercel, scalable for real users.

## Tech Stack

- **Backend**: Django, Django REST Framework, JWT, PostgreSQL, Celery, Redis
- **Frontend**: React (Vite), TailwindCSS, Axios
- **Media & Cloud**: Cloudinary or AWS S3, Render, Vercel, Supabase
- **Extra**: Stripe API (optional), SendGrid, Notion/Google Forms for beta feedback

## Development Roadmap

Development is organized as daily modules covering Git setup, database schema, authentication, frontend-backend integration, real-time communication, admin tooling, and deployment. This schedule maximizes learning by incorporating end-to-end delivery and encourages a continuous feedback cycle from early users.







Entity relationship diagram(ERD)
┌───────────────────────────┐
│        UserProfile        │
│───────────────────────────│
│ id (PK)                   │
│ name                      │
│ email (unique)            │
│ bio                       │
│ joined_at                 │
└──────────────┬────────────┘
               │ 1 (creates)
               │
               │
┌──────────────▼────────────┐      ┌────────────────────────────┐
│        Community           │      │         Listing            │
│────────────────────────────│      │────────────────────────────│
│ id (PK)                    │      │ id (PK)                   │
│ name (unique)              │      │ title                     │
│ description                │      │ description               │
│ created_by (FK → User)     │      │ created_by (FK → User)    │
│ created_at                 │      │ community (FK → Community)│
└──────────────┬─────────────┘      │ created_at                │
               │                    │ updated_at                │
               │                    └────────────────────────────┘
               │
               │ many-to-many
               │
       ┌───────▼────────┐
       │ UserProfile     │
       │ (members)       │
       └─────────────────┘




Entity Relationship Diagram (ERD)
UserProfile
├── name : string
├── email : string (unique)
├── bio : text (optional)
└── joined_at : datetime

Community
├── name : string (unique)
├── description : text (optional)
├── created_by : FK → UserProfile
├── members : ManyToMany → UserProfile
└── created_at : datetime

Listing
├── title : string
├── description : text
├── created_by : FK → UserProfile
├── community : FK → Community
├── created_at : datetime
└── updated_at : datetime
