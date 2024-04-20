-- Write query to find the number of grade A's given by the teacher who has graded the most assignments

SELECT COUNT(*) AS grade_A_count
FROM Assignments
WHERE grade = 'A' AND teacher_id IN (
    SELECT teacher_id
    FROM Assignments
    WHERE created_at = (SELECT MAX(created_at) FROM Assignments)
)
GROUP BY teacher_id
ORDER BY grade_A_count DESC
LIMIT 1;