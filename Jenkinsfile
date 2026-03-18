pipeline {
    agent any

    environment {
        BASE_URL = "http://localhost:5000"
        API_TIMEOUT = "10"
    }

    stages {


        stage('Setup Python') {
    steps {
        bat 'python -m venv venv'
        bat 'venv\\Scripts\\python -m pip install --upgrade pip'
        bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
    }
}

       stage('Run Tests') {
    steps {
        bat 'venv\\Scripts\\python -m pytest -n 4 --html=reports/report.html --self-contained-html --alluredir=reports/allure-results'
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
                allure includeProperties: false, jdk: '', results: [[path: 'reports/allure-results']]
            }
        }
    }
}
