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
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest api-automation-level2/tests --alluredir=allure-results/api
                '''
            }
        }

        stage('Run UI Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest ui-automation-level2/tests --alluredir=allure-results/ui
                '''
            }
        }

        stage('Merge Allure Results') {
            steps {
                bat '''
                mkdir merged-results
                xcopy /s /e /y allure-results\\api merged-results
                xcopy /s /e /y allure-results\\ui merged-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'merged-results']]
            }
        }
    }
}
