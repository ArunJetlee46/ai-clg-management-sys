# User Stories with Acceptance Criteria

## US-01 Student Risk Insights
**As a** student, **I want** personalized risk insights **so that** I can improve outcomes early.

### Acceptance Criteria
- Student dashboard shows risk level (low/medium/high) for performance and attendance.
- Each insight includes at least 3 explainable factors.
- Recommendations are actionable and course-specific.
- Last updated timestamp is visible.

## US-02 Faculty Intervention Support
**As a** faculty member, **I want** intervention suggestions for low-attendance students **so that** I can act before failure risk increases.

### Acceptance Criteria
- Faculty view lists students below attendance threshold.
- Suggested interventions include outreach templates and follow-up schedule.
- Faculty can mark interventions as completed.
- Intervention history is retained and queryable.

## US-03 Placement Readiness Ranking
**As a** placement officer, **I want** readiness ranking with explainable factors **so that** I can prioritize support.

### Acceptance Criteria
- Students are ranked by readiness score.
- Score includes explainability summary.
- Filtering by department, batch, and skill domain is supported.
- Export to CSV is available.

## US-04 Conflict-Free Timetable
**As an** admin, **I want** conflict-free timetables respecting constraints **so that** scheduling is operationally valid.

### Acceptance Criteria
- No faculty/room/student group overlap in final schedule.
- Lab constraints and room capacity are enforced.
- Constraint violations (if any) are shown with reason.
- Admin can re-run generation with modified constraints.

## US-05 Institutional Risk Oversight
**As a** principal, **I want** institution-wide risk trends with auditable AI reasoning **so that** governance decisions are evidence-based.

### Acceptance Criteria
- Dashboard shows trend metrics for attendance, dropout, and performance.
- High-risk recommendations require explicit approval status.
- Drill-down reveals underlying recommendation metadata.
- Audit reference ID is available for every AI-generated critical recommendation.

## US-06 Compliance Auditability
**As a** compliance reviewer, **I want** immutable AI decision logs **so that** accountability is enforceable.

### Acceptance Criteria
- Every critical AI decision has a unique immutable log entry.
- Log includes actor, timestamp, confidence score, and rationale metadata.
- Historical entries cannot be overwritten through standard API operations.
- Query by decision ID, date range, module, and stakeholder role is supported.
