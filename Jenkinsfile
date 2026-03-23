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
                venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r api-automation-level2\\requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                venv\\Scripts\\activate
                cd api-automation-level2
                pytest
                '''
            }
        }

        stage('Allure Report') {
            steps {
                bat '''
                venv\\Scripts\\activate
                cd api-automation-level2
                pytest --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
    }
}
