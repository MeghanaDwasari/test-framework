pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/MeghanaDwasari/test-framework.git'
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r api-automation-level2\\requirements.txt
                '''
            }
        }

        stage('Run Tests + Generate Allure Results') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                cd api-automation-level2
                pytest --alluredir=allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'api-automation-level2/allure-results']]
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
    }
}
