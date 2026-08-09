CREATE CONSTRAINT student_roll IF NOT EXISTS FOR (s:Student) REQUIRE s.roll_no IS UNIQUE;
CREATE CONSTRAINT course_code IF NOT EXISTS FOR (c:Course) REQUIRE c.code IS UNIQUE;

MERGE (c1:Course {code:'CS101', name:'Data Structures'});
MERGE (c2:Course {code:'CS102', name:'Operating Systems'});
MERGE (s1:Student {roll_no:'A001', name:'Asha'});
MERGE (s2:Student {roll_no:'A002', name:'Vikram'});
MERGE (s1)-[:ENROLLED_IN]->(c1);
MERGE (s1)-[:ENROLLED_IN]->(c2);
MERGE (s2)-[:ENROLLED_IN]->(c1);
