pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-minor-app:latest .'
            }
        }
        stage('Deploy Container') {
            steps {
                sh 'docker rm -f devops-minor-app || true'
                sh 'docker run -d --name devops-minor-app --restart unless-stopped -p 80:5000 devops-minor-app:latest'
            }
        }
        stage('Health Check') {
            steps {
                sh 'sleep 3'
                sh 'curl -fsS http://127.0.0.1/health'
            }
        }
    }
    post {
        success { echo 'Deployment completed successfully.' }
        failure { echo 'Pipeline failed. Check the console output.' }
    }
}
