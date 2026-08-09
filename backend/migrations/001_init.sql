CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(50) NOT NULL,
  is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS students (
  id SERIAL PRIMARY KEY,
  roll_no VARCHAR(50) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  department VARCHAR(100) NOT NULL,
  semester INT NOT NULL
);

CREATE TABLE IF NOT EXISTS attendance_records (
  id SERIAL PRIMARY KEY,
  student_id INT REFERENCES students(id),
  attendance_pct FLOAT NOT NULL,
  recorded_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS performance_records (
  id SERIAL PRIMARY KEY,
  student_id INT REFERENCES students(id),
  gpa FLOAT NOT NULL,
  arrears INT DEFAULT 0,
  recorded_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS placement_records (
  id SERIAL PRIMARY KEY,
  student_id INT REFERENCES students(id),
  status VARCHAR(50) NOT NULL,
  package_lpa FLOAT,
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS dropout_risk_flags (
  id SERIAL PRIMARY KEY,
  student_id INT REFERENCES students(id),
  risk_score FLOAT NOT NULL,
  reason TEXT,
  decision_trace TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS audit_logs (
  id SERIAL PRIMARY KEY,
  actor_user_id INT REFERENCES users(id),
  action VARCHAR(255) NOT NULL,
  metadata JSONB DEFAULT '{}'::jsonb,
  created_at TIMESTAMP DEFAULT NOW()
);
