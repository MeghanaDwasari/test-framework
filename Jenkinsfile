pipeline {
    agent any

    tools {
        // This must match the name you gave in Jenkins Global Tool Configuration
        allure 'allure'
    }

    environment {
        BASE_URL = "http://localhost:5000"
        API_TIMEOUT = "10"
    }

    stages {

        stage('Clean Workspace') {
            steps {
                // Clean old reports to avoid conflicts
                bat 'if exist reports rmdir /s /q reports'
            }
        }

        stage('Setup Python') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                venv\\Scripts\\python -m pytest ^
                -n 4 ^
                --html=reports/report.html ^
                --self-contained-html ^
                --alluredir=reports/allure-results
                '''
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML(target: [
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Pytest Report',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: true
                ])
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: 'reports/allure-results']]
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed'
        }
        success {
            echo 'All tests passed successfully ✅'
        }
        failure {
            echo 'Some tests failed ❌'
        }
    }
}
