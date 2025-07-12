def to_plant(letter):
    return {'V':'Violets','G':'Grass','R':'Radishes','C':'Clover'}[letter]
class Garden:
    DEFAULT_STUDENTS=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid','Larry']
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.rows=diagram.split('\n')
        self.kids=sorted(students)
    def plants(self, student):
        return list(map(to_plant,[self.rows[0][self.kids.index(student) * 2],self.rows[0][self.kids.index(student) * 2 + 1],self.rows[1][self.kids.index(student) * 2],self.rows[1][self.kids.index(student) * 2 + 1]]))
