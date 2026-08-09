# Functional Requirements (FR)

## Core Platform
- **FR-01:** System shall provide JWT-based authentication with RBAC for Student, Faculty, Admin, Placement, and Principal roles.
- **FR-02:** System shall provide role-specific dashboards and workflows.
- **FR-03:** System shall support CRUD for students, courses, faculty, sections, exams, and placements.

## AI + Agentic
- **FR-04:** System shall orchestrate multi-agent workflows using LangGraph.
- **FR-05:** System shall route agent tasks based on intent and role context.
- **FR-06:** System shall enforce human approval for high-stakes actions.
- **FR-07:** System shall output confidence scores for critical recommendations.
- **FR-08:** System shall support agent-to-agent debate for sensitive risk decisions.

## RAG
- **FR-09:** System shall ingest documents, chunk text, embed vectors, index data, retrieve evidence, and cite sources.
- **FR-10:** System shall support offline-first retrieval mode without generation.

## ML
- **FR-11:** System shall train and serve models for performance, attendance, dropout, and placement prediction.
- **FR-12:** System shall provide SHAP/LIME-based explanation outputs.
- **FR-13:** System shall track experiments through MLflow.

## Optimization
- **FR-14:** System shall generate conflict-free timetables using OR-Tools constraints.

## Governance
- **FR-15:** Audit Trail Agent shall log all agent decisions and reasoning metadata immutably.
- **FR-16:** System shall maintain complete action history for manual and AI-triggered operations.

## Data
- **FR-17:** System shall generate synthetic datasets for privacy-safe bootstrapping/testing.
- **FR-18:** System shall perform data quality checks and drift alerts.
