export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const found = newGrades.find((g) => g.studentId === student.id);
      return { ...student, grade: found ? found.grade : 'N/A' };
    });
}
