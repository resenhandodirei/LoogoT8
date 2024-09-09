from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Base de dados simulada de potenciais alunos que não concluíram a matrícula
students_data = [
    {'id': 1, 'name': 'Ana', 'email': 'ana@example.com', 'status': 'incomplete'},
    {'id': 2, 'name': 'Bruno', 'email': 'bruno@example.com', 'status': 'incomplete'},
    {'id': 3, 'name': 'Clara', 'email': 'clara@example.com', 'status': 'incomplete'}
]

# Função para gerar mensagem personalizada
def generate_message(student_name):
    messages = [
        f"Olá {student_name}, percebemos que você não finalizou sua matrícula! Precisamos de você na nossa turma. Complete sua matrícula hoje mesmo!",
        f"{student_name}, estamos quase lá! Sua vaga está te esperando. Finalize sua matrícula agora!",
        f"Oi {student_name}, sua jornada de aprendizado está quase começando! Não deixe sua matrícula pendente."
    ]
    return random.choice(messages)

# Rota para listar alunos incompletos
@app.route('/students', methods=['GET'])
def get_students():
    incomplete_students = [student for student in students_data if student['status'] == 'incomplete']
    return jsonify(incomplete_students)

# Rota para tentar reconverter aluno
@app.route('/convert/<int:student_id>', methods=['POST'])
def convert_student(student_id):
    student = next((student for student in students_data if student['id'] == student_id), None)
    
    if student and student['status'] == 'incomplete':
        # Gerar mensagem personalizada
        message = generate_message(student['name'])
        
        # Simular envio de e-mail ou mensagem
        print(f"Enviando mensagem para {student['email']}: {message}")
        
        # Alterar status para "reconvertido"
        student['status'] = 'converted'
        return jsonify({'status': 'success', 'message': 'Aluno reconvertido com sucesso!', 'student': student})
    else:
        return jsonify({'status': 'error', 'message': 'Aluno não encontrado ou já convertido.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
